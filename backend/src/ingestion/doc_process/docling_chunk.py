from src.ingestion.doc_process.document_processor import DocumentProcessor
from src.ingestion.store.store import Store
from pathlib import Path
from typing import Any
from docling_core.types.doc.document import DoclingDocument
from langchain_docling.loader import MetaExtractor, BaseMetaExtractor
from langchain_core.documents import Document
from src.config.app_config import app_settings
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling_core.transforms.chunker.base import BaseChunker, BaseChunk
from docling_core.transforms.chunker.hybrid_chunker import HybridChunker
from docling.datamodel.document import ConversionResult
from hierarchical.postprocessor import ResultPostprocessor # type: ignore
from docling.document_converter import DocumentConverter

import torch

torch.backends.mkldnn.enabled = False  # type: ignore


class DoclingProccesor(DocumentProcessor):
    SALT: str = 'docling'

    def __init__(self, store: Store):
        self._converter: DocumentConverter = DocumentConverter()
        self._chunker: BaseChunker = HybridChunker(
            tokenizer=HuggingFaceTokenizer.from_pretrained(app_settings.EMBEDDING_MODEL)
        )
        self._meta_extractor: BaseMetaExtractor = MetaExtractor()
        self.store: Store = store

    def _convert_to_docling(self, file_path: Path) -> ConversionResult:
        result: ConversionResult = self._converter.convert(source=file_path)
        ResultPostprocessor(result).process()
        return result

    def _chunk_it(self, docling_document: DoclingDocument) -> list[BaseChunk]:
        chunks: list[BaseChunk] = list(self._chunker.chunk(docling_document))
        return chunks

    def _to_Langchain_Document(
        self,
        chunks: list[BaseChunk],
        file_path: Path,
        additional_metdata: dict[str, Any] = {},
    ) -> list[Document]:
        documents = []
        for chunk in chunks:
            meta_data: dict[str, Any] = self._meta_extractor.extract_chunk_meta(
                file_path=str(file_path), chunk=chunk
            )
            meta_data.update(additional_metdata)
            documents.append(
                Document(
                    page_content=self._chunker.contextualize(chunk), meta_data=meta_data
                )
            )

        return documents

    def process(self, file_path: Path, additional_metdata: dict[str, Any] = {},) -> list[Document]:
        
        cached_chunks = self.store.get_chunks(file_path=file_path, salt=self.SALT)
        if cached_chunks:
            return cached_chunks
        
        result: ConversionResult = self._convert_to_docling(file_path=file_path)
        chunks: list[BaseChunk] = self._chunk_it(docling_document=result.document)
        documents: list[Document] = self._to_Langchain_Document(
            chunks=chunks, file_path=file_path, additional_metdata=additional_metdata,
        )
        
        self.store.set_chunks(file_path=file_path, salt=self.SALT, chunks=documents)

        return documents


