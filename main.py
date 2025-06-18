from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routes.pipeline import router as pipeline_router  # import the router

# Create FastAPI app
app = FastAPI()

# Enable CORS 
# In production, remove ["*"] defaults and define explicit allowed values in your .env for better security

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins or ["*"],
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allowed_methods or ["*"],
    allow_headers=settings.cors_allowed_headers or ["*"],  # remove ["*"] later & remove comments in .env
)

# Register the routes from pipeline.py
app.include_router(pipeline_router)


if __name__ == "__main__":
    import uvicorn

    #modify 'host + port  => .env "
    # Use host and port from .env, enable auto reload for development

    uvicorn.run(
        "main:app",
        host=settings.backend_host,
        port=settings.backend_port,
        reload=True,
    )
