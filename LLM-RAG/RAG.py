import os
import re
import torch
import pandas as pd
import numpy as np
from glob import glob
from typing import List, Dict, Tuple
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
from transformers import AutoTokenizer, AutoModel, AutoModelForSequenceClassification, pipeline


load_dotenv()

# ======================== Configuration Parameters ========================

MARKDOWN_DIR = ""

IMPACT_FACTOR_CSV = ""

QWEN3_EMBEDDING_MODEL = ""
QWEN3_RANKER_MODEL = ""

CHROMA_DB_PATH = ""

EMBEDDING_DIM = 768



def load_and_split_markdown_docs() -> List[Dict]:
    """Load and split Markdown documents"""

    impact_factor_df = pd.read_csv(IMPACT_FACTOR_CSV)
    impact_factor_map = dict(zip(impact_factor_df["article_id"], impact_factor_df["impact_factor"]))

    docs_with_meta = []

    for md_file in glob(os.path.join(MARKDOWN_DIR, "*.md")):

        article_id = re.search(r"article_(\d+)\.md", md_file).group(1)

        loader = UnstructuredMarkdownLoader(md_file)
        raw_doc = loader.load()[0]

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=50,
            separators=["\n\n", "\n", ".", " ", ""]
        )
        chunks = text_splitter.split_text(raw_doc.page_content)

        for chunk_idx, chunk in enumerate(chunks):
            docs_with_meta.append({
                "text": chunk,
                "metadata": {
                    "article_id": article_id,
                    "impact_factor": impact_factor_map.get(article_id, 0.0),  # Default 0 (no data)
                    "file_name": os.path.basename(md_file),
                    "chunk_idx": chunk_idx
                }
            })

    print(f"Preprocessing completed: Loaded {len(docs_with_meta)} document chunks in total")
    return docs_with_meta


# ======================== 2. Qwen3 Embedding Model ========================
class Qwen3EmbeddingFunction:
    """Custom Qwen3 embedding function (adapted for Chroma interface)"""

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(QWEN3_EMBEDDING_MODEL, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(QWEN3_EMBEDDING_MODEL, trust_remote_code=True).half().cuda()  # FP16 acceleration
        self.model.eval()

    def __call__(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for input texts"""

        embeddings = []
        for text in texts:

            prompt = f"<|im_start|>user\n{text}<|im_end|>\n<|im_start|>assistant\n"
            inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True).to("cuda")


            with torch.no_grad():
                outputs = self.model(**inputs)
                embedding = outputs.last_hidden_state.mean(dim=1).squeeze().cpu().numpy().tolist()

            embeddings.append(embedding)
        return embeddings


# ======================== 3. Build Chroma Vector Database ========================
def build_chroma_kb(docs: List[Dict]) -> chromadb.Collection:
    """Initialize Chroma and build vector knowledge base (HNSW index)"""

    chroma_client = chromadb.PersistentClient(
        path=CHROMA_DB_PATH,
        settings=Settings(anonymized_telemetry=False)
    )


    qwen3_embedding_fn = Qwen3EmbeddingFunction()

    collection = chroma_client.get_or_create_collection(
        name="materials_science_kb",
        embedding_function=qwen3_embedding_fn,
        metadata={"hnsw:space": "cosine"}
    )


    texts = [doc["text"] for doc in docs]
    metadatas = [doc["metadata"] for doc in docs]
    ids = [f"doc_{i}" for i in range(len(docs))]


    batch_size = 1000
    for i in range(0, len(texts), batch_size):
        batch_texts = texts[i:i + batch_size]
        batch_metas = metadatas[i:i + batch_size]
        batch_ids = ids[i:i + batch_size]
        collection.add(
            documents=batch_texts,
            metadatas=batch_metas,
            ids=batch_ids
        )

    print(f"Chroma vector database built successfully: Stored {collection.count()} vectors in total")
    return collection


# ======================== 4. Retrieval and Reranking ========================
def retrieve_and_rerank(query: str, collection: chromadb.Collection, top_k: int = 20) -> List[Tuple[str, float]]:
    """Retrieve candidate paragraphs and rerank via Qwen3 Ranker (50% semantic + 50% impact factor)"""

    qwen3_embedding_fn = Qwen3EmbeddingFunction()
    query_embedding = qwen3_embedding_fn([query])[0]

    # Retrieve top_k candidates
    initial_results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )


    candidates = []
    for doc, meta, distance in zip(
            initial_results["documents"][0],
            initial_results["metadatas"][0],
            initial_results["distances"][0]
    ):

        semantic_score = 1 - distance
        impact_factor = meta["impact_factor"]

        # Normalize impact factor (assumed range 0-10, scaled to 0-1)
        normalized_impact = min(impact_factor / 10, 1.0)

        candidates.append({
            "text": doc,
            "semantic_score": semantic_score,
            "impact_score": normalized_impact,
            "metadata": meta
        })


    ranker_tokenizer = AutoTokenizer.from_pretrained(QWEN3_RANKER_MODEL, trust_remote_code=True)
    ranker_model = AutoModelForSequenceClassification.from_pretrained(QWEN3_RANKER_MODEL,
                                                                      trust_remote_code=True).half().cuda()
    ranker_pipeline = pipeline(
        "text-classification",
        model=ranker_model,
        tokenizer=ranker_tokenizer,
        device=0  # GPU acceleration
    )


    ranker_inputs = [[query, cand["text"]] for cand in candidates]
    ranker_scores = [res["score"] for res in ranker_pipeline(ranker_inputs)]


    for i, cand in enumerate(candidates):
        combined_score = 0.5 * ranker_scores[i] + 0.5 * cand["impact_score"]
        candidates[i]["combined_score"] = combined_score


    sorted_candidates = sorted(candidates, key=lambda x: x["combined_score"], reverse=True)

    return [(cand["text"], cand["combined_score"]) for cand in sorted_candidates[:10]]  # Return top10



def qa_generate(query: str, collection: chromadb.Collection) -> str:
    """Retrieval + generation QA pipeline"""

    retrieved_docs = retrieve_and_rerank(query, collection)
    context = "\n\n".join([doc for doc, _ in retrieved_docs])


    tokenizer = AutoTokenizer.from_pretrained(QWEN3_EMBEDDING_MODEL, trust_remote_code=True)
    generator = pipeline(
        "text-generation",
        model=AutoModel.from_pretrained(QWEN3_EMBEDDING_MODEL, trust_remote_code=True).half().cuda(),
        tokenizer=tokenizer,
        device=0
    )


    prompt = f"""<|im_start|>system
You are an expert in materials science, answer questions based on the following reference documents.
Reference documents:
{context}

Ensure the answer is accurate, concise, and cite key information from the reference documents.<|im_end|>
<|im_start|>user
{query}<|im_end|>
<|im_start|>assistant
"""


    response = generator(
        prompt,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    return response[0]["generated_text"].split("<|im_start|>assistant\n")[-1]



if __name__ == "__main__":

    docs = load_and_split_markdown_docs()


    collection = build_chroma_kb(docs)


    query = ""
    answer = qa_generate(query, collection)

    print(f"Query: {query}\n")
    print(f"Answer: {answer}")