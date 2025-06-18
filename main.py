from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from config import settings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_SECRET_TOKEN = os.getenv("API_SECRET_TOKEN")
GITLAB_TRIGGER_TOKEN = os.getenv("GITLAB_TRIGGER_TOKEN")
GITLAB_PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")
GITLAB_REF = os.getenv("GITLAB_REF")

# Create FastAPI app
app = FastAPI()

# Enable CORS (necessary for your frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace '*' with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/trigger-pipeline")
async def trigger_pipeline(authorization: str = Header(None)):
   
    url = f"https://gitlab.com/api/v4/projects/{settings.gitlab_project_id}/trigger/pipeline"
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
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
