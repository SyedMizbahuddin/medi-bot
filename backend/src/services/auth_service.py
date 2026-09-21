"""SQLite-backed authentication and JWT service."""

import base64
import hashlib
import hmac
import json
import secrets
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt

from src.config.app_config import app_settings
from src.models.user import User
from src.utils.constants import Role


class AuthService:
    """Manage users in SQLite and issue long-lived signed JWTs."""

    def __init__(self) -> None:
        """Initialize the database and seed learning-project users."""
        self.db_path = Path().cwd().parent / "sql_db" / "users.sqlite3"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize_database()
        self._seed_users()

    def _connect(self) -> sqlite3.Connection:
        """Open a connection to the authentication database."""
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize_database(self) -> None:
        """Create the users table when it does not exist."""
        with self._connect() as connection:
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
        """Create default learning users without overwriting existing users."""
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
        with self._connect() as connection:
            connection.execute(
                "INSERT INTO users (user_name, password_hash, roles) VALUES (?, ?, ?)",
                (user.user_name, password_hash, json.dumps([role.value for role in user.roles])),
            )
        return user

    def get_user(self, user_name: str) -> User | None:
        """Load a user by username without exposing the stored password hash."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT user_name, roles FROM users WHERE user_name = ?",
                (user_name,),
            ).fetchone()
        if row is None:
            return None
        return User(
            user_name=row["user_name"],
            password="",
            roles=[Role(role) for role in json.loads(row["roles"])],
        )

    def authenticate(self, user_name: str, password: str) -> User | None:
        """Verify credentials and return the user when they are valid."""
        with self._connect() as connection:
            row = connection.execute(
                "SELECT user_name, password_hash, roles FROM users WHERE user_name = ?",
                (user_name,),
            ).fetchone()
        if row is None or not self._verify_password(password, row["password_hash"]):
            return None
        return User(
            user_name=row["user_name"],
            password="",
            roles=[Role(role) for role in json.loads(row["roles"])],
        )

    def create_access_token(self, user: User) -> str:
        """Create a JWT containing username, roles, issue time, and expiry."""
        issued_at = datetime.now(timezone.utc)
        payload = {
            "sub": user.user_name,
            "user_name": user.user_name,
            "roles": [role.value for role in user.roles],
            "iat": issued_at,
            "exp": issued_at + timedelta(days=app_settings.JWT_EXPIRY_DAYS),
        }
        return jwt.encode(payload, app_settings.JWT_SECRET, algorithm=app_settings.JWT_ALGORITHM)

    def decode_access_token(self, token: str) -> dict:
        """Validate and decode a JWT access token."""
        return jwt.decode(token, app_settings.JWT_SECRET, algorithms=[app_settings.JWT_ALGORITHM])

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
