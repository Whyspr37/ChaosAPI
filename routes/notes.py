from fastapi import APIRouter, UploadFile, File, Form
from utils.note_handler import save_note, restore_note, delete_note, rename_note
from utils.file_manager import timestamp_filename
from typing import Optional

router = APIRouter()

@router.post("/upload_note")
async def upload_note(file: UploadFile = File(...), project: Optional[str] = Form(None)):
    filename = await timestamp_filename(file.filename)
    result = await save_note(file, filename, project)
    return {"status": "success", "filename": filename, "project": project, "details": result}

@router.post("/rename_note")
def rename_note_endpoint(original_name: str = Form(...), new_name: str = Form(...)):
    success = rename_note(original_name, new_name)
    return {"status": "renamed" if success else "error", "from": original_name, "to": new_name}

@router.post("/delete_note")
def delete_note_endpoint(filename: str = Form(...)):
    success = delete_note(filename)
    return {"status": "deleted" if success else "error", "filename": filename}

@router.post("/restore_note")
def restore_note_endpoint(filename: str = Form(...)):
    success = restore_note(filename)
    return {"status": "restored" if success else "error", "filename": filename}