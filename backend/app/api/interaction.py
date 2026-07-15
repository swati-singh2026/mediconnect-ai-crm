from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
)
from app.services.interaction_service import (
    create_interaction,
    get_interactions,
    update_interaction,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"],
)


@router.post("/", response_model=InteractionResponse)
def create_new_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    return create_interaction(db, interaction)


@router.get("/", response_model=list[InteractionResponse])
def get_all_interactions(
    db: Session = Depends(get_db),
):
    return get_interactions(db)


@router.put("/{interaction_id}", response_model=InteractionResponse)
def update_existing_interaction(
    interaction_id: int,
    interaction: InteractionCreate,
    db: Session = Depends(get_db),
):
    return update_interaction(
        db,
        interaction_id,
        interaction,
    )