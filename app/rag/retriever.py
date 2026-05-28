from rank_bm25 import BM25Okapi
from loguru import logger

from app.rag.vector_store import VectorStore


class MedicalRetriever:

    def __init__(self):

        self.vector_store = VectorStore()

    def retrieve(self, query: str, top_k: int = 5):

        try:
            vector_results = self.vector_store.search(
                query=query,
                n_results=top_k
            )

            documents = []

            if vector_results and "documents" in vector_results:
                docs = vector_results["documents"][0]

                for doc in docs:
                    documents.append(doc)

            logger.info("Medical retrieval successful")

            return {
                "query": query,
                "documents": documents
            }

        except Exception as e:
            logger.error(f"Retriever Error: {e}")

            return {
                "query": query,
                "documents": []
            }