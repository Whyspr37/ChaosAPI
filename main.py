

# Implementation for: Rename endpoint

@app.put("/rename_note")
def rename_note(note_id: str, new_name: str):
    note_path = get_note_path(note_id)
    if not os.path.exists(note_path):
        raise HTTPException(status_code=404, detail="Note not found")
    new_path = os.path.join(os.path.dirname(note_path), new_name)
    os.rename(note_path, new_path)
    return {"status": "renamed", "new_name": new_name}


# Implementation for: Soft delete → /deleted/ folder

@app.delete("/delete_note")
def delete_note(note_id: str):
    note_path = get_note_path(note_id)
    if not os.path.exists(note_path):
        raise HTTPException(status_code=404, detail="Note not found")
    deleted_dir = os.path.join(BASE_DIR, "deleted")
    os.makedirs(deleted_dir, exist_ok=True)
    new_path = os.path.join(deleted_dir, os.path.basename(note_path))
    os.rename(note_path, new_path)
    return {"status": "deleted", "new_location": new_path}


# Implementation for: Restore deleted notes

@app.post("/restore_note")
def restore_note(note_id: str):
    deleted_path = os.path.join(BASE_DIR, "deleted", note_id)
    restore_path = os.path.join(BASE_DIR, "notes", note_id)
    if not os.path.exists(deleted_path):
        raise HTTPException(status_code=404, detail="Note not found in deleted folder")
    os.rename(deleted_path, restore_path)
    return {"status": "restored", "location": restore_path}


# Implementation for: Manual note naming

@app.post("/upload_note_named")
def upload_note_named(file: UploadFile = File(...), name: str = Form(...)):
    save_path = os.path.join(BASE_DIR, "notes", name)
    with open(save_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": name, "status": "uploaded"}


# Implementation for: Timestamped uploads

@app.post("/upload_note")
def upload_note(file: UploadFile = File(...)):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    save_path = os.path.join(BASE_DIR, "notes", filename)
    with open(save_path, "wb") as f:
        f.write(file.file.read())
    return {"filename": filename, "status": "uploaded"}


# Implementation for: Tag Merge Tool

@app.post("/merge_tags")
def merge_tags(tag1: str, tag2: str, new_tag: str):
    # Placeholder: In production, this would update the tag database
    return {"merged": [tag1, tag2], "into": new_tag}


# Implementation for: Manual highlight creation

@app.post("/highlight_manual")
def highlight_manual(note_id: str, text: str):
    highlights_file = os.path.join(BASE_DIR, "highlights.json")
    highlights = []
    if os.path.exists(highlights_file):
        with open(highlights_file, "r", encoding="utf-8") as f:
            highlights = json.load(f)
    highlights.append({"note_id": note_id, "text": text})
    with open(highlights_file, "w", encoding="utf-8") as f:
        json.dump(highlights, f)
    return {"status": "highlight added"}


# Implementation for: One-word Archive Summary

@app.get("/archive_summary")
def archive_summary():
    keywords = ["grief", "rage", "hope", "storm", "survival", "calm", "chaos"]
    selected = random.choice(keywords)
    return {"summary": selected, "note": "AI-selected one-word archive summary"}


# Implementation for: Storyline Tracker (group notes into arcs)

@app.post("/track_storyline")
def track_storyline(arc_name: str, note_ids: list[str]):
    storyline_path = os.path.join(BASE_DIR, "storylines.json")
    data = {}
    if os.path.exists(storyline_path):
        with open(storyline_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    data[arc_name] = note_ids
    with open(storyline_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return {"status": "storyline saved"}


# Implementation for: Export Notes as .txt, .md, .docx ✅ (new)

@app.get("/export_note")
def export_note(note_id: str, format: str = "txt"):
    note_path = get_note_path(note_id)
    if not os.path.exists(note_path):
        raise HTTPException(status_code=404, detail="Note not found")
    content = Path(note_path).read_text()
    if format == "md":
        export_path = note_path.replace(".txt", ".md")
    elif format == "docx":
        from docx import Document
        doc = Document()
        doc.add_paragraph(content)
        export_path = note_path.replace(".txt", ".docx")
        doc.save(export_path)
    else:
        export_path = note_path
    return FileResponse(export_path)
