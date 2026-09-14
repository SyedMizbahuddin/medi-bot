import logging
from src.ingestion.embedder import Embedder
from src.utils.constants import accessible_roles, SourceCollection
from src.ingestion.store.store import Store
import argparse
from src.ingestion.store.file_store import FileStore
from src.ingestion.doc_process.docling_chunk import DoclingProcessor
from langchain_core.documents import Document
from src.helpers.ingestion_helper import generate_file_directory
from src.ingestion.doc_process.document_processor import DocumentProcessor
from src.models.dir_file_model import Directory
from pathlib import Path

logger = logging.getLogger(__name__)

logging.basicConfig(
      level=logging.INFO,
      format="%(asctime)s | %(levelname)-8s | %(name)-32s | %(message)s",
  )

for logger_name in ("httpx", "httpcore", "huggingface_hub", "transformers", "sentence_transformers"):
    logging.getLogger(logger_name).setLevel(logging.WARNING)

class IngestionPipeline:

    def __init__(self, document_processor: DocumentProcessor, embedder: Embedder):
        """Initialize the ingestion pipeline dependencies."""
        self.document_processor: DocumentProcessor = document_processor
        self.embedder: Embedder = embedder
        self.CURRENT_DIR: Path = Path().cwd()
        self.MEDIASSIST_DATA: Path = self.CURRENT_DIR.parent / "mediassist_data"

    def chunk_document(self, file: Path, dir: Path) -> list[Document]:
        """Chunk one source document and attach access-control metadata."""
        logger.info("Chunking document %s", file.name)
        additional_metdata = {
            "source_document": file.name,
            "collection": dir.name,
            "access_roles": accessible_roles(SourceCollection(dir.name))
        }
        chunks = self.document_processor.process(
            file_path=file, additional_metdata=additional_metdata
        )

        return chunks

    def ingest_the_files(self, folder: Directory):
        """Process supported files in each configured source collection."""

        for source_collection_dirs in folder.sub_dirs or []:
            source_collection = source_collection_dirs.name
            
            if source_collection.name == 'db':
                continue

            for file in source_collection_dirs.files or []:
                chunks: list[Document] = self.chunk_document(
                    file, source_collection
                )
                
                embeddings: list[list[float]] = self.embedder.embed(file, chunks)

    def process(self):
        """Discover the configured data directory and ingest its files."""
        logger.info("Starting ingestion from %s", self.MEDIASSIST_DATA)
        mediassist_folder: Directory = generate_file_directory(self.MEDIASSIST_DATA)
        self.ingest_the_files(folder=mediassist_folder)




def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--force",
        action="store_true",
        help="Use without force to use the cache",
    )

    args = parser.parse_args()
    
    file_store: Store = FileStore(args.force)
    docling_processor: DocumentProcessor = DoclingProcessor(store=file_store)
    embedder = Embedder(file_store)
    pipeline= IngestionPipeline(document_processor=docling_processor, embedder=embedder)
    
    pipeline.process()


if __name__ == "__main__":
    main()
