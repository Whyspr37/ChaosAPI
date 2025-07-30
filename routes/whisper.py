
from fastapi import APIRouter, UploadFile, File
import whisper
import os

router = APIRouter()
model = whisper.load_model("base")

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(temp_path)
    os.remove(temp_path)
    return {"transcription": result["text"]}
