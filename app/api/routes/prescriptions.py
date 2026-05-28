from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.postgres import SessionLocal

from app.database.schemas import PrescriptionCreate

from app.database.crud import (
    create_prescription,
    get_patient_prescriptions
)

from loguru import logger


router = APIRouter(
    prefix="/prescriptions",
    tags=["Prescriptions"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
async def add_prescription(
    prescription: PrescriptionCreate,
    db: Session = Depends(get_db)
):

    try:
        result = create_prescription(
            db,
            prescription
        )

        logger.info("Prescription added")

        return {
            "success": True,
            "prescription": result
        }

    except Exception as e:

        logger.error(f"Prescription Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }


@router.get("/{patient_id}")
async def fetch_prescriptions(
    patient_id: int,
    db: Session = Depends(get_db)
):

    try:
        prescriptions = get_patient_prescriptions(
            db,
            patient_id
        )

        return {
            "success": True,
            "prescriptions": prescriptions
        }

    except Exception as e:

        logger.error(
            f"Fetch Prescriptions Error: {e}"
        )

        return {
            "success": False,
            "error": str(e)
        }