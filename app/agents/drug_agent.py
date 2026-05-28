from app.models.llm import LLMModel


class DrugAgent:

    def __init__(self):

        self.llm = LLMModel()

    def analyze_drugs(
        self,
        medicines: list
    ):

        prompt = f"""
        Analyze these medicines:

        {medicines}

        Check:
        - interactions
        - risks
        - side effects
        """

        return self.llm.generate_response(
            prompt
        )