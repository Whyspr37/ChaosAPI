
from fastapi import APIRouter, UploadFile, File
import os
import whisper
from tempfile import NamedTemporaryFile

router = APIRouter()

# Load the Whisper model (base, small, medium, large — choose based on performance needs)
model = whisper.load_model("base")


@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save uploaded file to a temporary location
    with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_audio.write(await file.read())
        temp_path = temp_audio.name

    # Transcribe with Whisper
    try:
        result = model.transcribe(temp_path)
    finally:
        os.remove(temp_path)  # Clean up

    return {
        "transcription": result.get("text", ""),
        "language": result.get("language", "unknown")
    }