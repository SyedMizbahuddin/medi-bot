"""Read-only SQL agent for the MediAssist operational database."""

import logging
from typing import Any, cast

from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.language_models import BaseChatModel

from src.services.sqlite_db import SQLiteDB
from src.utils.constants import Role

logger = logging.getLogger(__name__)

_SQL_AGENT_PREFIX = """You are MediAssist's read-only SQL data analyst.

Use only the available SQLite database tables to answer the user's question.
Follow these rules:
- Generate only read-only SQL queries. Never INSERT, UPDATE, DELETE, DROP, or ALTER data.
- Inspect the table schema before writing a query.
- Use exact column names and return only the columns needed to answer the question.
- For counts, totals, averages, rankings, and date comparisons, calculate the result in SQL.
- If no rows match, clearly say that no matching records were found.
- Do not invent values or claim that a query succeeded when it did not.
- Keep the final answer concise and include the relevant numbers.
"""


class SqlAgent:
    """Answer authorized analytical questions against the MediAssist SQLite DB."""

    _ALLOWED_ROLES = {Role.ADMIN, Role.BILLING_EXECUTIVE}

    def __init__(self, sqlite_db: SQLiteDB, language_model: BaseChatModel) -> None:
        """Create a SQL agent using injected database and language-model dependencies."""
        self.sqlite_db = sqlite_db
        self.database = SQLDatabase.from_uri(self._database_uri())
        self.agent = create_sql_agent(
            llm=language_model,
            db=self.database,
            agent_type="tool-calling",
            prefix=_SQL_AGENT_PREFIX,
            top_k=10,
            max_iterations=10,
            verbose=False,
        )
        logger.info("Initialized SQL agent for %s", self.sqlite_db.db_path)

    def query(self, question: str, role: Role) -> str:
        """Execute an authorized read-only analytical question and return its answer."""
        if role not in self._ALLOWED_ROLES:
            raise PermissionError(f"Role {role.value} is not allowed to query the SQL database")

        if not question.strip():
            return "No SQL question was provided."

        logger.info("Running SQL query agent for role %s", role.value)
        result = cast(dict[str, Any], self.agent.invoke({"input": question}))
        output = result.get("output")
        if output is None:
            logger.warning("SQL agent returned no output")
            return "No result was returned from the SQL database."

        return str(output)

    def _database_uri(self) -> str:
        """Build the SQLAlchemy URI for the injected SQLite database path."""
        return f"sqlite:///{self.sqlite_db.db_path.resolve()}"
