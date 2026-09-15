import logging
from src.services.doc_process.document_processor import DocumentProcessor
from src.services.store.store import Store
from pathlib import Path
from typing import Any
from docling_core.types.doc.document import DoclingDocument
from langchain_core.documents import Document
from src.config.app_config import app_settings
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from docling_core.transforms.chunker.base import BaseChunker, BaseChunk
from docling_core.transforms.chunker.hybrid_chunker import HybridChunker
from docling.datamodel.document import ConversionResult

# from hierarchical.postprocessor import ResultPostprocessor # type: ignore
from docling.document_converter import DocumentConverter

import torch

torch.backends.mkldnn.enabled = False  # type: ignore

logger = logging.getLogger(__name__)


class DoclingProcessor(DocumentProcessor):
    SALT: str = "docling"

    def __init__(self, store: Store):
        """Initialize Docling conversion, chunking, metadata, and storage services."""
        self._converter: DocumentConverter = DocumentConverter()
        self._chunker: BaseChunker = HybridChunker(
            tokenizer=HuggingFaceTokenizer.from_pretrained(app_settings.EMBEDDING_MODEL), merge_peers=True
        )

        self.store: Store = store

    def _convert_to_docling(self, file_path: Path) -> ConversionResult:
        """Convert a source file into a Docling document."""
        logger.info("Converting document %s with Docling", file_path.name)
        result: ConversionResult = self._converter.convert(source=file_path)
        # ResultPostprocessor(result).process()
        return result

    def _chunk_it(self, docling_document: DoclingDocument) -> list[BaseChunk]:
        """Split a Docling document into hybrid chunks."""
        chunks: list[BaseChunk] = list(self._chunker.chunk(docling_document))
        logger.info("Created %d Docling chunks", len(chunks))
        return chunks

    def _get_metadata(self, chunk: BaseChunk) -> dict[str, Any]:
        """Extract headings, labels, and page information from a chunk."""
        chunk_meta = chunk.meta.export_json_dict()
        labels = set()
        pages = set()
        for item in chunk_meta.get("doc_items", []):
            if item.get("label"):
                labels.add(item.get("label"))

            for p in item.get("prov", []):
                if p.get("page_no"):
                    pages.add(p.get("page_no"))

        metadata = {}
        metadata["headings"] = chunk_meta.get("headings", [])
        metadata["section_title"] = metadata["headings"][-1] if len(metadata["headings"]) > 0 else None
        metadata["chunk_type"] = list(labels)[0] if len(labels) > 0 else None
        metadata["page_number"] = list(pages)[0] if len(pages) > 0 else None

        return metadata

    def _to_Langchain_Document(
        self,
        chunks: list[BaseChunk],
        file_path: Path,
        additional_metdata: dict[str, Any] = {},
    ) -> list[Document]:
        """Convert Docling chunks into LangChain documents."""
        documents = []
        for ind, chunk in enumerate(chunks):
            metadata = self._get_metadata(chunk)
            metadata["index"] = ind
            metadata.update(additional_metdata)

            documents.append(
                Document(
                    id=file_path.stem + "_" + str(ind),
                    page_content=self._chunker.contextualize(chunk),
                    metadata=metadata,
                )
            )

        return documents

    def process(
        self,
        file_path: Path,
        additional_metdata: dict[str, Any] = {},
    ) -> list[Document]:
        """Load cached chunks or convert, chunk, enrich, and cache a document."""

        cached_chunks = self.store.get_chunks(file_path=file_path, salt=self.SALT)
        if cached_chunks:
            logger.info("Using cached chunks for %s", file_path.name)
            return cached_chunks

        result: ConversionResult = self._convert_to_docling(file_path=file_path)
        chunks: list[BaseChunk] = self._chunk_it(docling_document=result.document)
        documents: list[Document] = self._to_Langchain_Document(
            chunks=chunks,
            file_path=file_path,
            additional_metdata=additional_metdata,
        )

        self.store.set_chunks(file_path=file_path, salt=self.SALT, chunks=documents)
        logger.info("Processed and cached %d chunks for %s", len(documents), file_path.name)

        return documents
