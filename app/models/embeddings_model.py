from sentence_transformers import SentenceTransformer

from loguru import logger

from app.config.settings import settings


class EmbeddingModel:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.initialize_model()

        return cls._instance

    def initialize_model(self):

        try:
            logger.info(
                f"Loading embedding model: "
                f"{settings.EMBEDDING_MODEL}"
            )

            self.model = SentenceTransformer(
                settings.EMBEDDING_MODEL
            )

            logger.info(
                "Embedding model initialized"
            )

        except Exception as e:

            logger.error(
                f"Embedding Model Error: {e}"
            )

    def embed_text(self, text: str):

        try:
            embedding = self.model.encode(
                text
            ).tolist()

            return embedding

        except Exception as e:

            logger.error(
                f"Embedding Generation Error: {e}"
            )

            return None

    def embed_documents(self, documents: list):

        try:
            embeddings = self.model.encode(
                documents
            ).tolist()

            return embeddings

        except Exception as e:

            logger.error(
                f"Document Embedding Error: {e}"
            )

            return []