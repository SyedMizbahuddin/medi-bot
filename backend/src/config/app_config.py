from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    EMBEDDING_MODEL: str = ""
    SPARSE_EMBEDDING_MODEL: str = ""
    DB_COLLECTION: str = "medi_vector_db"
    JWT_SECRET: str = "change-this-development-secret-32"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_DAYS: int = 365

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


app_settings = _Settings()
