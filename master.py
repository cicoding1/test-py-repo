"""from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from config import settings


# this app actually uses the `settings` object from config.py for all config values

# Create FastAPI app
app = FastAPI()

# Enable CORS 
# In production, remove ["*"] defaults and define explicit allowed values in your .env for better security

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origins or ["*"],
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=settings.cors_allowed_methods or ["*"],
    allow_headers=settings.cors_allowed_headers or ["*"], # remove ["*"] later & remove comments in .env
)


@app.post("/trigger-pipeline")
async def trigger_pipeline():
   #modify 'api_url + project_id + token + ref => .env "
    url = f"https://{settings.gitlab_api_url}/api/v4/projects/{settings.gitlab_project_id}/trigger/pipeline"
    payload = {
        'token': settings.gitlab_trigger_token,
        'ref': settings.gitlab_ref
    }
    
    # Send POST request to GitLab API to trigger the pipeline
    try:
        response = requests.post(url, data=payload)
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to trigger pipeline: {str(e)}")

    if response.ok:
        return {
            "message": "Pipeline triggered successfully",
        }
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Failed to trigger pipeline: {response.text}"
        )


if __name__ == "__main__":
    import uvicorn
    
    #modify 'host + port  => .env "
    # Use host and port from .env, enable auto reload for development

    uvicorn.run(
        "main:app",
        host=settings.backend_host,
        port=settings.backend_port,
        reload=True,
    )"""