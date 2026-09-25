import sqlite3


from src.config.app_config import app_settings
from src.models.user import User
from src.services.auth_service import AuthService
from src.services.sqlite_db import SQLiteDB
from src.services.user_service import UserService
from src.utils.constants import Role


def build_services(tmp_path):
    sqlite_db = SQLiteDB(tmp_path / "users.sqlite3")
    user_service = UserService(sqlite_db)
    auth_service = AuthService(user_service)
    return sqlite_db, user_service, auth_service


def test_sqlite_db_creates_parent_and_named_rows(tmp_path):
    database_path = tmp_path / "nested" / "users.sqlite3"
    sqlite_db = SQLiteDB(database_path)

    assert database_path.parent.is_dir()
    with sqlite_db.connect() as connection:
        connection.execute("CREATE TABLE example (id INTEGER, name TEXT)")
        connection.execute("INSERT INTO example VALUES (?, ?)", (1, "one"))
        row = connection.execute("SELECT id, name FROM example").fetchone()

    assert isinstance(row, sqlite3.Row)
    assert row["name"] == "one"


def test_user_service_seeds_and_authenticates_users(tmp_path):
    sqlite_db, user_service, _ = build_services(tmp_path)

    admin = user_service.get_user("admin")
    doctor = user_service.authenticate("doctor", "doctor")
    created = User(user_name="nurse-user", password="secret", roles=[Role.NURSE])
    user_service.create_user(created)

    assert admin is not None
    assert set(admin.roles) == set(Role)
    assert doctor is not None
    assert doctor.roles == [Role.DOCTOR]
    assert user_service.authenticate("doctor", "wrong") is None
    created_user = user_service.get_user("nurse-user")
    assert created_user is not None
    assert created_user.roles == [Role.NURSE]

    with sqlite_db.connect() as connection:
        password_hash = connection.execute(
            "SELECT password_hash FROM users WHERE user_name = ?",
            ("nurse-user",),
        ).fetchone()["password_hash"]
    assert password_hash.startswith("scrypt$")
    assert password_hash != "secret"


def test_auth_service_delegates_and_preserves_jwt_claims(tmp_path):
    _, user_service, auth_service = build_services(tmp_path)
    user = user_service.get_user("doctor")

    assert user is not None
    assert auth_service.authenticate("doctor", "doctor") == user
    assert not hasattr(auth_service, "sqlite_db")

    token = auth_service.create_access_token(user)
    claims = auth_service.decode_access_token(token)

    assert claims["sub"] == "doctor"
    assert claims["user_name"] == "doctor"
    assert claims["roles"] == [Role.DOCTOR.value]
    assert claims["exp"] - claims["iat"] == app_settings.JWT_EXPIRY_DAYS * 24 * 60 * 60
