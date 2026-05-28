from fastapi import APIRouter

from app.agents.supervisor_agent import SupervisorAgent

from loguru import logger


router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"]
)

agent = SupervisorAgent()


@router.post("/")
async def diagnose_patient(payload: dict):

    try:
        symptoms = payload.get("symptoms", [])
        medicines = payload.get("medicines", [])

        result = agent.process_case(
            symptoms=symptoms,
            medicines=medicines
        )

        logger.info("Diagnosis completed")

        return {
            "success": True,
            "result": result
        }

    except Exception as e:

        logger.error(f"Diagnosis API Error: {e}")

        return {
            "success": False,
            "error": str(e)
        }