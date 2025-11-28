import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional

import pandas as pd
from openai import OpenAI
from pydantic import BaseSettings
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from io import StringIO

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


# Configuration management
class Settings(BaseSettings):
    """Project configuration class (read from environment variables or .env file)"""
    openai_api_key: str
    openai_base_url: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    target_folder: str = "./data"  # Default MD file storage directory
    model_name: str = "qwen-plus"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Load configuration
load_dotenv()
settings = Settings()

# Initialize OpenAI client
client = OpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_base_url
)


class MDFileProcessor:
    """MD file processing class"""

    @staticmethod
    def get_md_files(folder_path: str) -> List[Path]:
        """Get all MD files in the specified directory (exclude ipynb checkpoints)"""
        folder = Path(folder_path)
        md_files = list(folder.rglob("*.md"))
        return [f for f in md_files if ".ipynb_checkpoints" not in str(f)]

    @staticmethod
    def read_md_file(file_path: Path) -> Optional[str]:
        """Read content of a single MD file"""
        try:
            return file_path.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Failed to read file {file_path}: {e}")
            return None

    @staticmethod
    def clean_text(text: str) -> str:
        """Text cleaning: remove special characters and correct format"""
        # Remove soft hyphens
        text = text.replace("\xad", "")
        # Replace academic symbols
        text = text.replace("$\\O=$", "$\\approx$")
        # Remove control characters
        text = re.sub(r"[\x00-\x1F\x7F]", "", text)
        # Simplify formula symbols
        text = re.sub(r"\$\\times\$", "×", text)
        text = re.sub(r"\$\\mathrm\{(\w+)\}\$", r"\1", text)
        text = re.sub(r"\$\{\\circ\}\$", "°", text)
        text = re.sub(r"\$|\{|\}", "", text)
        return text

    @staticmethod
    def extract_content(
            content: str, file_path: Path
    ) -> Tuple[str, List[str], List[str], List[str]]:
        """Extract title, main text, tables and table titles from MD file"""
        # Extract title (file path conversion)
        title = str(file_path.relative_to(settings.target_folder)).replace(".md", "")

        # Truncate reference section (after REFERENCES/ACKNOWLEDGMENTS)
        references_pattern = re.compile(
            r"^#{1,6}\s*(REFERENCES|REFERENCE|ACKNOWLEDGMENT|ACKNOWLEDGMENTS)\b[:\s]*",
            re.IGNORECASE | re.MULTILINE
        )
        match = references_pattern.search(content)
        process_content = content[:match.start()].strip() if match else content.strip()

        # Remove irrelevant content like images and tables
        process_content = re.sub(r"\(images/.*?\)\s*\nFig\.\s*\d+\.\s*.*\n?", "", process_content)
        process_content = re.sub(r"[\u2000-\u200F\u0000-\u001F]", " ", process_content)
        process_content = re.sub(r"!\[.*?\]\(.*?\)", "", process_content)
        process_content = re.sub(r"!\[\]", " ", process_content)

        # Extract tables and titles
        table_pattern = re.compile(r"<table>(.*?)</table>", re.DOTALL)
        tables = [f"<table>{match}</table>" for match in table_pattern.findall(content)]

        table_title_pattern = re.compile(r"([^\n]+)\s*<html>", re.DOTALL)
        table_titles = table_title_pattern.findall(content)

        # Clean text after removing table content
        process_content = table_pattern.sub("", process_content)
        process_content = re.sub(r"(?i) {3,}table\s+\d+.*?</html>", "", process_content, flags=re.DOTALL)
        process_content = MDFileProcessor.clean_text(process_content)

        # Split sentences by #
        sentences = [s.strip() for s in process_content.split("#") if s.strip()]

        return title, sentences, tables, table_titles

    @staticmethod
    def split_sentences(sentences: List[str]) -> List[List[str]]:
        """Split sentences by punctuation (avoid splitting decimal points)"""
        split_sentences = []
        for text in sentences:
            parts = re.split(r"(?<!\d)\.(?!\d)|[!?]", text)
            parts = [p.strip() for p in parts if p.strip() and p.count(" ") >= 5]
            split_sentences.append(parts)
        return split_sentences


