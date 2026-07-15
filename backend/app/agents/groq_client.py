from functools import lru_cache

from langchain_groq import ChatGroq

from app.config.settings import settings


@lru_cache(maxsize=1)
def get_llm() -> ChatGroq:
    """Return a reusable Groq chat model instance."""

    if not settings.GROQ_API_KEY:
        raise RuntimeError("GROQ_API_KEY is not configured.")

    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        temperature=0,
    )