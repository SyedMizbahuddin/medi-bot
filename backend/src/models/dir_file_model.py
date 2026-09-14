from typing import Optional
from pathlib import Path
from pydantic import BaseModel

class Directory(BaseModel):
    """Represent a directory and its immediate files and subdirectories."""
    
    name: Path
    sub_dirs: Optional[list["Directory"]] 
    files: Optional[list[Path]]