from fastapi import FastAPI

from app.config import AI_PROVIDER, AI_MODEL
from app.routers.chat import router as chat_router


app = FastAPI(
    title="Model-Agnostic AI Chat API",
    description="A REST API for interacting with multiple AI providers.",
    version="1.0.0",
)


app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "AI Chat API is running",
        "provider": AI_PROVIDER,
        "model": AI_MODEL,
    }