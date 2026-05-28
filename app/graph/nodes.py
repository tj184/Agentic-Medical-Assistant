from loguru import logger

from app.graph.state import MedicalState

from app.tools.symptom_parser import SymptomParser
from app.tools.emergency_detector import EmergencyDetector
from app.tools.drug_checker import DrugChecker

from app.services.rag_service import RAGService
from app.services.report_service import ReportService

from app.agents.supervisor_agent import SupervisorAgent


# -------------------------
# INITIALIZE COMPONENTS
# -------------------------

symptom_parser = SymptomParser()

emergency_detector = EmergencyDetector()

drug_checker = DrugChecker()

rag_service = RAGService()

report_service = ReportService()

supervisor_agent = SupervisorAgent()


# -------------------------
# SYMPTOM NODE
# -------------------------

def symptom_analysis_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running symptom analysis node"
        )

        patient_text = state.get(
            "patient_text",
            ""
        )

        result = symptom_parser.extract_symptoms(
            patient_text
        )

        state["symptoms"] = result.get(
            "symptoms",
            []
        )

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["symptom_analysis"]
        )

        state["current_step"] = (
            "symptom_analysis_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"Symptom Node Error: {e}"
        )

        state["error"] = str(e)

        return state


# -------------------------
# EMERGENCY NODE
# -------------------------

def emergency_detection_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running emergency detection node"
        )

        symptoms = state.get(
            "symptoms",
            []
        )

        result = emergency_detector.detect(
            symptoms
        )

        state["emergency_detected"] = (
            result.get("emergency", False)
        )

        state["emergency_details"] = result

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["emergency_detection"]
        )

        state["current_step"] = (
            "emergency_detection_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"Emergency Node Error: {e}"
        )

        state["error"] = str(e)

        return state


# -------------------------
# DRUG ANALYSIS NODE
# -------------------------

def drug_analysis_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running drug analysis node"
        )

        medicines = state.get(
            "medicines",
            []
        )

        result = drug_checker.check_interactions(
            medicines
        )

        state["drug_analysis"] = result

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["drug_analysis"]
        )

        state["current_step"] = (
            "drug_analysis_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"Drug Node Error: {e}"
        )

        state["error"] = str(e)

        return state


# -------------------------
# RAG NODE
# -------------------------

def rag_retrieval_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running RAG retrieval node"
        )

        symptoms = state.get(
            "symptoms",
            []
        )

        query = (
            " ".join(symptoms)
        )

        result = rag_service.retrieve_medical_context(
            query
        )

        state["retrieved_documents"] = (
            result.get("documents", [])
        )

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["rag_retrieval"]
        )

        state["current_step"] = (
            "rag_retrieval_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"RAG Node Error: {e}"
        )

        state["error"] = str(e)

        return state


# -------------------------
# DIAGNOSIS NODE
# -------------------------

def diagnosis_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running diagnosis node"
        )

        symptoms = state.get(
            "symptoms",
            []
        )

        medicines = state.get(
            "medicines",
            []
        )

        result = supervisor_agent.process_case(
            symptoms=symptoms,
            medicines=medicines
        )

        state["diagnosis"] = result

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["diagnosis"]
        )

        state["current_step"] = (
            "diagnosis_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"Diagnosis Node Error: {e}"
        )

        state["error"] = str(e)

        return state


# -------------------------
# REPORT NODE
# -------------------------

def report_generation_node(
    state: MedicalState
):

    try:
        logger.info(
            "Running report generation node"
        )

        report_result = (
            report_service.generate_report(
                patient_data=state
            )
        )

        state["report"] = report_result.get(
            "report",
            ""
        )

        state["completed_steps"] = (
            state.get("completed_steps", [])
            + ["report_generation"]
        )

        state["current_step"] = (
            "workflow_completed"
        )

        return state

    except Exception as e:

        logger.error(
            f"Report Node Error: {e}"
        )

        state["error"] = str(e)

        return state