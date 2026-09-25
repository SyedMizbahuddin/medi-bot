from src.config.app_config import app_settings
from typing import Any
from src.services.sql_rag_agent import SqlRAG
from src.utils.constants import Role, RouteCategory
from langchain_core.documents import Document
from src.services.sqlite_db import SQLiteDB
from src.services.vector_db import VectorDB
from fastembed.rerank.cross_encoder import TextCrossEncoder

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
        self.reranker: TextCrossEncoder = TextCrossEncoder(model_name=app_settings.CROSS_ENCODER_MODEL)

    def query_vector_db(
        self,
        query: str,
        role: Role,
    ) -> list[Document]:
        docs = self.vector_db.retrieve(input=query, role=role)
        docs = self.vector_db.add_surroundings(docs)
        docs = self._cross_rank(query, docs)
        return docs

    def _cross_rank(
        self,
        query: str,
        retrieved_docs: list[Document],
    ): 
        content_hits = [doc.page_content for doc in retrieved_docs]
        new_scores = list(
            self.reranker.rerank(query, content_hits)
        )  # returns scores between query and each document

        ranking = [
            (i, score) for i, score in enumerate(new_scores)
        ]  # saving document indices
        ranking.sort(
            key=lambda x: x[1], reverse=True
        )  # sorting them in order of relevance defined by reranker

        new_docs_ordered = []
        for rank, score in ranking:
            doc = retrieved_docs[rank]
            doc.metadata['_cross_score'] = score
            new_docs_ordered.append(doc)
        
        return new_docs_ordered

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
