from paddleocr import PaddleOCR
from loguru import logger


class OCRTool:

    def __init__(self):

        self.ocr = PaddleOCR(
            use_angle_cls=True,
            lang="en"
        )

    def extract_text(self, image_path: str):

        try:
            result = self.ocr.ocr(image_path)

            extracted_text = []

            for line in result[0]:
                text = line[1][0]
                extracted_text.append(text)

            final_text = " ".join(extracted_text)

            logger.info("OCR extraction completed")

            return {
                "success": True,
                "text": final_text
            }

        except Exception as e:

            logger.error(f"OCR Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }