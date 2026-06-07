from fastapi import FastAPI
from app.api.routes import api_router
from app.core.logger import setup_logging
from app.core.config import settings

app = FastAPI(
    title="Titan AI Backend",
    description="Modular AI backend for the Titan AI desktop agent.",
    version="0.1.0",
)

setup_logging()
app.include_router(api_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "titan-ai-backend", "environment": settings.environment}
