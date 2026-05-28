import ollama

from loguru import logger

from app.config.settings import settings


class LLMModel:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.initialize_model()

        return cls._instance

    def initialize_model(self):

        try:

            logger.info(
                f"Using Ollama model: "
                f"{settings.OLLAMA_MODEL}"
            )

            self.model_name = (
                settings.OLLAMA_MODEL
            )

            logger.info(
                "LLM initialized successfully"
            )

        except Exception as e:

            logger.error(
                f"LLM Initialization Error: {e}"
            )

    def generate_response(
        self,
        prompt: str
    ):

        try:

            response = ollama.chat(

                model=self.model_name,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response[
                "message"
            ][
                "content"
            ]

        except Exception as e:

            logger.error(
                f"LLM Response Error: {e}"
            )

            return (
                "LLM response generation failed."
            )