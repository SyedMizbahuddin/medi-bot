from pydantic import TypeAdapter
from src.ingestion.store.store import Store
from langchain_core.documents import Document
from typing import Optional, List
from pathlib import Path
import pandas as pd


CURRENT_DIR: Path = Path().cwd()
CHUNKS_DIR: Path  = CURRENT_DIR.parent / 'cache_chunk_data'
# CHUNKS_EMBEDDING_DIR = CHUNKS_DIR / app_settings.EMBEDDING_MODEL

CHUNK_FILE = 'chunks.parquet'
EMBEDDINGS_FILE = 'embeddings.json'

list_document = TypeAdapter(List[Document])

class FileStore(Store):
    
    def __init__(self, force: bool = False):
        self.force = force
        
    
    def _get_chunks_dir(self, file_path: Path) -> Path:
        group = file_path.parent.name
                
        group_dir = CHUNKS_DIR / group
        file_name = file_path.stem
        
        # chunk_data/embedding-model/nursing/infection_control/
        file_chunk_dir = group_dir / file_name
        file_chunk_dir.mkdir(
            parents=True, 
            exist_ok=True,
        )
        
        return file_chunk_dir
    
    def _get_chunks_file(self, file_path : Path, salt : str) -> Path:
        file_chunk_dir = self._get_chunks_dir(file_path)
        # chunk_data/embedding-model/nursing/infection_control/chunks.json
        chunks_file = file_chunk_dir / salt / CHUNK_FILE
        
        return chunks_file
            
    
    def _get_embeddings_file(self, file_path : Path, salt : str)  -> Path:
        file_chunk_dir = self._get_chunks_dir(file_path)
        # chunk_data/embedding-model/nursing/infection_control/embeddings.json
        embeddings_file = file_chunk_dir / salt / EMBEDDINGS_FILE
        
        return embeddings_file    
    
    
    def get_chunks(self, file_path : Path, salt : str) -> Optional[List[Document]]:
        chunks_file = self._get_chunks_file(file_path, salt)

        if not chunks_file.is_file() or self.force:
            return None
        
        parquet_frame = pd.read_parquet(chunks_file)
        records = parquet_frame.to_dict(orient="records")
        
        chunks = list_document.validate_python(records)
        return chunks
    
    def set_chunks(self, file_path : Path, salt : str, chunks: List[Document]) -> None:
        chunks_file = self._get_chunks_file(file_path, salt)
        
        for i, chunk in enumerate(chunks):
            chunk.id = file_path.stem + "_" + str(i)

        pd.DataFrame(
            list_document.dump_python(chunks,  mode='json')
        ).to_parquet(chunks_file, index=False)
        
        return None
        
    
    
    def get_embeddings(self, file_path : Path, salt : str)  -> Optional[Path]:
        embeddings_file = self._get_embeddings_file(file_path, salt)

        if not embeddings_file.is_file() or self.force:
            return None
        
        return None
    