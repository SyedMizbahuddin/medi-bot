from enum import Enum


class Role(str, Enum):
    ADMIN = "admin"
    DOCTOR = "doctor"
    NURSE = "nurse"
    BILLING_EXECUTIVE = "billing_executive"
    TECHNICIAN = "technician"


class SourceCollection(str, Enum):
    GENERAL = "general"
    CLINICAL = "clinical"
    NURSING = "nursing"
    BILLING = "billing"
    EQUIPMENT = "equipment"


ROLE_COLLECTIONS: dict[Role, set[SourceCollection]] = {
    Role.ADMIN: {
        SourceCollection.GENERAL,
        SourceCollection.CLINICAL,
        SourceCollection.NURSING,
        SourceCollection.BILLING,
        SourceCollection.EQUIPMENT,
    },
    Role.DOCTOR: {
        SourceCollection.GENERAL,
        SourceCollection.CLINICAL,
        SourceCollection.NURSING,
    },
    Role.NURSE: {
        SourceCollection.GENERAL,
        SourceCollection.NURSING,
    },
    Role.BILLING_EXECUTIVE: {
        SourceCollection.BILLING,
        SourceCollection.GENERAL,
    },
    Role.TECHNICIAN: {
        SourceCollection.EQUIPMENT,
        SourceCollection.GENERAL,
    },
}


def can_access(role: Role, collection: SourceCollection) -> bool:
    return collection in ROLE_COLLECTIONS.get(role, set())


def accessible_collections(role: Role) -> list[str]:
    return [c.value for c in ROLE_COLLECTIONS.get(role, set())]



def accessible_roles(collection: SourceCollection) -> list[str]:
    return [
        role.value
        for role, collections in ROLE_COLLECTIONS.items()
        if collection in collections
    ]