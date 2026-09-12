from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    
    EMBEDDING_MODEL : str = ""
    
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

app_settings = _Settings()