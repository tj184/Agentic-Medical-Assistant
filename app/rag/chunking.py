from langchain.text_splitter import RecursiveCharacterTextSplitter
from loguru import logger


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_text(self, text: str):

        try:
            chunks = self.splitter.split_text(text)

            logger.info(f"Generated {len(chunks)} chunks")

            return chunks

        except Exception as e:
            logger.error(f"Chunking Error: {e}")
            return []