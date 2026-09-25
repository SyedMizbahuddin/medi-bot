from pathlib import Path

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Object, Singleton

from src.services.auth_service import AuthService
from src.services.doc_process.docling_chunk import DoclingProcessor
from src.services.embedder import Embedder
from src.services.ingestion_pipeline import IngestionPipeline
from src.services.llm_chat import LLMChat
from src.services.medi_bot import MediBot
from src.services.prompt_handler import PromptHandler
from src.services.retriever import Retriever
from src.services.semantic_router import SemanticRouter
from src.services.sql_rag_agent import SqlRAG
from src.services.store.file_store import FileStore
from src.services.sqlite_db import SQLiteDB
from src.services.user_service import UserService
from src.services.vector_db import VectorDB


db_path = Path.cwd().parent / "sql_db" / "users.sqlite3"
sql_database_path = Path.cwd().parent / "mediassist_data" / "db" / "mediassist.db"


class AppContainer(DeclarativeContainer):
    """Provide application services through dependency injection."""

    database_path = Object(db_path)
    sqlite_db = Singleton(SQLiteDB, db_path=database_path)
    user_service = Singleton(UserService, sqlite_db=sqlite_db)
    auth_service = Singleton(AuthService, user_service=user_service)

    sql_database_path = Object(sql_database_path)
    sql_db = Singleton(SQLiteDB, db_path=sql_database_path)
    sql_rag = Singleton(SqlRAG)

    file_store = Singleton(FileStore)
    embedder = Singleton(Embedder, store=file_store)
    docling_proccesor = Singleton(DoclingProcessor, store=file_store)
    vector_db = Singleton(VectorDB, embedder=embedder)
    ingestion_pipeline = Singleton(
        IngestionPipeline,
        document_processor=docling_proccesor,
        embedder=embedder,
        vector_db=vector_db,
    )

    llm_chat = Singleton(LLMChat, sql_db=sql_db)
    semantic_router = Singleton(SemanticRouter)
    prompt_handler = Singleton(PromptHandler)
    retriever = Singleton(
        Retriever,
        vector_db=vector_db,
        sql_db=sql_db,
        sql_rag=sql_rag,
    )
    medi_bot = Singleton(
        MediBot,
        chat_bot=llm_chat,
        semantic_router=semantic_router,
        retriever=retriever,
        prompt_handler=prompt_handler,
    )
