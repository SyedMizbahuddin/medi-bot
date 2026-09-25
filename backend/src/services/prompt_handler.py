from src.utils.constants import RouteCategory
from langchain_core.documents import Document
from typing import Any
from langchain_core.prompts import PromptTemplate


class PromptHandler:
    def __init__(self):
        self._sql_prompt_template: PromptTemplate = PromptTemplate.from_template("this is sql prompt")
        self._vector_prompt_template: PromptTemplate = PromptTemplate.from_template("this is vector prompt")
        self._continuation_template: PromptTemplate = PromptTemplate.from_template("this is continuation prompt")

    def sql_prompt(self, query: str, context: Any) -> str:
        return self._sql_prompt_template.invoke({"query": query, "context": context}).to_string()

    def vector_db_prompt(self, query: str, context: list[Document]) -> str:
        return self._vector_prompt_template.invoke({"query": query, "context": context}).to_string()

    def continuation_prompt(self, query: str, context: Any) -> str:
        return self._continuation_template.invoke({"query": query, "context": context}).to_string()

    def get_prompt(
        self,
        query: str,
        context: Any,
        category: RouteCategory,
    ) -> str:
        handler = {
            RouteCategory.SQL: self.sql_prompt,
            RouteCategory.VECTOR_DB: self.vector_db_prompt,
            RouteCategory.FOLLOW_UP: self.continuation_prompt,
        }.get(category)

        if handler is None:
            raise ValueError(f"Unsupported route category: {category}")

        return handler(query, context)
