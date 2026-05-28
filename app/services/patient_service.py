from loguru import logger

from sqlalchemy.orm import Session

from app.database.crud import (
    create_patient,
    get_patient,
    get_all_patients
)

from app.database.schemas import PatientCreate


class PatientService:

    def __init__(self):
        pass

    def create_new_patient(
        self,
        db: Session,
        patient_data: dict
    ):

        try:
            patient = PatientCreate(
                **patient_data
            )

            result = create_patient(
                db,
                patient
            )

            logger.info(
                "Patient created successfully"
            )

            return {
                "success": True,
                "patient": result
            }

        except Exception as e:

            logger.error(
                f"Patient Service Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }

    def fetch_patient(
        self,
        db: Session,
        patient_id: int
    ):

        try:
            patient = get_patient(
                db,
                patient_id
            )

            return {
                "success": True,
                "patient": patient
            }

        except Exception as e:

            logger.error(
                f"Fetch Patient Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }

    def fetch_all_patients(
        self,
        db: Session
    ):

        try:
            patients = get_all_patients(db)

            return {
                "success": True,
                "patients": patients
            }

        except Exception as e:

            logger.error(
                f"Fetch All Patients Error: {e}"
            )

            return {
                "success": False,
                "error": str(e)
            }