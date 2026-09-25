"""Application service for chat requests."""

from langchain_core.documents import Document

from src.models.dto.chat import ChatRequest, ChatResponse, RetrievalType, Source
from src.models.user import User
from src.services.rag.generate.medi_bot import MediBot, MediBotResult
from src.utils.constants import RouteCategory


class ChatService:
    """Coordinate chat requests with the MediBot RAG service."""

    def __init__(self, medi_bot: MediBot) -> None:
        """Initialize the chat service with the MediBot dependency."""
        self.medi_bot = medi_bot

    def chat(self, request: ChatRequest, user: User) -> ChatResponse:
        """Ask MediBot a question and format the API response."""
        result = self.medi_bot.ask_bot(
            query=request.question,
            thread_id=user.user_name,
            role=request.role,
        )

        return ChatResponse(
            answer=result.answer,
            sources=self._format_sources(result),
            retrieval_type=self._retrieval_type(result.category),
            role=request.role,
        )

    @staticmethod
    def _format_sources(result: MediBotResult) -> list[Source]:
        """Convert retrieved vector documents into API source citations."""
        if not isinstance(result.context, list):
            return []

        sources = []
        for document in result.context:
            if not isinstance(document, Document):
                continue

            metadata = document.metadata
            section_title = metadata.get("section_title")
            section_titles = metadata.get("section_titles")
            if section_title is None and isinstance(section_titles, list):
                section_title = "; ".join(str(title) for title in section_titles if title)

            sources.append(
                Source(
                    source_document=str(metadata.get("source_document", "")),
                    section_title=section_title,
                    collection=str(metadata.get("collection", "")),
                )
            )

        return sources

    @staticmethod
    def _retrieval_type(category: RouteCategory) -> RetrievalType:
        """Map the internal RAG route to the public response type."""
        if category is RouteCategory.SQL:
            return RetrievalType.SQL_RAG
        return RetrievalType.HYBRID_RAG
