from fastapi import FastAPI

from app.api.interaction import router as interaction_router
from app.config.settings import settings
from app.database import models
from app.database.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="AI-First CRM for Healthcare Professionals",
)

# Register API routes
app.include_router(interaction_router)


@app.get("/")
def home():
    return {
        "message": f"{settings.APP_NAME} Backend Running 🚀",
        "version": settings.APP_VERSION,
        "status": "Healthy",
    }
Base.metadata.create_all(bind=engine)