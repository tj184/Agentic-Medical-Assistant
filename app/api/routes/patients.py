from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.postgres import SessionLocal
from app.database.schemas import PatientCreate
from app.database.crud import (
    create_patient,
    get_patient,
    get_all_patients
)

from loguru import logger


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
async def add_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    try:
        result = create_patient(db, patient)

        logger.info("Patient added")

        return {
            "success": True,
            "patient": result
        }

    except Exception as e:

        logger.error(f"Add Patient Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }


@router.get("/{patient_id}")
async def fetch_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    try:
        patient = get_patient(db, patient_id)

        return {
            "success": True,
            "patient": patient
        }

    except Exception as e:

        logger.error(f"Fetch Patient Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }


@router.get("/")
async def fetch_all_patients(
    db: Session = Depends(get_db)
):

    try:
        patients = get_all_patients(db)

        return {
            "success": True,
            "patients": patients
        }

    except Exception as e:

        logger.error(f"Fetch All Patients Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }