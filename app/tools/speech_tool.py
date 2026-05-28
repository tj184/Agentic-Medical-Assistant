import whisper
from loguru import logger


class SpeechTool:

    def __init__(self):

        logger.info("Loading Whisper model")

        self.model = whisper.load_model("base")

    def transcribe_audio(self, audio_path: str):

        try:
            result = self.model.transcribe(audio_path)

            logger.info("Speech transcription completed")

            return {
                "success": True,
                "text": result["text"]
            }

        except Exception as e:

            logger.error(f"Speech Transcription Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }