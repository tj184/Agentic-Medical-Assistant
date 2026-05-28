from langchain_community.chat_models import ChatOllama
from loguru import logger


class DrugAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3",
            temperature=0.1
        )

    def analyze_drugs(self, medicines: list):

        try:
            prompt = f"""
            You are a medical drug interaction AI.

            Analyze the following medicines:
            {medicines}

            Return:
            1. Possible drug interactions
            2. Side effects
            3. Safety warnings
            4. Allergy concerns
            5. General precautions

            Keep the response structured.
            """

            response = self.llm.invoke(prompt)

            logger.info("Drug analysis completed")

            return {
                "agent": "DrugAgent",
                "analysis": response.content
            }

        except Exception as e:
            logger.error(f"DrugAgent Error: {e}")

            return {
                "agent": "DrugAgent",
                "error": str(e)
            }