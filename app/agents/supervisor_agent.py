from loguru import logger

from app.agents.symptom_agent import SymptomAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.drug_agent import DrugAgent
from app.agents.report_agent import ReportAgent
from app.agents.emergency_agent import EmergencyAgent


class SupervisorAgent:

    def __init__(self):

        self.symptom_agent = SymptomAgent()
        self.retrieval_agent = RetrievalAgent()
        self.drug_agent = DrugAgent()
        self.report_agent = ReportAgent()
        self.emergency_agent = EmergencyAgent()

    def process_case(self, symptoms: list, medicines: list = None):

        try:
            logger.info("Starting multi-agent workflow")

            # Step 1: Symptom Analysis
            symptom_result = self.symptom_agent.analyze_symptoms(symptoms)

            # Step 2: Emergency Detection
            emergency_result = self.emergency_agent.detect_emergency(symptoms)

            # Step 3: Medical Retrieval
            retrieval_result = self.retrieval_agent.retrieve_medical_context(
                ", ".join(symptoms)
            )

            # Step 4: Drug Analysis
            drug_result = None

            if medicines:
                drug_result = self.drug_agent.analyze_drugs(medicines)

            # Step 5: Report Generation
            final_report = self.report_agent.generate_report({
                "symptoms": symptom_result,
                "retrieval": retrieval_result,
                "drug_analysis": drug_result,
                "emergency": emergency_result
            })

            logger.info("Workflow completed successfully")

            return {
                "symptom_analysis": symptom_result,
                "retrieval": retrieval_result,
                "drug_analysis": drug_result,
                "emergency": emergency_result,
                "final_report": final_report
            }

        except Exception as e:
            logger.error(f"SupervisorAgent Error: {e}")

            return {
                "error": str(e)
            }