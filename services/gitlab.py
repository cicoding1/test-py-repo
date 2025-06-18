import requests
from config import settings

def trigger_pipeline_service():
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
        # raise an exception to be caught in routes for HTTP error response
        raise Exception(f"Failed to trigger pipeline: {str(e)}")

    if response.ok:
        return "Pipeline triggered successfully"
    else:
        raise Exception(f"Failed to trigger pipeline: {response.text}")
