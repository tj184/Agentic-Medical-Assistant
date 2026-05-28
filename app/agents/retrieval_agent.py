from app.models.llm import LLMModel


class RetrievalAgent:

    def __init__(self):

        self.llm = LLMModel()

    def retrieve_medical_information(
        self,
        query: str,
        context: str
    ):

        prompt = f"""
        Use the following medical context
        to answer the query.

        Context:
        {context}

        Query:
        {query}
        """

        return self.llm.generate_response(
            prompt
        )