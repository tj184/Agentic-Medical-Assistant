from loguru import logger

from app.models.llm import LLMModel


class ReportService:

    def __init__(self):

        self.llm = LLMModel()

        with open(
            "app/prompts/report_prompt.txt",
            "r",
            encoding="utf-8"
        ) as file:

            self.report_prompt = file.read()

    def generate_report(
        self,
        patient_data: dict
    ):

        try:
            prompt = f"""
            {self.report_prompt}

            PATIENT DATA:
            {patient_data}
            """

            report = self.llm.generate_response(
                prompt
            )

            logger.info(
                "Medical report generated"
            )

            return {
                "success": True,
                "report": report
            }

        except Exception as e:

            logger.error(
                f"Report Service Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }