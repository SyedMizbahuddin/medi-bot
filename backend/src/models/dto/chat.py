"""Chat request and response models."""

from enum import Enum

from pydantic import BaseModel, Field

from src.utils.constants import Role


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
