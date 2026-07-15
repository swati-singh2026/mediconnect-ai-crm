from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.models import Interaction
from app.schemas.interaction import InteractionCreate


def create_interaction(db: Session, interaction: InteractionCreate):
    db_interaction = Interaction(
        doctor_name=interaction.doctor_name,
        interaction_type=interaction.interaction_type,
        interaction_date=interaction.interaction_date,
        summary=interaction.summary,
        follow_up=interaction.follow_up,
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_interactions(db: Session):
    return db.query(Interaction).all()


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction: InteractionCreate,
):
    db_interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if db_interaction is None:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found",
        )

    db_interaction.doctor_name = interaction.doctor_name
    db_interaction.interaction_type = interaction.interaction_type
    db_interaction.interaction_date = interaction.interaction_date
    db_interaction.summary = interaction.summary
    db_interaction.follow_up = interaction.follow_up

    db.commit()
    db.refresh(db_interaction)

    return db_interaction