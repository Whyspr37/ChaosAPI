from fastapi import APIRouter, UploadFile, File
from utils.whisper_handler import transcribe_audio_file, stream_transcription
from utils.emotion_analysis import detect_emotion, suggest_voice_highlights

router = APIRouter()

@router.post("/voice/transcribe")
async def whisper_transcribe(file: UploadFile = File(...)):
    transcript = await transcribe_audio_file(file)
    return {"transcript": transcript}

@router.post("/voice/live_preview")
async def whisper_preview(file: UploadFile = File(...)):
    preview = await stream_transcription(file)
    return {"preview": preview}

@router.post("/voice/tone")
async def detect_tone(file: UploadFile = File(...)):
    tones = await detect_emotion(file)
    return {"tones": tones}

@router.post("/voice/highlights")
async def emotional_highlights(file: UploadFile = File(...)):
    highlights = await suggest_voice_highlights(file)
    return {"emotional_highlights": highlights}