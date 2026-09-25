"""Authentication routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import jwt

from src.models.dto.auth import LoginRequest, LoginResponse
from src.models.user import User
from src.services.auth_service import AuthService
from src.utils.constants import Role, accessible_collections

router = APIRouter(tags=["auth"])
auth_service = AuthService()
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    """Validate the bearer token and return its authenticated user."""
    try:
        claims = auth_service.decode_access_token(credentials.credentials)
        return User(
            user_name=claims["user_name"],
            roles=[Role(role) for role in claims["roles"]],
        )
    except (KeyError, ValueError, jwt.InvalidTokenError) as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        ) from error


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest) -> LoginResponse:
    """Authenticate credentials and return a 365-day JWT."""
    user = auth_service.authenticate(request.user_name, request.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = auth_service.create_access_token(user)
    return LoginResponse(
        access_token=token,
        user_name=user.user_name,
        roles=user.roles,
    )


@router.get("/collections/{role}", response_model=list[str])
def collections(role: Role) -> list[str]:
    """Return collections accessible to the requested role."""
    return accessible_collections(role)
