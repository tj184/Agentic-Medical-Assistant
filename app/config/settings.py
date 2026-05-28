from pydantic_settings import BaseSettings

from loguru import logger


class Settings(BaseSettings):

    # -------------------------
    # APP
    # -------------------------

    APP_NAME: str = "Medical AI Assistant"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    # -------------------------
    # API
    # -------------------------

    API_HOST: str = "0.0.0.0"

    API_PORT: int = 8000

    # -------------------------
    # DATABASE
    # -------------------------

    DATABASE_URL: str = "sqlite:///medical_ai.db"

    # -------------------------
    # REDIS
    # -------------------------

    REDIS_HOST: str = "localhost"

    REDIS_PORT: int = 6379

    REDIS_DB: int = 0

    # -------------------------
    # JWT
    # -------------------------

    SECRET_KEY: str = "SUPER_SECRET_KEY"

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_HOURS: int = 24

    # -------------------------
    # OLLAMA
    # -------------------------

    OLLAMA_MODEL: str = "gemma4:e2b"

    OLLAMA_BASE_URL: str = (
        "http://localhost:11434"
    )

    # -------------------------
    # EMBEDDINGS
    # -------------------------

    EMBEDDING_MODEL: str = (
        "BAAI/bge-large-en"
    )

    RERANKER_MODEL: str = (
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    # -------------------------
    # VECTOR DATABASE
    # -------------------------

    CHROMA_DB_PATH: str = (
        "data/vector_store"
    )

    CHROMA_COLLECTION: str = (
        "medical_knowledge"
    )

    # -------------------------
    # WHISPER
    # -------------------------

    WHISPER_MODEL: str = "base"

    # -------------------------
    # OCR
    # -------------------------

    OCR_LANGUAGE: str = "en"

    # -------------------------
    # LOGGING
    # -------------------------

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "logs/app.log"

    # -------------------------
    # ENV FILE
    # -------------------------

    class Config:

        env_file = ".env"

        case_sensitive = True


settings = Settings()

logger.info("Application settings loaded")