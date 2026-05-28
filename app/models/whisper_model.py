import whisper

from loguru import logger

from app.config.settings import settings


class WhisperModel:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

            cls._instance.initialize_model()

        return cls._instance

    def initialize_model(self):

        try:
            logger.info(
                f"Loading Whisper model: "
                f"{settings.WHISPER_MODEL}"
            )

            self.model = whisper.load_model(
                settings.WHISPER_MODEL
            )

            logger.info(
                "Whisper model initialized"
            )

        except Exception as e:

            logger.error(
                f"Whisper Initialization Error: {e}"
            )

    def transcribe(self, audio_path: str):

        try:
            result = self.model.transcribe(
                audio_path
            )

            logger.info(
                "Audio transcription completed"
            )

            return result["text"]

        except Exception as e:

            logger.error(
                f"Transcription Error: {e}"
            )

            return ""