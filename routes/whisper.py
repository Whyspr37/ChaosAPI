import requests
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()

WHISPER_PROXY_URL = "https://your-whisper-server.ngrok.io/transcribe"  # Replace with actual

@router.post("/transcribe")
async def proxy_transcribe(file: UploadFile = File(...)):
    try:
        response = requests.post(
            WHISPER_PROXY_URL,
            files={"file": (file.filename, file.file, file.content_type)},
            headers={"x-api-key": "your-secret"}  # Optional
        )
        return JSONResponse(content=response.json())
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)