"""FastAPI application for the MediAssist backend."""

from fastapi import FastAPI

from src import routes
from src.config.container import AppContainer

container = AppContainer()
container.wire(packages=[routes])

app = FastAPI(title="MediAssist API", version="0.1.0")
app.include_router(routes.router)


@app.get("/health")
def health() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}
