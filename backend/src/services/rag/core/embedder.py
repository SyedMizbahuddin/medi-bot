from fastembed import SparseTextEmbedding, TextEmbedding
import logging
from pathlib import Path
from src.config.app_config import app_settings
from langchain_core.documents import Document
from typing import List
from src.services.rag.core.store.store import Store
from qdrant_client.models import SparseVector
import numpy as np

logger = logging.getLogger(__name__)


class Embedder:
    SALT: str = "embedding"


    def __init__(self, store: Store):
        """Initialize the embedder with a persistence store."""
        self._store: Store = store

        self._dense_model = TextEmbedding(model_name=app_settings.EMBEDDING_MODEL)
        self._sparse_model = SparseTextEmbedding(
            model_name=app_settings.SPARSE_EMBEDDING_MODEL,
        )

    def embed_file_chunks(self, file_path: Path, docs: List[Document]) -> list[list[float]]:
        """Load cached embeddings or create and persist embeddings for documents."""
        logger.info("Looking for cached embeddings for %s", file_path.name)

        cached_embeddings = self._store.get_embeddings(
            file_path=file_path,
            salt=self.SALT,
        )
        if cached_embeddings is not None:
            logger.info("Using cached embeddings for %s", file_path.name)
            return cached_embeddings

        logger.info("Creating embeddings for %d documents from %s", len(docs), file_path.name)

        texts = [doc.page_content for doc in docs]
        vectors: list[list[float]] = [
            embedding.astype(np.float32).tolist()
            for embedding in self._dense_model.embed(texts)
        ]
        self._store.set_embeddings(
            file_path=file_path,
            salt=self.SALT,
            embeddings=vectors,
        )

        logger.info("Saved embeddings for %s", file_path.name)

        return vectors

    def embed_file_chunks_sparse(
        self,
        file_path: Path,
        docs: list[Document],
    ) -> list[SparseVector]:
        """Load or create BM25 sparse embeddings."""
        logger.info(
            "Looking for cached sparse embeddings for %s",
            file_path.name,
        )

        cached_embeddings = self._store.get_sparse_embeddings(
            file_path=file_path,
            salt=self.SALT,
        )

        if cached_embeddings is not None:
            logger.info(
                "Using cached sparse embeddings for %s",
                file_path.name,
            )
            return cached_embeddings

        logger.info(
            "Creating sparse embeddings for %d documents from %s",
            len(docs),
            file_path.name,
        )

        texts = [doc.page_content for doc in docs]

        vectors: list[SparseVector] = [
            SparseVector(
                indices=embedding.indices.astype(int).tolist(),
                values=embedding.values.astype(float).tolist(),
            )
            for embedding in self._sparse_model.embed(texts)
        ]

        self._store.set_sparse_embeddings(
            file_path=file_path,
            salt=self.SALT,
            embeddings=vectors,
        )

        logger.info(
            "Saved %d sparse embeddings for %s",
            len(vectors),
            file_path.name,
        )

        return vectors
    
    
    def embed_query(self, text: str) -> list[float]:
        """Create a dense embedding for a single query string."""
        embedding = next(iter(self._dense_model.embed([text])))

        return embedding.tolist()

    def embed_query_sparse(self, text: str) -> SparseVector:
        embedding = list(self._sparse_model.embed([text]))[0]
        vector = SparseVector(
            indices=embedding.indices.astype(int).tolist(),
            values=embedding.values.astype(float).tolist(),
        )

        return vector
