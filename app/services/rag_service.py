from loguru import logger

from app.rag.retriever import MedicalRetriever
from app.rag.reranker import ReRanker


class RAGService:

    def __init__(self):

        self.retriever = MedicalRetriever()

        self.reranker = ReRanker()

    def retrieve_medical_context(
        self,
        query: str
    ):

        try:
            retrieval_results = (
                self.retriever.retrieve(query)
            )

            documents = retrieval_results.get(
                "documents",
                []
            )

            ranked_documents = (
                self.reranker.rerank(
                    query=query,
                    documents=documents
                )
            )

            logger.info(
                "RAG retrieval completed"
            )

            return {
                "success": True,
                "query": query,
                "documents": ranked_documents
            }

        except Exception as e:

            logger.error(
                f"RAG Service Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }