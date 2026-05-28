from app.agents.symptom_agent import (
    SymptomAgent
)

from app.agents.drug_agent import (
    DrugAgent
)

from app.agents.report_agent import (
    ReportAgent
)

from app.agents.emergency_agent import (
    EmergencyAgent
)


class SupervisorAgent:

    def __init__(self):

        self.symptom_agent = (
            SymptomAgent()
        )

        self.drug_agent = (
            DrugAgent()
        )

        self.report_agent = (
            ReportAgent()
        )

        self.emergency_agent = (
            EmergencyAgent()
        )

    def process_case(
        self,
        symptoms,
        medicines
    ):

        symptom_analysis = (
            self.symptom_agent
            .analyze_symptoms(symptoms)
        )

        drug_analysis = (
            self.drug_agent
            .analyze_drugs(medicines)
        )

        emergency_analysis = (
            self.emergency_agent
            .detect_emergency(symptoms)
        )

        report = (
            self.report_agent
            .generate_report(
                f"""
                Symptoms:
                {symptoms}

                Symptom Analysis:
                {symptom_analysis}

                Drug Analysis:
                {drug_analysis}

                Emergency Analysis:
                {emergency_analysis}
                """
            )
        )

        return {
            "symptom_analysis":
            symptom_analysis,

            "drug_analysis":
            drug_analysis,

            "emergency_analysis":
            emergency_analysis,

            "report":
            report
        }