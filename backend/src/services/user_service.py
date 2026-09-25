"""User persistence and credential management."""

import base64
import hashlib
import hmac
import json
import sqlite3
import secrets

from src.models.user import User
from src.services.sqlite_db import SQLiteDB
from src.utils.constants import Role


class UserService:
    """Manage users, passwords, roles, and authentication against SQLite."""

    def __init__(self, sqlite_db: SQLiteDB) -> None:
        """Initialize the user table and seed default learning users."""
        self.sqlite_db = sqlite_db
        self._initialize_database()
        self._seed_users()

    def _initialize_database(self) -> None:
        """Create the users table when it does not exist."""
        with self.sqlite_db.connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_name TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL,
                    roles TEXT NOT NULL
                )
                """
            )

    def _seed_users(self) -> None:
        """Create default users without overwriting existing users."""
        default_users = [
            User(user_name="admin", password="admin", roles=list(Role)),
            User(user_name="doctor", password="doctor", roles=[Role.DOCTOR]),
        ]
        for user in default_users:
            if self.get_user(user.user_name) is None:
                self.create_user(user)

    def create_user(self, user: User) -> User:
        """Store a user with a salted scrypt password hash."""
        password_hash = self._hash_password(user.password)
        with self.sqlite_db.connect() as connection:
            connection.execute(
                "INSERT INTO users (user_name, password_hash, roles) VALUES (?, ?, ?)",
                (user.user_name, password_hash, json.dumps([role.value for role in user.roles])),
            )
        return user

    def get_user(self, user_name: str) -> User | None:
        """Load a user by username without exposing the stored password hash."""
        with self.sqlite_db.connect() as connection:
            row = connection.execute(
                "SELECT user_name, roles FROM users WHERE user_name = ?",
                (user_name,),
            ).fetchone()
        return self._row_to_user(row) if row is not None else None

    def authenticate(self, user_name: str, password: str) -> User | None:
        """Verify credentials and return the user when they are valid."""
        with self.sqlite_db.connect() as connection:
            row = connection.execute(
                "SELECT user_name, password_hash, roles FROM users WHERE user_name = ?",
                (user_name,),
            ).fetchone()
        if row is None or not self._verify_password(password, row["password_hash"]):
            return None
        return self._row_to_user(row)

    @staticmethod
    def _row_to_user(row: sqlite3.Row) -> User:
        """Convert a SQLite row into a user without its password hash."""
        return User(
            user_name=row["user_name"],
            password="",
            roles=[Role(role) for role in json.loads(row["roles"])],
        )

    @staticmethod
    def _hash_password(password: str) -> str:
        """Hash a password with a random salt using scrypt."""
        salt = secrets.token_bytes(16)
        digest = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=64)
        return "scrypt${}${}".format(
            base64.urlsafe_b64encode(salt).decode(),
            base64.urlsafe_b64encode(digest).decode(),
        )

    @staticmethod
    def _verify_password(password: str, stored_hash: str) -> bool:
        """Verify a password against a stored scrypt hash."""
        try:
            scheme, encoded_salt, encoded_digest = stored_hash.split("$", 2)
            if scheme != "scrypt":
                return False
            salt = base64.urlsafe_b64decode(encoded_salt.encode())
            expected = base64.urlsafe_b64decode(encoded_digest.encode())
            actual = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=64)
            return hmac.compare_digest(actual, expected)
        except (ValueError, TypeError):
            return False
