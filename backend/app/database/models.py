from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.database.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(100), nullable=False)

    interaction_type = Column(String(50), nullable=False)

    interaction_date = Column(DateTime, nullable=False)

    summary = Column(Text, nullable=True)

    follow_up = Column(String(255), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)