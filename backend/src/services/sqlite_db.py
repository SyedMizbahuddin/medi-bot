"""SQLite connection management."""

import sqlite3
from pathlib import Path


class SQLiteDB:
    """Own the SQLite database path and connection configuration."""

    def __init__(self, db_path: str | Path) -> None:
        """Store the database path and create its parent directory."""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        """Open a row-aware SQLite connection."""
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection
