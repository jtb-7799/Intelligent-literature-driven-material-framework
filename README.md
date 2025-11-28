# Intelligent Literature-Driven Material Framework for Data Mining and Performance Prediction of Invar Alloy

---

## 📖 Project Overview

In this work, an integrated literature intelligence-driven material framework is developed to predict the Coefficient of Thermal Expansion (CTE) of Invar alloys. Optical Character Recognition (OCR), Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG) technologies are combined to establish a closed-loop workflow, including:

- Literature acquisition

- Structured data extraction

- Materials information mining

- Interpretable performance prediction

Within this framework, 120 data entries and 323 potential machine-learning features are collected. Feature selection is performed using a genetic algorithm to identify an optimal subset, yielding a prediction coefficient of determination (*R²*) of 0.935 after ten-fold cross-validation. This approach provides a generalizable pathway for intelligent research and development in materials science.

## 🌟 Core Features

- 📄 **PDF Parsing**: Supports structured PDF content extraction (based on Mineru: `PyPDF2` + `magic-pdf`)
- 🔍 **Text Analysis**: Invokes OpenAI API to implement intelligent Q&A for PDF content
- 📊 **Data Processing**: Completes data cleaning and analysis based on `pandas`/`numpy`
- 🗂️ **Vector Retrieval**: Builds a PDF text vector database via LangChain + Chromadb, supporting semantic search

## 🚀 Usage

### 1. Environment Preparation

1. Install dependencies `pip install -r requirements.txt`
2. Configure environment variables: Create a `.env` file in the project root to store sensitive information `# OpenAI Configuration ``OPENAI_API_KEY=your-openai-api-key ``OPENAI_BASE_URL=optional-custom-base-url `` ``# Path Configuration ``MODEL_STORAGE_PATH=./models ``CHROMADB_STORAGE_PATH=./chroma_db`

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](https://www.doubao.cn) file for details.

The MIT License allows free use, modification, and distribution, both commercially and non-commercially, as long as the original copyright and license notice are included.



