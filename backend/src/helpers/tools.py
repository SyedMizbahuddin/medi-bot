from src.models.llm_context import RoleContext
from langchain.tools import ToolRuntime, tool
from typing import Any



@tool
def get_chunk_of_a_document_by_index(
    source_document: str,
    index: int,
    runtime: ToolRuntime[RoleContext],
) -> dict[str, Any]:
    """Retrieve one document chunk when the caller has collection access.

    Use this tool when a retrieved chunk is relevant to the user's question
    but does not contain enough information to answer confidently. Query the
    neighbouring chunks from the same document, such as ``index - 1`` or
    ``index + 1``, to obtain the missing surrounding context. The chunk is
    looked up by its source filename and zero-based index, and the user's role
    from the runtime context is applied to the access check.

    Args:
        source_document: Exact source filename stored in the vector database.
        index: Zero-based index of the chunk within the source document.
        runtime: Runtime context containing the authenticated user's role.

    Returns:
        A dictionary containing the retrieved chunk payload with these fields:

        - ``content``: Text content of the requested chunk.
        - ``source_document``: Source filename containing the chunk.
        - ``index``: Zero-based chunk index within the source document.
        - ``collection``: Document collection containing the source.
        - ``section_title``: Section heading associated with the chunk.

        If the chunk does not exist or is not accessible for the user's role,
        returns ``{"error": "No chunk found with <source_document> and <index>"}``.
    """
    from src.config.container import AppContainer
    container = AppContainer()
    point = container.vector_db().retrieve_chunk(source_document, index, runtime.context.role)
    if point is None:
        return {'error': f'No chunk found with {source_document} and {index}'}
    
    payload = point.payload or {}
    return payload
