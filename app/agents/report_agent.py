from langchain_community.chat_models import ChatOllama
from loguru import logger


class ReportAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3",
            temperature=0.2
        )

    def generate_report(self, data: dict):

        try:
            prompt = f"""
            You are a professional medical report generation AI.

            Generate a detailed medical report using:
            {data}

            Include:
            1. Symptoms Summary
            2. Possible Conditions
            3. Risk Assessment
            4. Drug Warnings
            5. Recommended Next Steps
            6. Emergency Recommendations if needed

            Format professionally.
            """

            response = self.llm.invoke(prompt)

            logger.info("Medical report generated")

            return {
                "agent": "ReportAgent",
                "report": response.content
            }

        except Exception as e:
            logger.error(f"ReportAgent Error: {e}")

            return {
                "agent": "ReportAgent",
                "error": str(e)
            }