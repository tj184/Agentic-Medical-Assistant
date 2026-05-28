from langchain_community.chat_models import ChatOllama

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
                f"Loading Ollama model: "
                f"{settings.OLLAMA_MODEL}"
            )

            self.llm = ChatOllama(
                model=settings.OLLAMA_MODEL,
                temperature=0.2,
                base_url=settings.OLLAMA_BASE_URL
            )

            logger.info("LLM initialized successfully")

        except Exception as e:

            logger.error(f"LLM Initialization Error: {e}")

    def generate_response(self, prompt: str):

        try:
            response = self.llm.invoke(prompt)

            return response.content

        except Exception as e:

            logger.error(f"LLM Response Error: {e}")

            return "LLM response generation failed."