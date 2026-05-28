from pydantic import BaseModel

from typing import Optional
from datetime import datetime


# -------------------------
# Patient Schemas
# -------------------------

class PatientBase(BaseModel):

    name: str
    age: int
    gender: str
    allergies: Optional[str] = None
    medical_history: Optional[str] = None


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# -------------------------
# Session Schemas
# -------------------------

class SessionBase(BaseModel):

    patient_id: int
    conversation: str
    diagnosis: str


class SessionCreate(SessionBase):
    pass


class SessionResponse(SessionBase):

    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# -------------------------
# Prescription Schemas
# -------------------------

class PrescriptionBase(BaseModel):

    patient_id: int
    medicine: str
    dosage: str
    warnings: Optional[str] = None


class PrescriptionCreate(PrescriptionBase):
    pass


class PrescriptionResponse(PrescriptionBase):

    id: int
    created_at: datetime

    class Config:
        from_attributes = True