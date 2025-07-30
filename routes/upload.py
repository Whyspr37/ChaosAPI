
from fastapi import APIRouter, UploadFile, File
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR = "notes"

@router.post("/")
async def upload_note(file: UploadFile = File(...)):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_location = os.path.join(UPLOAD_DIR, f"{timestamp}_{file.filename}")
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "stored_as": file_location}
