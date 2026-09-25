from typing import Any
from src.services.sql_rag_agent import SqlRAG
from src.utils.constants import Role, RouteCategory
from langchain_core.documents import Document
from src.services.sqlite_db import SQLiteDB
from src.services.vector_db import VectorDB


class Retriever:
    def __init__(
        self,
        vector_db: VectorDB,
        sql_db: SQLiteDB,
        sql_rag: SqlRAG,
    ):
        self.vector_db = vector_db
        self.sql_db = sql_db
        self.sql_rag = sql_rag

    def query_vector_db(
        self,
        query: str,
        role: Role,
    ) -> list[Document]:
        return []

    def _cross_rank(
        self,
        retrieved_docs: list[Document],
    ): ...

    def query_sql_db(self, query: str, role: Role) -> Any: ...

    def query_follow_up(
        self,
        query: str,
        role: Role,
    ) -> str:
        return query

    def query(
        self,
        query: str,
        category: RouteCategory,
        role: Role,
    ) -> Any:
        handlers = {
            RouteCategory.VECTOR_DB: self.query_vector_db,
            RouteCategory.SQL: self.query_sql_db,
            RouteCategory.FOLLOW_UP: self.query_follow_up,
        }

        try:
            handler = handlers[category]
        except KeyError:
            raise ValueError(f"Unsupported route category: {category}") from None

        return handler(query, role)
