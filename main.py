from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from config import settings
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
GITLAB_TRIGGER_TOKEN = os.getenv("GITLAB_TRIGGER_TOKEN")
GITLAB_PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")
GITLAB_REF = os.getenv("GITLAB_REF")

# Create FastAPI app
app = FastAPI()

# Enable CORS 

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
    uvicorn.run(
        "main:app",
        host=settings.backend_host,
        port=settings.backend_port,
        reload=True,
    )