from src.services.prompt_handler import PromptHandler
from src.services.retriever import Retriever
from src.utils.constants import Role
from src.services.semantic_router import SemanticRouter
from src.services.llm_chat import LLMChat


class MediBot:
    def __init__(
        self,
        chat_bot: LLMChat,
        semantic_router: SemanticRouter,
        retriever: Retriever,
        prompt_handler: PromptHandler,
    ):
        self.chat_bot = chat_bot
        self.semantic_router = semantic_router
        self.retriever = retriever
        self.prompt_handler = prompt_handler

    def ask_bot(
        self,
        query: str,
        thread_id: str,
        role: Role,
    ) -> str:
        route = self.semantic_router.get_route(query, role)

        context = self.retriever.query(
            query=query,
            category=route,
            role=role,
        )

        prompt = self.prompt_handler.get_prompt(
            query=query,
            context=context,
            category=route,
        )

        return self.chat_bot.chat(
            prompt,
            thread_id,
        )
