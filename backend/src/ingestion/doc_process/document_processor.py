from langchain_core.documents import Document
from typing import Any
from pathlib import Path
from abc import ABC, abstractmethod


class DocumentProcessor(ABC):
    
    @abstractmethod
    def process(self, file_path: Path, additional_metdata: dict[str, Any] = {},) -> list[Document]:
        raise NotImplementedError()
         
    
    