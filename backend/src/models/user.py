"""User models used by authentication."""

from pydantic import BaseModel, Field

from src.utils.constants import Role


class User(BaseModel):
    """Application user with credentials and assigned roles."""

    user_name: str = Field(min_length=1)
    password: str = ""
    roles: list[Role]
