from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
import os
from docx import Document
import zipfile

router = APIRouter()

UPLOAD_DIR = "uploaded_notes"
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

def convert_to_docx(text, output_path):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_path)

def convert_and_export(file_path, export_format):
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    export_path = os.path.join(EXPORT_DIR, f"{base_name}.{export_format}")

    if export_format == "txt":
        with open(export_path, "w", encoding="utf-8") as out:
            out.write(content)
    elif export_format == "md":
        with open(export_path, "w", encoding="utf-8") as out:
            out.write(content)
    elif export_format == "docx":
        convert_to_docx(content, export_path)
    else:
        raise ValueError("Unsupported format")

    return export_path

@router.get("/export_note")
def export_note(filename: str = Query(...), format: str = Query("txt")):
    note_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.isfile(note_path):
        raise HTTPException(status_code=404, detail="Note not found")

    try:
        export_path = convert_and_export(note_path, format)
        return FileResponse(export_path, filename=os.path.basename(export_path))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Export failed: {str(e)}")

@router.get("/export_project")
def export_project(project: str = Query(...), format: str = Query("txt")):
    project_path = os.path.join(UPLOAD_DIR, project)
    if not os.path.isdir(project_path):
        raise HTTPException(status_code=404, detail="Project folder not found")

    temp_export_dir = os.path.join(EXPORT_DIR, f"{project}_{format}")
    os.makedirs(temp_export_dir, exist_ok=True)

    exported_files = []
    for filename in os.listdir(project_path):
        full_path = os.path.join(project_path, filename)
        if os.path.isfile(full_path):
            try:
                out_path = convert_and_export(full_path, format)
                shutil.copy(out_path, temp_export_dir)
                exported_files.append(out_path)
            except Exception:
                continue

    zip_path = os.path.join(EXPORT_DIR, f"{project}_{format}.zip")
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in os.listdir(temp_export_dir):
            zipf.write(os.path.join(temp_export_dir, file), arcname=file)

    return FileResponse(zip_path, filename=os.path.basename(zip_path))
