from app.models.llm import LLMModel


class SymptomAgent:

    def __init__(self):

        self.llm = LLMModel()

    def analyze_symptoms(
        self,
        symptoms: str
    ):

        prompt = f"""
        Analyze the following symptoms.

        Symptoms:
        {symptoms}

        Provide:
        1. Possible conditions
        2. Severity
        3. Recommended action
        """

        response = (
            self.llm.generate_response(
                prompt
            )
        )

        return response