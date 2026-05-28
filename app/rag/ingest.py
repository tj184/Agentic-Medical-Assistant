import os
from pypdf import PdfReader
from loguru import logger

from app.rag.chunking import TextChunker
from app.rag.vector_store import VectorStore


class MedicalDataIngestion:

    def __init__(self):

        self.chunker = TextChunker()
        self.vector_store = VectorStore()

    def read_pdf(self, file_path: str):

        try:
            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:
                text += page.extract_text() + "\n"

            logger.info(f"PDF Loaded: {file_path}")

            return text

        except Exception as e:
            logger.error(f"PDF Read Error: {e}")
            return ""

    def ingest_pdf(self, file_path: str):

        try:
            raw_text = self.read_pdf(file_path)

            chunks = self.chunker.chunk_text(raw_text)

            documents = []

            for index, chunk in enumerate(chunks):

                documents.append({
                    "text": chunk,
                    "metadata": {
                        "source": file_path,
                        "chunk_id": index
                    }
                })

            self.vector_store.add_documents(documents)

            logger.info(f"Ingestion completed for: {file_path}")

        except Exception as e:
            logger.error(f"Ingestion Error: {e}")

    def ingest_directory(self, directory_path: str):

        try:
            for filename in os.listdir(directory_path):

                if filename.endswith(".pdf"):

                    file_path = os.path.join(directory_path, filename)

                    self.ingest_pdf(file_path)

            logger.info("Directory ingestion completed")

        except Exception as e:
            logger.error(f"Directory Ingestion Error: {e}")