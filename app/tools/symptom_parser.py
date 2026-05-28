import re
from loguru import logger


class SymptomParser:

    def __init__(self):

        self.known_symptoms = [
            "fever",
            "cough",
            "headache",
            "chest pain",
            "shortness of breath",
            "fatigue",
            "vomiting",
            "nausea",
            "dizziness",
            "sore throat",
            "diarrhea",
            "body pain"
        ]

    def extract_symptoms(self, text: str):

        try:
            text = text.lower()

            detected_symptoms = []

            for symptom in self.known_symptoms:

                pattern = rf"\b{re.escape(symptom)}\b"

                if re.search(pattern, text):
                    detected_symptoms.append(symptom)

            logger.info("Symptom extraction completed")

            return {
                "success": True,
                "symptoms": detected_symptoms
            }

        except Exception as e:

            logger.error(f"Symptom Parser Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }