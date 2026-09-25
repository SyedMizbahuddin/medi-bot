"""Chat routes."""

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException, status

from src.config.container import AppContainer
from src.models.dto.chat import ChatRequest, ChatResponse
from src.models.user import User
from src.routes.auth import get_current_user
from src.services.api.chat_service import ChatService

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
@inject
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user),
    chat_service: ChatService = Depends(Provide[AppContainer.chat_service]),
) -> ChatResponse:
    """Ask MediBot after validating the requested role."""
    if request.role not in current_user.roles:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The requested role is not assigned to this user",
        )

    return chat_service.chat(request=request, user=current_user)