class LLMService:
    """LLM interaction service class"""

    @staticmethod
    def _call_llm(prompt: str, system_prompt: str = "You are an expert in the field of Invar alloy.") -> Optional[str]:
        """General LLM call method"""
        try:
            completion = client.chat.completions.create(
                model=settings.model_name,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                stream=True,
                stream_options={"include_usage": True},
                extra_body={"enable_thinking": False},
                max_tokens=4096,
                seed=42,
                timeout=30
            )

            response = ""
            for chunk in completion:
                if chunk.choices and chunk.choices[0].delta.content:
                    response += chunk.choices[0].delta.content
            return response.strip()
        except Exception as e:
            logger.error(f"LLM call failed: {e}")
            return None

    @staticmethod
    def classify_invar_content(text: str) -> bool:
        """Determine if text contains Invar alloy related entities"""
        prompt = ""
        response = LLMService._call_llm(prompt)
        return response and response.lower() == "yes"

    @staticmethod
    def extract_invar_entities(text: str) -> List[str]:
        """Extract Invar alloy metal entities from text"""
        prompt = ""
        response = LLMService._call_llm(prompt)
        if not response:
            return []

        entities = re.findall(r"@@([^@#]+)##", response)
        return list(dict.fromkeys(entities))  # Remove duplicates

    @staticmethod
    def extract_relation(entity: str, text: str) -> Optional[Dict]:
        """Extract relation information for a single entity"""
        prompt = ""
        response = LLMService._call_llm(prompt)
        if not response:
            return None

        try:
            result = json.loads(response)
            # Filter results with all null values
            required_keys = ["composition", "annealing temperature", "thermal expansion test temperature range",
                             "coefficient of thermal expansion (CTE)"]
            if any(result.get(key) != "null" for key in required_keys):
                return result
            logger.warning(f"No valid relation data for entity {entity}")
            return None
        except json.JSONDecodeError:
            logger.error(f"Failed to parse relation extraction result: {response}")
            return None

    @staticmethod
    def verify_relation(relation: Dict, text: str) -> Optional[Dict]:
        """Verify accuracy of relation extraction results (remove hallucinations)"""
        verified = {"metal entity": relation["metal entity"], "txt": relation["txt"]}
        required_keys = ["composition", "annealing temperature", "thermal expansion test temperature range",
                         "coefficient of thermal expansion (CTE)"]

        for key in required_keys:
            value = relation.get(key)
            if value == "null":
                verified[key] = []
                continue

            prompt = ""
            response = LLMService._call_llm(prompt)
            if response == "Yes":
                verified[key] = [value]
            else:
                verified[key] = []

        if any(verified[key] for key in required_keys):
            return verified
        return None

    @staticmethod
    def classify_table_title(title: str) -> bool:
        """Determine if table title belongs to Invar alloy related category"""
        prompt = ""
        response = LLMService._call_llm(prompt)
        return response and response.lower() == "yes"

    @staticmethod
    def extract_table_relation(table_content: str) -> Optional[List[Dict]]:
        """Extract relation information from table"""
        prompt = ""
        response = LLMService._call_llm(prompt)
        if not response:
            return None

        try:
            results = json.loads(response)
            # Filter results with all null values
            required_keys = ["composition", "annealing temperature", "thermal expansion test temperature range",
                             "coefficient of thermal expansion (CTE)"]
            return [r for r in results if any(r.get(key) != "null" for key in required_keys)]
        except json.JSONDecodeError:
            logger.error(f"Failed to parse table relation extraction result: {response}")
            return None


class ResultExporter:
    """Result export class"""

    @staticmethod
    def parse_html_table(table_html: str) -> Optional[pd.DataFrame]:
        """Parse HTML table to DataFrame"""
        try:
            soup = BeautifulSoup(table_html, "html5lib")
            table = soup.find("table")
            if not table:
                return None
            return pd.read_html(StringIO(str(table)))[0]
        except Exception as e:
            logger.error(f"Table parsing failed: {e}")
            return None

    @staticmethod
    def export_excel(
            title: str,
            text_results: List[Dict],
            table_results: List[Dict],
            tables: List[str],
            table_titles: List[str]
    ):
        """Export results to Excel file"""
        output_path = Path(f"{title.replace('/', '_')}.xlsx")
        try:
            with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
                # Write text results
                if text_results:
                    pd.DataFrame(text_results).to_excel(writer, sheet_name="text_relations", index=False)

                # Write table relation results
                if table_results:
                    pd.DataFrame(table_results).to_excel(writer, sheet_name="table_relations", index=False)

                # Write original tables
                table_sheet = writer.book.create_sheet("raw_tables")
                start_row = 0
                for idx, (table_html, table_title) in enumerate(zip(tables, table_titles)):
                    # Write table title
                    table_sheet.cell(row=start_row + 1, column=1, value=table_title)
                    start_row += 1

                    # Write table content
                    table_df = ResultExporter.parse_html_table(table_html)
                    if table_df is not None:
                        table_df.to_excel(writer, sheet_name="raw_tables", index=False, startrow=start_row)
                        start_row += len(table_df) + 2

            logger.info(f"Results exported to: {output_path}")
        except Exception as e:
            logger.error(f"Excel export failed: {e}")


def main():
    """Main function"""
    # 1. Get and process MD files
    md_processor = MDFileProcessor()
    md_files = md_processor.get_md_files(settings.target_folder)
    logger.info(f"Found {len(md_files)} MD files")

    for file_path in md_files:
        logger.info(f"Processing file: {file_path}")

        # Read file content
        content = md_processor.read_md_file(file_path)
        if not content:
            continue

        # Extract content
        title, sentences, tables, table_titles = md_processor.extract_content(content, file_path)
        split_sentences = md_processor.split_sentences(sentences)

        # 2. Process text relation extraction
        text_relations = []
        for sentence_group in split_sentences:
            # Filter Invar alloy related content
            invar_texts = [text for text in sentence_group if LLMService.classify_invar_content(text)]
            if not invar_texts:
                continue

            full_text = ".".join(invar_texts)
            entities = LLMService.extract_invar_entities(full_text)

            if not entities:
                continue

            # Extract relations
            for entity in entities:
                relation = LLMService.extract_relation(entity, full_text)
                if not relation:
                    continue

                # Verify relation (for multiple entities)
                if len(entities) > 1:
                    relation = LLMService.verify_relation(relation, full_text)
                    if not relation:
                        continue

                relation["title"] = title
                text_relations.append(relation)

        # 3. Process table relation extraction
        table_relations = []
        for table_html, table_title in zip(tables, table_titles):
            if LLMService.classify_table_title(table_title):
                table_content = f"{table_title}\n{table_html}"
                relations = LLMService.extract_table_relation(table_content)
                if relations:
                    table_relations.extend(relations)

        # 4. Export results
        ResultExporter.export_excel(title, text_relations, table_relations, tables, table_titles)


if __name__ == "__main__":
    main()