from fastapi import APIRouter, HTTPException
from services.gitlab import trigger_pipeline_service

router = APIRouter()

@router.post("/trigger-pipeline")
async def trigger_pipeline():
    # Call the service function to trigger pipeline
    try:
        message = trigger_pipeline_service()
        return {
            "message": message,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
