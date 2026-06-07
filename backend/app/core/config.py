import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "development")
    gemini_api_key: str | None = None
    gemini_model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-lite")
    gemini_fallback_model: str = os.getenv("GEMINI_FALLBACK_MODEL", "gemini-1.5")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./titan_memory.db")
    max_retry_attempts: int = 3
    request_timeout_seconds: int = 60

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
