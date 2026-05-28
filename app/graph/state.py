from typing import TypedDict
from typing import List
from typing import Dict
from typing import Optional


class MedicalState(TypedDict, total=False):

    # -------------------------
    # INPUT DATA
    # -------------------------

    patient_id: str

    patient_text: str

    medicines: List[str]

    symptoms: List[str]

    # -------------------------
    # RAG DATA
    # -------------------------

    retrieved_documents: List[str]

    # -------------------------
    # ANALYSIS
    # -------------------------

    emergency_detected: bool

    emergency_details: Dict

    drug_analysis: Dict

    diagnosis: Dict

    report: str

    # -------------------------
    # WORKFLOW
    # -------------------------

    current_step: str

    completed_steps: List[str]

    error: Optional[str]