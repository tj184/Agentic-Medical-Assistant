from loguru import logger


class EmergencyDetector:

    def __init__(self):

        self.emergency_conditions = {
            "heart_attack": [
                "chest pain",
                "shortness of breath"
            ],

            "stroke": [
                "dizziness",
                "confusion"
            ],

            "respiratory_failure": [
                "difficulty breathing",
                "low oxygen"
            ]
        }

    def detect(self, symptoms: list):

        try:
            symptoms = [symptom.lower() for symptom in symptoms]

            detected_emergencies = []

            for condition, required_symptoms in self.emergency_conditions.items():

                matched = all(
                    symptom in symptoms
                    for symptom in required_symptoms
                )

                if matched:
                    detected_emergencies.append(condition)

            if detected_emergencies:

                logger.warning(
                    f"Emergency detected: {detected_emergencies}"
                )

                return {
                    "success": True,
                    "emergency": True,
                    "conditions": detected_emergencies,
                    "message": "Immediate medical attention recommended."
                }

            return {
                "success": True,
                "emergency": False,
                "conditions": [],
                "message": "No emergency detected."
            }

        except Exception as e:

            logger.error(f"Emergency Detector Error: {e}")

            return {
                "success": False,
                "error": str(e)
            }