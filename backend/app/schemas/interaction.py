from datetime import datetime

from pydantic import BaseModel


class InteractionCreate(BaseModel):
    doctor_name: str
    interaction_type: str
    interaction_date: datetime
    summary: str
    follow_up: str


class InteractionResponse(InteractionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True