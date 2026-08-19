from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.ai_service import AIService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        description="The message to send to the AI model.",
    )


ai_service = AIService()


@router.post("/")
def chat(request: ChatRequest):
    try:
        response = ai_service.chat(request.message)

        return {
            "response": response,
            "model": ai_service.model,
        }

    except RuntimeError as error:
        raise HTTPException(
            status_code=503,
            detail=str(error),
        )