from src.utils.utils import get_point_id
from pydash import get
from qdrant_client.http.models.models import ScoredPoint, Record
from src.utils.constants import Role
import logging
from langchain_core.documents import Document
from qdrant_client.models import (
    PointStruct,
    VectorParams,
    Distance,
    SparseVectorParams,
    Modifier,
    SparseVector,
    FusionQuery,
    Fusion,
    Prefetch,
    Filter,
    FieldCondition,
    MatchAny,
)
from src.services.rag.core.embedder import Embedder
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

    def _create_point_id(self, ind: int, doc: Document) -> str:
        """Create a deterministic point ID for a document chunk."""
        if doc.id:
            return str(doc.id)

        return get_point_id(doc.metadata["source_document"], ind)

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

    def retrieve(self, input: str, role: Role) -> list[Document]:
        dense_embedding: list[float] = self._embedder.embed_query(input)
        sparse_embedding: SparseVector = self._embedder.embed_query_sparse(input)

        query_filter = Filter(
            must=[
                FieldCondition(
                    key="access_roles",
                    match=MatchAny(
                        any=[role.value],
                    ),
                )
            ]
        )
        results: list[ScoredPoint] = self._client.query_points(
            collection_name=app_settings.DB_COLLECTION,
            query=FusionQuery(fusion=Fusion.RRF),
            query_filter=query_filter,
            limit=20,
            prefetch=[
                Prefetch(
                    query=dense_embedding,
                    using="dense",
                    limit=20,
                    filter=query_filter,
                ),
                Prefetch(
                    query=sparse_embedding,
                    using="sparse",
                    limit=20,
                    filter=query_filter,
                ),
            ],
        ).points

        docs = []
        for result in results:
            metadata = result.payload or {}
            content = str(get(metadata, "content"))
            metadata.pop("content")
            metadata["_score"] = result.score
            docs.append(Document(id=str(result.id), page_content=content, metadata=metadata))

        return docs

    def add_surroundings(self, docs: list[Document]) -> list[Document]:
        """Enrich each retrieved chunk with its previous and next chunk content."""
        if not docs:
            return []

        # Step 1: Identify which (source_document, index) chunks we need to fetch.
        # For every retrieved doc, we need index-1, index, and index+1.
        needed_chunk_keys: set[tuple[str, int]] = set()

        for doc in docs:
            source_document = doc.metadata.get("source_document")
            index = doc.metadata.get("index")

            if not isinstance(source_document, str) or not isinstance(index, int):
                continue

            for neighbor_index in (index - 1, index, index + 1):
                if neighbor_index >= 0:
                    needed_chunk_keys.add((source_document, neighbor_index))

        # Step 2: Map each needed chunk to its deterministic Qdrant point ID.
        point_id_to_chunk_key = {
            get_point_id(source_document, index): (source_document, index)
            for source_document, index in needed_chunk_keys
        }

        # Step 3: Fetch all needed chunks in a single batched call.
        points: list[Record] = self._client.retrieve(
            collection_name=app_settings.DB_COLLECTION,
            ids=list(point_id_to_chunk_key.keys()),
            with_payload=["content", "source_document", "index", "collection", "section_title"],
            with_vectors=False,
        )

        # Step 4: Build a simple lookup: (source_document, index) -> content.
        content_by_chunk_key: dict[tuple[str, int], Record] = {}

        for point in points:
            payload = point.payload or {}
            source_document = payload.get("source_document")
            index = payload.get("index")
            content = payload.get("content")

            if isinstance(source_document, str) and isinstance(index, int) and content:
                content_by_chunk_key[(source_document, index)] = point

        # Step 5: Rebuild each doc's page_content as prev + current + next.
        indices_by_source: dict[str, set[int]] = {}

        for doc in docs:
            source_document = doc.metadata.get("source_document")
            index = doc.metadata.get("index")

            if isinstance(source_document, str) and isinstance(index, int):
                neighbors = {index - 1, index, index + 1}
                indices_by_source.setdefault(source_document, set()).update(neighbors)


        enriched_docs: list[Document] = []

        for source_document, indices in indices_by_source.items():
            # Only keep indices that actually exist in Qdrant, then sort them.
            sorted_indices = sorted(i for i in indices if (source_document, i) in content_by_chunk_key)

            # Split into contiguous runs, e.g. [3,4,5,6,7] stays one run,
            # but [3,4,5, 9,10] becomes two runs.
            runs: list[list[int]] = []
            for i in sorted_indices:
                if runs and i == runs[-1][-1] + 1:
                    runs[-1].append(i)
                else:
                    runs.append([i])

            for run in runs:
                contents = []
                section_titles = []
                collection = ""

                for ind in run:
                    point = content_by_chunk_key[(source_document, ind)]
                    payload = point.payload or {}
                    content = payload.get("content", "")
                    section_title = payload.get("section_title", "")
                    collection = payload.get("collection", "")

                    contents.append(content)
                    section_titles.append(section_title)

                combined_content = "\n\n".join(contents)

                enriched_docs.append(
                    Document(
                        page_content=combined_content,
                        metadata={
                            "source_document": source_document,
                            "merged_indices": run,
                            "section_titles": section_titles,
                            "collection": collection,
                        },
                    )
                )

        return enriched_docs
