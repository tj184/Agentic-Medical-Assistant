from app.models.llm import LLMModel


class EmergencyAgent:

    def __init__(self):

        self.llm = LLMModel()

    def detect_emergency(
        self,
        symptoms: str
    ):

        prompt = f"""
        Detect whether this is a
        medical emergency.

        Symptoms:
        {symptoms}

        Return:
        - Emergency Level
        - Reason
        - Immediate Action
        """

        return self.llm.generate_response(
            prompt
        )