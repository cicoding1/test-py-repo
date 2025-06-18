from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_secret_token: str
    gitlab_trigger_token: str
    gitlab_project_id: str
    gitlab_ref: str

    class Config:
        env_file = ".env"

settings = Settings()
