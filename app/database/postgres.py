from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from loguru import logger


DATABASE_URL = (
    "postgresql://postgres:password@localhost:5432/medical_ai"
)

try:

    engine = create_engine(
        DATABASE_URL,
        echo=False
    )

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    Base = declarative_base()

    logger.info("PostgreSQL connection initialized")

except Exception as e:

    logger.error(f"Database Connection Error: {e}")