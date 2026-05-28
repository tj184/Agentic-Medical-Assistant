from langchain_community.chat_models import ChatOllama
from loguru import logger


class RetrievalAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3",
            temperature=0
        )

    def retrieve_medical_context(self, query: str):

        try:
            # Placeholder for RAG integration
            # Later this will connect with ChromaDB

            retrieved_context = """
            Fever and cough may indicate viral infections,
            influenza, bronchitis, or pneumonia.
            Persistent chest pain requires emergency evaluation.
            """

            prompt = f"""
            User Query:
            {query}

            Retrieved Medical Context:
            {retrieved_context}

            Generate a medically informative response.
            """

            response = self.llm.invoke(prompt)

            logger.info("Medical retrieval completed")

            return {
                "agent": "RetrievalAgent",
                "retrieved_context": retrieved_context,
                "response": response.content
            }

        except Exception as e:
            logger.error(f"RetrievalAgent Error: {e}")

            return {
                "agent": "RetrievalAgent",
                "error": str(e)
            }