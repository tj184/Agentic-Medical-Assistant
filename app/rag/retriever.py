from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.vector_store = VectorStore()

    def retrieve(
        self,
        query_embedding,
        top_k=5
    ):

        return self.vector_store.search(
            query_embedding,
            top_k
        )