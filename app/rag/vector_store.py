import chromadb
from chromadb.config import Settings
from loguru import logger

from app.rag.embeddings import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/vector_store"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_knowledge"
        )

        self.embedding_model = EmbeddingModel()

        logger.info("ChromaDB initialized")

    def add_documents(self, documents: list):

        try:
            ids = []
            texts = []
            embeddings = []
            metadatas = []

            for index, doc in enumerate(documents):

                ids.append(f"doc_{index}")
                texts.append(doc["text"])
                metadatas.append(doc.get("metadata", {}))

                embedding = self.embedding_model.embed_text(doc["text"])
                embeddings.append(embedding)

            self.collection.add(
                ids=ids,
                documents=texts,
                embeddings=embeddings,
                metadatas=metadatas
            )

            logger.info(f"Added {len(documents)} documents to vector DB")

        except Exception as e:
            logger.error(f"Vector Store Add Error: {e}")

    def search(self, query: str, n_results: int = 5):

        try:
            query_embedding = self.embedding_model.embed_text(query)

            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )

            return results

        except Exception as e:
            logger.error(f"Vector Search Error: {e}")
            return {}