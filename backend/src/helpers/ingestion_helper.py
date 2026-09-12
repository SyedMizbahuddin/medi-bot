from src.models.dir_file_model import Directory
from pathlib import Path


def generate_file_directory(path: Path) -> Directory:
    sub_dirs = []
    files = []
    
    for child in path.iterdir():
        if child.is_file():
            files.append(child)
            
        if child.is_dir():
            sub_dirs.append(generate_file_directory(child))
    
    return Directory(name=path, sub_dirs=sub_dirs, files=files)