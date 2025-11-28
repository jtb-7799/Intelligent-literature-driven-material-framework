import os
import json
import csv
import logging
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass

import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('invar_extraction.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# Configuration class
@dataclass
class Config:
    """Configuration class for application settings"""
    api_key: str = os.getenv("DASHSCOPE_API_KEY", "")
    base_url: str = os.getenv("DASHSCOPE_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1")
    model_name: str = os.getenv("MODEL_NAME", "qwen-plus")
    max_token_length: int = int(os.getenv("MAX_TOKEN_LENGTH", 8000))
    timeout: int = int(os.getenv("TIMEOUT", 120))


class PDFProcessor:
    """PDF file processing utility class"""

    @staticmethod
    def read_pdf(file_path: str) -> Optional[str]:
        """Read content from a single PDF file"""
        try:
            with open(file_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                content = []
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        content.append(page_text.strip())
                full_text = '\n\n'.join(content)
                logger.info(f"Successfully read PDF: {file_path}")
                return full_text
        except Exception as e:
            logger.error(f"Failed to read PDF {file_path}: {str(e)}")
            return None

    @staticmethod
    def read_all_pdfs_in_folder(folder_path: str) -> List[Tuple[str, str]]:
        """Read all PDF files in specified folder and return their content"""
        pdf_contents = []
        folder = Path(folder_path)

        if not folder.exists():
            logger.error(f"Folder does not exist: {folder_path}")
            return pdf_contents

        for file_path in folder.glob("*.pdf"):
            content = PDFProcessor.read_pdf(str(file_path))
            if content:
                pdf_contents.append((str(file_path), content))

        return pdf_contents

    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        """Truncate text to fit model token limitations while preserving key information"""
        if len(text) <= max_length:
            return text

        # Preserve important information from both start and end
        half_length = max_length // 2
        return text[:half_length] + "\n...[Content truncated]...\n" + text[-half_length:]


class LLMClient:
    """LLM interaction client class"""

    def __init__(self, config: Config):
        self.config = config
        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url
        )

    def extract_invar_info(self, content: str) -> Optional[List[Dict[str, str]]]:
        """Extract Invar alloy information using LLM"""
        # Truncate text to avoid exceeding model token limits
        truncated_content = PDFProcessor.truncate_text(content, self.config.max_token_length)

        prompt = self._build_prompt(truncated_content)

        try:
            response = self.client.chat.completions.create(
                model=self.config.model_name,
                messages=[
                    {"role": "system",
                     "content": "Only return JSON array, no additional text (including code block markers)"},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                timeout=self.config.timeout
            )

            return self._parse_response(response.choices[0].message.content)

        except Exception as e:
            logger.error(f"LLM API call failed: {str(e)}")
            return None

    def _build_prompt(self, content: str) -> str:
        """Build extraction prompt (empty as requested)"""
        return ""

    def _parse_response(self, raw_content: str) -> Optional[List[Dict[str, str]]]:
        """Parse LLM response and clean formatting"""
        if not raw_content:
            logger.warning("Response content is empty")
            return None

        # Clean code block markers
        clean_content = self._clean_response(raw_content)

        try:
            result = json.loads(clean_content)

            if isinstance(result, list):
                return result
            elif isinstance(result, dict):
                logger.warning("Response is single object, converting to list")
                return [result]
            else:
                logger.error(f"Invalid response format: {type(result)}")
                return None

        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {str(e)}")
            logger.debug(f"Raw response: {raw_content}")
            logger.debug(f"Cleaned response: {clean_content}")
            return None

    def _clean_response(self, content: str) -> str:
        """Remove code block markers and clean response content"""
        content = content.strip()

        # Remove markdown code block markers
        if content.startswith('```'):
            lines = []
            in_code_block = False
            for line in content.split('\n'):
                line = line.strip()
                if line.startswith('```'):
                    in_code_block = not in_code_block
                    continue
                if in_code_block:
                    lines.append(line)
                else:
                    # Keep only JSON content if mixed with other text
                    if '{' in line or '[' in line:
                        lines.append(line)

            content = '\n'.join(lines).strip()

        return content


class CSVExporter:
    """CSV file export utility class"""

    @staticmethod
    def get_output_path(pdf_path: str, suffix: str = "_extracted") -> str:
        """Generate output CSV file path based on source PDF path"""
        pdf_path = Path(pdf_path)
        return str(pdf_path.parent / f"{pdf_path.stem}{suffix}.csv")

    @staticmethod
    def save_to_csv(entries: List[Dict[str, str]], output_path: str, source_file: str) -> bool:
        """Save extracted information to CSV file with UTF-8 BOM encoding"""
        fieldnames = [
            'source_file', 'alloy_entities', 'composition',
            'annealing_temp', 'expansion_test_range', 'cte'
        ]

        try:
            # Use UTF-8 BOM encoding for proper Excel display
            with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(
                    csvfile,
                    fieldnames=fieldnames,
                    quoting=csv.QUOTE_ALL  # Quote all fields to handle special characters
                )

                writer.writeheader()

                for entry in entries:
                    row = {
                        'source_file': source_file,
                        'alloy_entities': entry.get('alloy_entities', '') or '',
                        'composition': entry.get('composition', '') or '',
                        'annealing_temp': entry.get('annealing_temp', '') or '',
                        'expansion_test_range': entry.get('expansion_test_range', '') or '',
                        'cte': entry.get('cte', '') or ''
                    }
                    writer.writerow(row)

            logger.info(f"Successfully saved results to: {output_path}")
            return True

        except Exception as e:
            logger.error(f"Failed to save CSV {output_path}: {str(e)}")
            return False


def main():
    """Main function to coordinate PDF processing and information extraction"""
    # Initialize configuration
    config = Config(
        api_key=os.getenv("DASHSCOPE_API_KEY", ""),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model_name="qwen-plus"
    )

    # Check required configuration
    if not config.api_key:
        logger.error("Please configure DASHSCOPE_API_KEY environment variable or set in code")
        return

    # Target folder path
    target_folder = r""

    # Initialize components
    pdf_processor = PDFProcessor()
    llm_client = LLMClient(config)
    csv_exporter = CSVExporter()

    # Read all PDF files
    pdf_files = pdf_processor.read_all_pdfs_in_folder(target_folder)
    logger.info(f"Found {len(pdf_files)} PDF files")

    # Process each PDF file
    success_count = 0
    total_entries = 0

    for pdf_path, content in pdf_files:
        logger.info(f"\nProcessing: {pdf_path}")

        # Extract Invar alloy information
        entries = llm_client.extract_invar_info(content)

        if entries and len(entries) > 0:
            # Generate output path
            output_path = csv_exporter.get_output_path(pdf_path)

            # Save to CSV
            if csv_exporter.save_to_csv(entries, output_path, pdf_path):
                success_count += 1
                total_entries += len(entries)
                logger.info(f"Extracted {len(entries)} Invar alloy records")
        else:
            logger.warning(f"No valid information extracted from {pdf_path}")

    # Output processing statistics
    logger.info(f"\nProcessing completed:")
    logger.info(f"- Successfully processed files: {success_count}/{len(pdf_files)}")
    logger.info(f"- Total extracted records: {total_entries}")


if __name__ == "__main__":
    main()