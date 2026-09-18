import shutil
from qdrant_client.models import SparseVector
import logging
from pydantic import TypeAdapter
from src.services.store.store import Store
from langchain_core.documents import Document
from typing import Optional, List
from pathlib import Path
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

CURRENT_DIR: Path = Path().cwd()
CHUNKS_DIR: Path = CURRENT_DIR.parent / "cache_chunk_data"
# CHUNKS_EMBEDDING_DIR = CHUNKS_DIR / app_settings.EMBEDDING_MODEL

CHUNK_FILE = "chunks.parquet"
EMBEDDINGS_FILE = "embeddings.npy"
SPARSE_EMBEDDINGS_FILE = "sparse_embeddings.parquet"

list_document = TypeAdapter(List[Document])
list_sparse_vector = TypeAdapter(List[SparseVector])


class FileStore(Store):
    def __init__(self):
        """Initialize the file store, optionally bypassing existing cache files."""
        pass

    def _get_chunks_dir(self, file_path: Path, salt: str) -> Path:
        """Return and create the cache directory for a source file."""
        group = file_path.parent.name

        group_dir = CHUNKS_DIR / group
        file_name = file_path.stem

        # chunk_data/embedding-model/nursing/infection_control/
        file_chunk_dir = group_dir / file_name / salt
        file_chunk_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        return file_chunk_dir

    def _get_chunks_file(self, file_path: Path, salt: str) -> Path:
        """Return the chunk cache path for a source file."""
        file_chunk_dir = self._get_chunks_dir(file_path, salt)
        # chunk_data/embedding-model/nursing/infection_control/chunks.parquet
        chunks_file = file_chunk_dir / CHUNK_FILE

        return chunks_file

    def _get_embeddings_file(self, file_path: Path, salt: str) -> Path:
        """Return the embedding cache path for a source file."""
        file_chunk_dir = self._get_chunks_dir(file_path, salt)
        # chunk_data/embedding-model/nursing/infection_control/embeddings.npy
        embeddings_file = file_chunk_dir / EMBEDDINGS_FILE

        return embeddings_file

    def _get_sparse_embeddings_file(
        self,
        file_path: Path,
        salt: str,
    ) -> Path:
        """Return the sparse embedding cache path."""
        file_chunk_dir = self._get_chunks_dir(
            file_path,
            salt,
        )
        # chunk_data/embedding-model/nursing/infection_control/sparse_embeddings.parquet
        return file_chunk_dir / SPARSE_EMBEDDINGS_FILE

    def get_chunks(self, file_path: Path, salt: str) -> Optional[List[Document]]:
        """Load cached document chunks, or return None when unavailable."""
        chunks_file = self._get_chunks_file(file_path, salt)

        if not chunks_file.is_file() :
            logger.info("Chunk cache miss for %s", file_path.name)
            return None

        parquet_frame = pd.read_parquet(chunks_file)

        records_json = parquet_frame.to_json(
            orient="records",
        )
        chunks = list_document.validate_json(records_json)
        logger.info("Loaded %d cached chunks for %s", len(chunks), file_path.name)
        return chunks

    def set_chunks(self, file_path: Path, salt: str, chunks: List[Document]) -> None:
        """Persist document chunks as a Parquet cache file."""
        chunks_file = self._get_chunks_file(file_path, salt)

        pd.DataFrame(list_document.dump_python(chunks, mode="json")).to_parquet(chunks_file, index=False)
        logger.info("Saved %d chunks for %s", len(chunks), file_path.name)

        return None

    def get_embeddings(self, file_path: Path, salt: str) -> Optional[list[list[float]]]:
        """Load cached embeddings, or return None when unavailable."""
        embeddings_file = self._get_embeddings_file(file_path, salt)

        if not embeddings_file.is_file():
            logger.info("Embedding cache miss for %s", file_path.name)
            return None

        matrix = np.load(embeddings_file, allow_pickle=False)
        logger.info("Loaded %d cached embeddings for %s", len(matrix), file_path.name)
        return matrix.tolist()

    def set_embeddings(self, file_path: Path, salt: str, embeddings: list[list[float]]) -> None:
        """Persist embeddings as a NumPy array cache file."""
        embeddings_file = self._get_embeddings_file(file_path, salt)

        matrix = np.asarray(embeddings, dtype=np.float32)

        np.save(embeddings_file, matrix, allow_pickle=False)
        logger.info("Saved %d embeddings for %s", len(embeddings), file_path.name)

        return None

    def get_sparse_embeddings(
        self,
        file_path: Path,
        salt: str,
    ) -> Optional[list[SparseVector]]:
        """Load cached sparse embeddings."""
        embeddings_file = self._get_sparse_embeddings_file(
            file_path,
            salt,
        )

        if not embeddings_file.is_file() :
            logger.info(
                "Sparse embedding cache miss for %s",
                file_path.name,
            )
            return None

        parquet_frame = pd.read_parquet(embeddings_file)
        records = parquet_frame.to_dict(orient="records")

        embeddings = list_sparse_vector.validate_python(records)

        logger.info(
            "Loaded %d cached sparse embeddings for %s",
            len(embeddings),
            file_path.name,
        )

        return embeddings

    def set_sparse_embeddings(
        self,
        file_path: Path,
        salt: str,
        embeddings: list[SparseVector],
    ) -> None:
        """Persist sparse embeddings as Parquet."""
        embeddings_file = self._get_sparse_embeddings_file(
            file_path,
            salt,
        )

        pd.DataFrame(list_sparse_vector.dump_python(embeddings, mode="json")).to_parquet(embeddings_file, index=False)

        logger.info(
            "Saved %d sparse embeddings for %s",
            len(embeddings),
            file_path.name,
        )
    
    
    def clear_cache(self) -> None:
        logger.info("Clearing cache")
        if CHUNKS_DIR.exists():
            shutil.rmtree(CHUNKS_DIR)
        logger.info("Cleared cache")

