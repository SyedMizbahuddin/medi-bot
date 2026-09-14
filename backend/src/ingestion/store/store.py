from langchain_core.documents import Document
from typing import Optional, List
from pathlib import Path
from abc import ABC, abstractmethod


class Store(ABC):
    
    @abstractmethod
    def get_chunks(self, file_path : Path, salt : str) -> Optional[List[Document]]:
        """Load cached chunks for a source file."""
        raise NotImplementedError()
    
    @abstractmethod
    def get_embeddings(self, file_path : Path, salt : str)  -> Optional[list[list[float]]]:
        """Load cached embeddings for a source file."""
        raise NotImplementedError()
    
    @abstractmethod
    def set_chunks(self, file_path : Path, salt : str, chunks: List[Document]) -> None:
        """Persist chunks for a source file."""
        raise NotImplementedError()
    
    @abstractmethod
    def set_embeddings(self, file_path : Path, salt : str, embeddings: list[list[float]]) -> None:
        """Persist embeddings for a source file."""
        raise NotImplementedError()