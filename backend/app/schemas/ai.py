from datetime import datetime

from pydantic import BaseModel


class AISummaryRequest(BaseModel):
    doctor_name: str
    interaction_type: str
    interaction_date: datetime
    summary: str
    follow_up: str


class AISummaryResponse(BaseModel):
    summary: str
