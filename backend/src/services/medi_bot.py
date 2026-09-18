from src.utils.constants import Role
from src.services.semantic_router import SemanticRouter
from src.services.llm_chat import LLMChat


class MediBot:
    
    def __init__(self, chat_bot : LLMChat, semantic_router: SemanticRouter):
        self.chat_bot = chat_bot
        self.semantic_router = semantic_router 
    
    def ask_bot(self, query: str, query_id: str, role: Role):
        ok=1
        pass