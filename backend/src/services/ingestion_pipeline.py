from src.services.vector_db import VectorDB
from qdrant_client.http.models.models import SparseVector
import logging
from src.services.embedder import Embedder
from src.utils.constants import accessible_roles, SourceCollection
from langchain_core.documents import Document
from src.helpers.ingestion_helper import generate_file_directory
from src.services.doc_process.document_processor import DocumentProcessor
from src.models.dir_file_model import Directory
from pathlib import Path

logger = logging.getLogger(__name__)



class IngestionPipeline:
    def __init__(self, document_processor: DocumentProcessor, embedder: Embedder, vector_db: VectorDB):
        """Initialize the ingestion pipeline dependencies."""
        self.document_processor: DocumentProcessor = document_processor
        self.embedder: Embedder = embedder
        self.vector_db: VectorDB = vector_db
        self.CURRENT_DIR: Path = Path().cwd()
        self.MEDIASSIST_DATA: Path = self.CURRENT_DIR.parent / "mediassist_data"

    def chunk_document(self, file: Path, dir: Path) -> list[Document]:
        """Chunk one source document and attach access-control metadata."""
        logger.info("Chunking document %s", file.name)
        additional_metdata = {
            "source_document": file.name,
            "collection": dir.name,
            "access_roles": accessible_roles(SourceCollection(dir.name)),
        }
        chunks = self.document_processor.process(file_path=file, additional_metdata=additional_metdata)

        return chunks

    def ingest_the_files(self, folder: Directory) -> None:
        """Process supported files in each configured source collection."""

        for source_collection_dirs in folder.sub_dirs or []:
            source_collection = source_collection_dirs.name

            if source_collection.name == "db":
                continue

            for file in source_collection_dirs.files or []:
                chunks: list[Document] = self.chunk_document(file, source_collection)

                embeddings: list[list[float]] = self.embedder.embed_file_chunks(file, chunks)
                sparse_embeddings: list[SparseVector] = self.embedder.embed_file_chunks_sparse(file, chunks)

                self.vector_db.add_documents(chunks, embeddings, sparse_embeddings)

    def process(self) -> None:
        """Discover the configured data directory and ingest its files."""
        logger.info("Starting ingestion from %s", self.MEDIASSIST_DATA)
        mediassist_folder: Directory = generate_file_directory(self.MEDIASSIST_DATA)
        self.vector_db.recreate_collection()
        self.ingest_the_files(folder=mediassist_folder)



