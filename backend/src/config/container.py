from src.services.auth_service import AuthService
from src.services.ingestion_pipeline import IngestionPipeline
from src.services.vector_db import VectorDB
from src.services.doc_process.docling_chunk import DoclingProcessor
from src.services.embedder import Embedder
from src.services.store.file_store import FileStore
from dependency_injector.providers import Singleton
from dependency_injector.containers import DeclarativeContainer


class Appcontainer(DeclarativeContainer):
    auth_service = Singleton(AuthService)
    file_store = Singleton(FileStore)
    embedder = Singleton(Embedder, store=file_store)
    docling_proccesor = Singleton(DoclingProcessor, store=file_store)
    vector_db = Singleton(VectorDB, embedder=embedder)
    ingestion_pipeline = Singleton(IngestionPipeline,
                                   document_processor=docling_proccesor,
                                   embedder=embedder, 
                                   vector_db=vector_db)
    