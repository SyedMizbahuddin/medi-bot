import logging
from pathlib import Path
from langchain.embeddings import Embeddings
from src.config.app_config import app_settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List
from src.ingestion.store.store import Store

logger = logging.getLogger(__name__)


class Embedder:
    SALT: str = "embedding"
    
    def __init__(self, store: Store):
        """Initialize the embedder with a persistence store."""
        self.store: Store = store
        self._embedder: Embeddings = HuggingFaceEmbeddings(model=app_settings.EMBEDDING_MODEL)
    
    
    def embed(self, file_path: Path, docs: List[Document]) -> list[list[float]]:
        """Load cached embeddings or create and persist embeddings for documents."""
        logger.info("Looking for cached embeddings for %s", file_path.name)
        cached_embeddings = self.store.get_embeddings(
            file_path=file_path,
            salt=self.SALT,
        )
        if cached_embeddings is not None:
            logger.info("Using cached embeddings for %s", file_path.name)
            return cached_embeddings

        logger.info("Creating embeddings for %d documents from %s", len(docs), file_path.name)
        texts = [doc.page_content for doc in docs]
        vectors = self._embedder.embed_documents(texts)
        self.store.set_embeddings(
            file_path=file_path,
            salt=self.SALT,
            embeddings=vectors,
        )

        logger.info("Saved embeddings for %s", file_path.name)

        return vectors
        
