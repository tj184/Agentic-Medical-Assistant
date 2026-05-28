from fastapi import FastAPI

from app.api.routes.diagnosis import router as diagnosis_router
from app.api.routes.patients import router as patients_router
from app.api.routes.prescriptions import router as prescriptions_router
from app.api.routes.auth import router as auth_router

from app.api.middleware.logging_middleware import LoggingMiddleware
from app.api.middleware.auth_middleware import AuthMiddleware

from loguru import logger


app = FastAPI(
    title="Medical AI Assistant",
    version="1.0.0"
)

# Middleware
app.add_middleware(LoggingMiddleware)
app.add_middleware(AuthMiddleware)

# Routes
app.include_router(auth_router)
app.include_router(diagnosis_router)
app.include_router(patients_router)
app.include_router(prescriptions_router)


@app.get("/")
async def root():

    logger.info("Root endpoint accessed")

    return {
        "message": "Medical AI Assistant API Running"
    }