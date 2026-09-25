"""Chat routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from src.models.dto.chat import ChatRequest, ChatResponse, RetrievalType
from src.models.user import User
from src.routes.auth import get_current_user

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
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
