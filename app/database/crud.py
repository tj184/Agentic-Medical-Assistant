from sqlalchemy.orm import Session

from loguru import logger

from app.database.models import (
    Patient,
    Session as MedicalSession,
    Prescription
)

from app.database.schemas import (
    PatientCreate,
    SessionCreate,
    PrescriptionCreate
)


# -------------------------
# PATIENT CRUD
# -------------------------

def create_patient(
    db: Session,
    patient: PatientCreate
):

    try:
        db_patient = Patient(
            name=patient.name,
            age=patient.age,
            gender=patient.gender,
            allergies=patient.allergies,
            medical_history=patient.medical_history
        )

        db.add(db_patient)

        db.commit()

        db.refresh(db_patient)

        logger.info(
            f"Patient created: {db_patient.id}"
        )

        return db_patient

    except Exception as e:

        logger.error(f"Create Patient Error: {e}")

        db.rollback()

        return None


def get_patient(
    db: Session,
    patient_id: int
):

    try:
        patient = db.query(Patient).filter(
            Patient.id == patient_id
        ).first()

        return patient

    except Exception as e:

        logger.error(f"Get Patient Error: {e}")

        return None


def get_all_patients(db: Session):

    try:
        patients = db.query(Patient).all()

        return patients

    except Exception as e:

        logger.error(f"Get All Patients Error: {e}")

        return []


# -------------------------
# SESSION CRUD
# -------------------------

def create_session(
    db: Session,
    session_data: SessionCreate
):

    try:
        db_session = MedicalSession(
            patient_id=session_data.patient_id,
            conversation=session_data.conversation,
            diagnosis=session_data.diagnosis
        )

        db.add(db_session)

        db.commit()

        db.refresh(db_session)

        logger.info(
            f"Session created: {db_session.id}"
        )

        return db_session

    except Exception as e:

        logger.error(f"Create Session Error: {e}")

        db.rollback()

        return None


def get_patient_sessions(
    db: Session,
    patient_id: int
):

    try:
        sessions = db.query(MedicalSession).filter(
            MedicalSession.patient_id == patient_id
        ).all()

        return sessions

    except Exception as e:

        logger.error(f"Get Sessions Error: {e}")

        return []


# -------------------------
# PRESCRIPTION CRUD
# -------------------------

def create_prescription(
    db: Session,
    prescription: PrescriptionCreate
):

    try:
        db_prescription = Prescription(
            patient_id=prescription.patient_id,
            medicine=prescription.medicine,
            dosage=prescription.dosage,
            warnings=prescription.warnings
        )

        db.add(db_prescription)

        db.commit()

        db.refresh(db_prescription)

        logger.info(
            f"Prescription created: {db_prescription.id}"
        )

        return db_prescription

    except Exception as e:

        logger.error(f"Create Prescription Error: {e}")

        db.rollback()

        return None


def get_patient_prescriptions(
    db: Session,
    patient_id: int
):

    try:
        prescriptions = db.query(Prescription).filter(
            Prescription.patient_id == patient_id
        ).all()

        return prescriptions

    except Exception as e:

        logger.error(
            f"Get Prescriptions Error: {e}"
        )

        return []