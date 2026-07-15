from fastapi import APIRouter, Depends, HTTPException

from app.schemas.ai import AISummaryRequest, AISummaryResponse
from app.services.ai_service import AIService


router = APIRouter(prefix="/ai", tags=["AI"])


def get_ai_service() -> AIService:
    return AIService()


@router.post("/summary", response_model=AISummaryResponse)
def generate_summary(
    request: AISummaryRequest,
    ai_service: AIService = Depends(get_ai_service),
) -> AISummaryResponse:
    try:
        summary = ai_service.generate_summary(
            doctor_name=request.doctor_name,
            interaction_type=request.interaction_type,
            interaction_date=str(request.interaction_date),
            summary=request.summary,
            follow_up=request.follow_up,
        )

        return AISummaryResponse(summary=summary)

    except Exception as exc:
        import traceback

    traceback.print_exc()  # Print full error in terminal

    raise HTTPException(
        status_code=500,
        detail=str(exc),  # Return actual error in Swagger
    )