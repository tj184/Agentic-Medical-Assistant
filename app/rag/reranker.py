from sentence_transformers import CrossEncoder
from loguru import logger


class ReRanker:

    def __init__(self):

        logger.info("Loading reranker model")

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query: str, documents: list, top_k: int = 3):

        try:
            pairs = [[query, doc] for doc in documents]

            scores = self.model.predict(pairs)

            scored_docs = list(zip(documents, scores))

            ranked_docs = sorted(
                scored_docs,
                key=lambda x: x[1],
                reverse=True
            )

            top_documents = [doc for doc, score in ranked_docs[:top_k]]

            logger.info("Re-ranking completed")

            return top_documents

        except Exception as e:
            logger.error(f"ReRanker Error: {e}")
            return documents[:top_k]