from pathlib import Path

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Object, Singleton

from src.services.auth_service import AuthService
from src.services.doc_process.docling_chunk import DoclingProcessor
from src.services.embedder import Embedder
from src.services.ingestion_pipeline import IngestionPipeline
from src.services.store.file_store import FileStore
from src.services.sqlite_db import SQLiteDB
from src.services.user_service import UserService
from src.services.vector_db import VectorDB


db_path = Path.cwd().parent / "sql_db" / "users.sqlite3"


class AppContainer(DeclarativeContainer):
    """Provide application services through dependency injection."""

    database_path = Object(db_path)
    sqlite_db = Singleton(SQLiteDB, db_path=database_path)
    user_service = Singleton(UserService, sqlite_db=sqlite_db)
    auth_service = Singleton(AuthService, user_service=user_service)

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
