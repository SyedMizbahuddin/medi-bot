from typing import Any

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

from src.helpers.prompt_templates import (
    CONTINUATION_PROMPT,
    SQL_PROMPT,
    VECTOR_DB_PROMPT,
)
from src.utils.constants import RouteCategory


class PromptHandler:
    """Build prompts for each supported RAG route."""

    def __init__(self) -> None:
        """Initialize the route-specific prompt templates."""
        self._sql_prompt_template = PromptTemplate.from_template(SQL_PROMPT)
        self._vector_prompt_template = PromptTemplate.from_template(VECTOR_DB_PROMPT)
        self._continuation_template = PromptTemplate.from_template(CONTINUATION_PROMPT)

    def sql_prompt(self, query: str, context: Any) -> str:
        """Create a prompt for an analytical SQL-RAG response."""
        return self._sql_prompt_template.invoke({"query": query, "context": context}).to_string()

    def vector_db_prompt(self, query: str, context: list[Document]) -> str:
        """Create a prompt containing each retrieved document and its metadata."""
        context_blocks = []
        for index, document in enumerate(context[:4], start=1): # max 4
            metadata = document.metadata
            source_document = metadata.get("source_document", "Unknown document")
            section_title = metadata.get("section_title")
            if section_title is None:
                section_titles = metadata.get("section_titles", [])
                section_title = "; ".join(str(title) for title in section_titles if title)
            indices = metadata.get("index")
            if indices is None:
                indices = metadata.get('indices',[])
                indices = ','.join(str(ind) for ind in indices)

            collection = metadata.get("collection", "Unknown collection")
            context_blocks.append(
                "\n".join(
                    [
                        f"[Context {index}]",
                        f"Source document: {source_document}",
                        f"Section: {section_title or 'Unknown section'}",
                        f"chunk_indices: {indices or 'Unknown chunk indices'}",
                        f"Collection: {collection}",
                        f"Content:\n{document.page_content}",
                    ]
                )
            )

        formatted_context = "\n\n".join(context_blocks) or "No retrieved context was found."
        return self._vector_prompt_template.invoke(
            {"query": query, "context": formatted_context}
        ).to_string()

    def continuation_prompt(self, query: str, context: Any) -> str:
        """Create a prompt for a follow-up question."""
        return self._continuation_template.invoke({"query": query, "context": context}).to_string()

    def get_prompt(
        self,
        query: str,
        context: Any,
        category: RouteCategory,
    ) -> str:
        """Build a prompt using the handler for the selected route."""
        handler = {
            RouteCategory.SQL: self.sql_prompt,
            RouteCategory.VECTOR_DB: self.vector_db_prompt,
            RouteCategory.FOLLOW_UP: self.continuation_prompt,
        }.get(category)

        if handler is None:
            raise ValueError(f"Unsupported route category: {category}")

        return handler(query, context)
