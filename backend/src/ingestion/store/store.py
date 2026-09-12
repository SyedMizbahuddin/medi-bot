from langchain_core.documents import Document
from typing import Optional, List
from pathlib import Path
from abc import ABC, abstractmethod


class Store(ABC):
    
    @abstractmethod
    def get_chunks(self, file_path : Path, salt : str) -> Optional[List[Document]]:
        raise NotImplementedError()
    
    @abstractmethod
    def get_embeddings(self, file_path : Path, salt : str)  -> Optional[Path]:
        raise NotImplementedError()
    
    @abstractmethod
    def set_chunks(self, file_path : Path, salt : str, chunks: List[Document]) -> None:
        raise NotImplementedError()