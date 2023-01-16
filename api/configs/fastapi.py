from pydantic import BaseSettings


class FastapiSettings(BaseSettings):
    DEBUG: str
    class Config:
        env_file: str = ".env"