from loguru import logger


class EmergencyAgent:

    def __init__(self):
        self.emergency_keywords = [
            "chest pain",
            "shortness of breath",
            "stroke",
            "unconscious",
            "severe bleeding",
            "heart attack",
            "difficulty breathing"
        ]

    def detect_emergency(self, symptoms: list):

        try:
            detected_emergencies = []

            for symptom in symptoms:
                symptom_lower = symptom.lower()

                for keyword in self.emergency_keywords:
                    if keyword in symptom_lower:
                        detected_emergencies.append(keyword)

            if detected_emergencies:
                logger.warning("Emergency symptoms detected")

                return {
                    "agent": "EmergencyAgent",
                    "emergency": True,
                    "detected": detected_emergencies,
                    "message": "Immediate medical attention recommended"
                }

            return {
                "agent": "EmergencyAgent",
                "emergency": False,
                "message": "No emergency indicators detected"
            }

        except Exception as e:
            logger.error(f"EmergencyAgent Error: {e}")

            return {
                "agent": "EmergencyAgent",
                "error": str(e)
            }