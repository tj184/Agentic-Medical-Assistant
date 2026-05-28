from langgraph.graph import StateGraph
from langgraph.graph import END

from loguru import logger

from app.graph.state import MedicalState

from app.graph.nodes import (
    symptom_analysis_node,
    emergency_detection_node,
    drug_analysis_node,
    rag_retrieval_node,
    diagnosis_node,
    report_generation_node
)


class MedicalWorkflow:

    def __init__(self):

        logger.info(
            "Initializing Medical Workflow"
        )

        self.workflow = StateGraph(
            MedicalState
        )

        self.build_workflow()

    def build_workflow(self):

        # -------------------------
        # ADD NODES
        # -------------------------

        self.workflow.add_node(
            "symptom_analysis",
            symptom_analysis_node
        )

        self.workflow.add_node(
            "emergency_detection",
            emergency_detection_node
        )

        self.workflow.add_node(
            "drug_analysis",
            drug_analysis_node
        )

        self.workflow.add_node(
            "rag_retrieval",
            rag_retrieval_node
        )

        self.workflow.add_node(
            "diagnosis",
            diagnosis_node
        )

        self.workflow.add_node(
            "report_generation",
            report_generation_node
        )

        # -------------------------
        # ENTRY POINT
        # -------------------------

        self.workflow.set_entry_point(
            "symptom_analysis"
        )

        # -------------------------
        # EDGES
        # -------------------------

        self.workflow.add_edge(
            "symptom_analysis",
            "emergency_detection"
        )

        self.workflow.add_edge(
            "emergency_detection",
            "drug_analysis"
        )

        self.workflow.add_edge(
            "drug_analysis",
            "rag_retrieval"
        )

        self.workflow.add_edge(
            "rag_retrieval",
            "diagnosis"
        )

        self.workflow.add_edge(
            "diagnosis",
            "report_generation"
        )

        self.workflow.add_edge(
            "report_generation",
            END
        )

        # -------------------------
        # COMPILE
        # -------------------------

        self.app = self.workflow.compile()

        logger.info(
            "Medical workflow compiled"
        )

    def run(
        self,
        patient_text: str,
        medicines: list,
        patient_id: str = "UNKNOWN"
    ):

        try:
            initial_state = {

                "patient_id": patient_id,

                "patient_text": patient_text,

                "medicines": medicines,

                "completed_steps": []
            }

            result = self.app.invoke(
                initial_state
            )

            logger.info(
                "Workflow execution completed"
            )

            return result

        except Exception as e:

            logger.error(
                f"Workflow Execution Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }