from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/audio_upload"
    # DATABASE_URL: str = "postgresql+psycopg2://user:password@localhost/audio_upload"
    DB_NAME: str = "audio_upload"
    SECRET_KEY: str = "YOUR_SECRET_KEY"
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()