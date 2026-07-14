from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # For type checkers / linters, import the real FastAPI
    from fastapi import FastAPI  # type: ignore[import]
else:
    try:
        from fastapi import FastAPI
    except Exception:
        # Provide a minimal runtime stub so editors/linters don't complain when
        # FastAPI isn't available. Installing FastAPI is still required to
        # actually run the application: pip install fastapi uvicorn
        class FastAPI:  # pragma: no cover - stub for dev environment
            def __init__(self, *args, **kwargs):
                pass

            def get(self, *args, **kwargs):
                def decorator(f):
                    return f
                return decorator

app = FastAPI(
    title="MediConnect AI CRM",
    version="1.0.0",
    description="AI-First CRM for Healthcare Professionals"
)

@app.get("/")
def home():
    return {
        "message": "MediConnect AI CRM Backend Running 🚀"
    }