from langchain_community.chat_models import ChatOllama
from loguru import logger


class SymptomAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3",
            temperature=0.2
        )

    def analyze_symptoms(self, symptoms: list):

        try:
            prompt = f"""
            You are an advanced medical symptom analysis AI.

            Analyze the following symptoms:
            {symptoms}
            Return:
            1. Possible medical conditions
            2. Severity level
            3. Recommended medical department
            4. Recommended immediate actions

            Keep the response structured.
            """

            response = self.llm.invoke(prompt)

            logger.info("Symptom analysis completed")

            return {
                "agent": "SymptomAgent",
                "analysis": response.content
            }

        except Exception as e:
            logger.error(f"SymptomAgent Error: {e}")

            return {
                "agent": "SymptomAgent",
                "error": str(e)
            }