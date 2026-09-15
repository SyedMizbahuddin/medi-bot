import logging
from langchain_core.documents import Document
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance,
    SparseVectorParams,
    Modifier,
    SparseVector,
)
from uuid import NAMESPACE_URL, uuid5
from src.services.embedder import Embedder
from src.config.app_config import app_settings
from pathlib import Path
from qdrant_client import QdrantClient


CURRENT_DIR: Path = Path().cwd()
DB_PATH: Path = CURRENT_DIR.parent / "vector_db"

logger = logging.getLogger(__name__)


class VectorDB:
    def __init__(self, embedder: Embedder) -> None:
        """Initialize a local Qdrant client and retain the dense embedder."""
        self._client = QdrantClient(path=str(DB_PATH))
        self._embedder = embedder

    def recreate_collection(self) -> None:
        """Recreate the Qdrant collection for a fresh ingestion run."""
        logger.info("Recreating Qdrant collection %s", app_settings.DB_COLLECTION)
        sample = self._embedder.embed_query("sample")

        self._client.recreate_collection(
            collection_name=app_settings.DB_COLLECTION,
            vectors_config={"dense": VectorParams(size=len(sample), distance=Distance.COSINE)},
            sparse_vectors_config={"sparse": SparseVectorParams(modifier=Modifier.IDF)},
        )
        logger.info("Initialized Qdrant collection %s", app_settings.DB_COLLECTION)

    def _create_point_id(self, ind, doc) -> str:
        """Create a deterministic point ID for a document chunk."""
        return str(
            uuid5(
                NAMESPACE_URL,
                doc.id or f"{doc.metadata['source_document']}_{ind}",
            )
        )

    def add_documents(
        self, documents: list[Document], embeddings: list[list[float]], sparse_embeddings: list[SparseVector]
    ) -> None:
        """Build and upsert dense and sparse vectors with document payloads."""
        logger.info("Preparing %d documents for Qdrant", len(documents))
        points = [
            PointStruct(
                id=self._create_point_id(ind, doc),
                payload={**doc.metadata, "content": doc.page_content},
                vector={
                    "dense": embeddings[ind],
                    "sparse": sparse_embeddings[ind],
                },
            )
            for ind, doc in enumerate(documents)
        ]

        logger.info("Upserting %d points into %s", len(points), app_settings.DB_COLLECTION)
        self._client.upsert(collection_name=app_settings.DB_COLLECTION, points=points)
        logger.info("Upserted %d points into %s", len(points), app_settings.DB_COLLECTION)
