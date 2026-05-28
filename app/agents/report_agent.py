from app.models.llm import LLMModel


class ReportAgent:

    def __init__(self):

        self.llm = LLMModel()

    def generate_report(
        self,
        patient_data: str
    ):

        prompt = f"""
        Generate a professional
        medical report.

        Patient Data:
        {patient_data}
        """

        return self.llm.generate_response(
            prompt
        )