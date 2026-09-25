"""Authentication request and response models."""

from pydantic import BaseModel, Field

from src.utils.constants import Role


class LoginRequest(BaseModel):
    """Credentials submitted by a user."""

    user_name: str = Field(min_length=1)
    password: str = Field(min_length=1)


class LoginResponse(BaseModel):
    """JWT access token and authenticated user roles."""

    access_token: str
    token_type: str = "bearer"
    user_name: str
    roles: list[Role]
