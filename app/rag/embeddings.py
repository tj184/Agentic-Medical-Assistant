from sentence_transformers import SentenceTransformer
from loguru import logger


class EmbeddingModel:

    def __init__(self, model_name="BAAI/bge-large-en"):

        logger.info(f"Loading embedding model: {model_name}")

        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):

        try:
            embedding = self.model.encode(text).tolist()

            return embedding

        except Exception as e:
            logger.error(f"Embedding Error: {e}")
            return None

    def embed_documents(self, documents: list):

        try:
            embeddings = self.model.encode(documents).tolist()

            return embeddings

        except Exception as e:
            logger.error(f"Document Embedding Error: {e}")
            return []