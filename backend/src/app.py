"""FastAPI application for the MediAssist backend."""

from fastapi import FastAPI

from src.routes.auth import router as auth_router
from src.routes.chat import router as chat_router

app = FastAPI(title="MediAssist API", version="0.1.0")
app.include_router(auth_router)
app.include_router(chat_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}
