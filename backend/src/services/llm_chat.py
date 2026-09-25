from src.services.sqlite_db import SQLiteDB


class LLMChat:
    def __init__(self, sql_db: SQLiteDB):
        self.sql_db = sql_db

    def chat(self, prompt: str, thread_id: str) -> str:
        return ""
