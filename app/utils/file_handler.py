import os
import shutil

from loguru import logger

from app.config.constants import (
    SUPPORTED_IMAGE_TYPES,
    SUPPORTED_AUDIO_TYPES,
    SUPPORTED_DOCUMENT_TYPES
)


class FileHandler:

    def __init__(self):

        os.makedirs(
            "uploads/images",
            exist_ok=True
        )

        os.makedirs(
            "uploads/audio",
            exist_ok=True
        )

        os.makedirs(
            "uploads/documents",
            exist_ok=True
        )

    def save_file(
        self,
        source_path: str,
        destination_folder: str
    ):

        try:
            filename = os.path.basename(
                source_path
            )

            destination_path = os.path.join(
                destination_folder,
                filename
            )

            shutil.copy(
                source_path,
                destination_path
            )

            logger.info(
                f"File saved: {destination_path}"
            )

            return {
                "success": True,
                "path": destination_path
            }

        except Exception as e:

            logger.error(
                f"File Save Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }

    def validate_file_type(
        self,
        filename: str
    ):

        extension = os.path.splitext(
            filename
        )[1].lower()

        supported_extensions = (
            SUPPORTED_IMAGE_TYPES
            + SUPPORTED_AUDIO_TYPES
            + SUPPORTED_DOCUMENT_TYPES
        )

        return extension in supported_extensions