from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    SPARSE_EMBEDDING_MODEL: str = "Qdrant/bm25"
    CROSS_ENCODER_MODEL: str = 'jinaai/jina-reranker-v2-base-multilingual'
    GROQ_MODEL: str = "openai/gpt-oss-20b"
    GROQ_API_KEY: str = ""
    DB_COLLECTION: str = "medi_vector_db"
    JWT_SECRET: str = "change-this-development-secret-32"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_DAYS: int = 365

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


app_settings = _Settings()
