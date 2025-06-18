from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # GitLab-related config
    gitlab_trigger_token: str         # Token to trigger GitLab pipeline
    gitlab_project_id: str            # GitLab project ID
    gitlab_ref: str                   # Branch or ref name to trigger
    gitlab_api_url: str               # Base URL for GitLab API, e.g. gitlab.com

    # Backend server config
    backend_host: str                 # Host where FastAPI runs, e.g. 0.0.0.0
    backend_port: int                 # Port for FastAPI server, e.g. 5000

    # CORS settings, customizable via environment variables
    cors_allowed_origins: List[str] = []    # Allowed origins for CORS
    cors_allowed_methods: List[str] = []    # Allowed HTTP methods for CORS
    cors_allowed_headers: List[str] = []    # Allowed headers for CORS
    cors_allow_credentials: bool = False    # Whether to allow credentials in CORS

    # Tell Pydantic where to find the .env file and its encoding
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize normally with BaseSettings

        # Post-processing: parse comma-separated strings into lists if needed
        
        if isinstance(self.cors_allowed_origins, str):
            self.cors_allowed_origins = [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]

        if isinstance(self.cors_allowed_methods, str):
            self.cors_allowed_methods = [method.strip() for method in self.cors_allowed_methods.split(",") if method.strip()]

        if isinstance(self.cors_allowed_headers, str):
            self.cors_allowed_headers = [header.strip() for header in self.cors_allowed_headers.split(",") if header.strip()]

        # Convert cors_allow_credentials to bool if it's a string (from env)
        if isinstance(self.cors_allow_credentials, str):
            self.cors_allow_credentials = self.cors_allow_credentials.lower() in ("true", "1", "yes")

# Instantiate the settings object to be imported elsewhere
settings = Settings()
