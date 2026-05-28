import chromadb

from app.config.settings import settings


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_DB_PATH
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=settings.CHROMA_COLLECTION
            )
        )

    def add_documents(
        self,
        chunks,
        embeddings
    ):

        ids = []

        documents = []

        metadatas = []

        for i, chunk in enumerate(chunks):

            ids.append(str(i))

            documents.append(
                chunk["content"]
            )

            metadatas.append({
                "source": chunk["source"]
            })

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[
                query_embedding
            ],
            n_results=top_k
        )

        return results