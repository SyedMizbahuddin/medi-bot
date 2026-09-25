from uuid import NAMESPACE_URL, uuid5

def get_point_id(source_document: str, ind: int) -> str:
    """Create a deterministic point ID for a document chunk."""
    return str(
        uuid5(
            NAMESPACE_URL,
            f"{source_document}_{ind}",
        )
    )