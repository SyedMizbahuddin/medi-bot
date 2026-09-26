"""FastAPI application for the MediAssist backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import routes
from src.config.container import AppContainer
from src.middleware.jwt_middleware import JWTMiddleware

container = AppContainer()
container.wire(packages=[routes])

app = FastAPI(title="MediAssist API", version="0.1.0")
app.add_middleware(JWTMiddleware, auth_service=container.auth_service())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(routes.router)


@app.get("/health")
def health() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}
