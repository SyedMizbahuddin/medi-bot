import logging
from src.models.dir_file_model import Directory
from pathlib import Path

logger = logging.getLogger(__name__)


def generate_file_directory(path: Path) -> Directory:
    """Build a recursive directory model for a filesystem path."""
    logger.info("Scanning directory %s", path)
    sub_dirs = []
    files = []
    
    for child in path.iterdir():
        if child.is_file():
            files.append(child)
            
        if child.is_dir():
            sub_dirs.append(generate_file_directory(child))
    
    return Directory(name=path, sub_dirs=sub_dirs, files=files)