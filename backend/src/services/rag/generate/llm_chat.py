from src.helpers.tools import get_chunk_of_a_document_by_index
from src.utils.constants import Role
from src.models.llm_context import RoleContext
from langchain.messages import HumanMessage
from sqlite3 import Connection
from src.helpers.llm import llm
from src.helpers.prompt_templates import SYSTEM_PROMPT
from langchain.agents import create_agent
from src.services.sqlite_db import SQLiteDB
from langgraph.checkpoint.sqlite import SqliteSaver

class LLMChat:
    """Generate responses using the configured LangChain agent."""

    def __init__(self, sql_db: SQLiteDB):
        """Initialize the chat agent with the persistent system prompt."""
        self.sql_db = sql_db
        connection: Connection = self.sql_db.connect()
        checkpointer = SqliteSaver(connection)
        self.agent = create_agent(
            model=llm,
            system_prompt=SYSTEM_PROMPT,
            checkpointer=checkpointer,
            context_schema=RoleContext,
            tools=[get_chunk_of_a_document_by_index]
        )

    def chat(self, prompt: str, thread_id: str, role: Role) -> str:
        """Generate a response for a formatted route-specific prompt."""
        config = {"configurable": {"thread_id": thread_id}}

        response = self.agent.invoke(
            input={"messages": [HumanMessage(content=prompt)]},
            config=config, #type:ignore
            context=RoleContext(role=role),
            
        )
        
        print(response)
        return response["messages"][-1].content
