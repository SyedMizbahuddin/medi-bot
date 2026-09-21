"""FastAPI application for the MediAssist backend."""

from enum import Enum

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from src.routes.auth import get_current_user, router as auth_router
from src.models.user import User
from src.utils.constants import Role, accessible_collections

app = FastAPI(title="MediAssist API", version="0.1.0")
app.include_router(auth_router)


class ChatRequest(BaseModel):
    """Question submitted to the RAG endpoint."""

    question: str = Field(min_length=1)
    role: Role


class Source(BaseModel):
    """Source citation returned with an answer."""

    source_document: str
    section_title: str | None = None
    collection: str


class RetrievalType(str, Enum):
    """Supported retrieval strategies."""

    HYBRID_RAG = "hybrid_rag"
    SQL_RAG = "sql_rag"


class ChatResponse(BaseModel):
    """Response shape for the chat endpoint."""

    answer: str
    sources: list[Source]
    retrieval_type: RetrievalType
    role: Role


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, current_user: User = Depends(get_current_user)) -> ChatResponse:
    """Return the chat response shape; RAG routing is not implemented yet."""
    if request.role not in current_user.roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The requested role is not assigned to this user",
        )
    return ChatResponse(
        answer="Chat retrieval is not implemented yet.",
        sources=[],
        retrieval_type=RetrievalType.HYBRID_RAG,
        role=request.role,
    )


@app.get("/collections/{role}", response_model=list[str])
def collections(role: Role) -> list[str]:
    """Return collections accessible to the requested role."""
    return accessible_collections(role)


@app.get("/health")
def health() -> dict[str, str]:
    """Return the API health status."""
    return {"status": "ok"}
