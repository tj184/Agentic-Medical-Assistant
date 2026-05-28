from loguru import logger

from app.agents.supervisor_agent import SupervisorAgent
from app.tools.symptom_parser import SymptomParser
from app.tools.emergency_detector import EmergencyDetector
from app.tools.drug_checker import DrugChecker


class DiagnosisService:

    def __init__(self):

        self.supervisor_agent = SupervisorAgent()

        self.symptom_parser = SymptomParser()

        self.emergency_detector = EmergencyDetector()

        self.drug_checker = DrugChecker()

    def process_diagnosis(
        self,
        patient_text: str,
        medicines: list
    ):

        try:
            # -------------------------
            # Symptom Extraction
            # -------------------------

            symptoms_result = (
                self.symptom_parser.extract_symptoms(
                    patient_text
                )
            )

            symptoms = symptoms_result.get(
                "symptoms",
                []
            )

            # -------------------------
            # Emergency Detection
            # -------------------------

            emergency_result = (
                self.emergency_detector.detect(
                    symptoms
                )
            )

            # -------------------------
            # Drug Interaction Check
            # -------------------------

            drug_result = (
                self.drug_checker.check_interactions(
                    medicines
                )
            )

            # -------------------------
            # AI Diagnosis
            # -------------------------

            diagnosis_result = (
                self.supervisor_agent.process_case(
                    symptoms=symptoms,
                    medicines=medicines
                )
            )

            logger.info(
                "Diagnosis pipeline completed"
            )

            return {
                "success": True,
                "symptoms": symptoms,
                "emergency": emergency_result,
                "drug_analysis": drug_result,
                "diagnosis": diagnosis_result
            }

        except Exception as e:

            logger.error(
                f"Diagnosis Service Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }