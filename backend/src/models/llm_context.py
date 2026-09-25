from pydantic.dataclasses import dataclass
from src.utils.constants import Role

@dataclass
class RoleContext:
    role: Role
    