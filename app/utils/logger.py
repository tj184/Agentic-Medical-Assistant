import os

from loguru import logger

from app.config.settings import settings


# Create logs directory
os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    settings.LOG_FILE,
    rotation="10 MB",
    retention="10 days",
    level=settings.LOG_LEVEL,
    enqueue=True,
    backtrace=True,
    diagnose=True
)

logger.add(
    lambda msg: print(msg, end=""),
    level=settings.LOG_LEVEL
)

logger.info("Logger initialized")