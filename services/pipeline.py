from fastapi import APIRouter, HTTPException
from services.gitlab import trigger_pipeline_service
from pydantic import BaseModel
from typing import Dict


router = APIRouter()
class PipelineTriggerRequest(BaseModel):
    variables: Dict[str, str]




@router.post("/trigger-pipeline")
async def trigger_pipeline(data: PipelineTriggerRequest):
    # Call the service function to trigger pipeline
    try:
        message = trigger_pipeline_service(data.variables)
        print("Service response:", message)       # Debug log

        return {
            "message": message,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
