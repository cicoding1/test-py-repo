from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gitlab_trigger_token: str
    gitlab_project_id: str
    gitlab_ref: str
    gitlab_api_url: str  

    backend_host: str 
    backend_port: int

    cors_allowed_origins: List[str] = []
    cors_allowed_methods: List[str] = []
    cors_allowed_headers: List[str] = []
    cors_allow_credentials: bool = False 
    
      
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Call the original BaseSettings constructor first

    # Then post-process cors_allowed_origins => turn it into a list in case it s a string

     # Parse comma-separated strings into lists if needed
        if isinstance(self.cors_allowed_origins, str):
            self.cors_allowed_origins = [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]

        if isinstance(self.cors_allowed_methods, str):
            self.cors_allowed_methods = [method.strip() for method in self.cors_allowed_methods.split(",") if method.strip()]

        if isinstance(self.cors_allowed_headers, str):
            self.cors_allowed_headers = [header.strip() for header in self.cors_allowed_headers.split(",") if header.strip()]

        # Convert cors_allow_credentials from string to bool if needed
        if isinstance(self.cors_allow_credentials, str):
            self.cors_allow_credentials = self.cors_allow_credentials.lower() in ("true", "1", "yes")

   
settings = Settings()
