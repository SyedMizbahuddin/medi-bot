"""JWT creation and validation."""

from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

from src.config.app_config import app_settings
from src.models.user import User
from src.services.user_service import UserService


class AuthService:
    """Authenticate users through UserService and manage JWTs."""

    def __init__(self, user_service: UserService) -> None:
        """Initialize JWT authentication with a user service dependency."""
        self.user_service = user_service

    def authenticate(self, user_name: str, password: str) -> User | None:
        """Authenticate credentials through UserService."""
        return self.user_service.authenticate(user_name, password)

    def create_access_token(self, user: User) -> str:
        """Create a JWT containing username, roles, issue time, and expiry."""
        issued_at = datetime.now(timezone.utc)
        payload = {
            "sub": user.user_name,
            "user_name": user.user_name,
            "roles": [role.value for role in user.roles],
            "iat": issued_at,
            "exp": issued_at + timedelta(days=app_settings.JWT_EXPIRY_DAYS),
        }
        return jwt.encode(payload, app_settings.JWT_SECRET, algorithm=app_settings.JWT_ALGORITHM)

    def decode_access_token(self, token: str) -> dict[str, Any]:
        """Validate and decode a JWT access token."""
        return jwt.decode(token, app_settings.JWT_SECRET, algorithms=[app_settings.JWT_ALGORITHM])
