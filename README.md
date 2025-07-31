
# ChaosAPI – Phase 1 Archive System

This API serves as a creative memory and reflection archive for note-taking, voice transcription, emotional analysis, and symbolic patterning. It supports neurodivergent workflows, trauma-aware journaling, and artistic self-exploration.

---

## 🗂️ NOTE MANAGEMENT

### Upload Notes
- `POST /upload_note`: Upload a text file (auto-timestamped)
- `POST /upload_note_named`: Upload with a custom filename
- `POST /upload_audio`: Upload audio (transcribed via Whisper)

### Soft Delete
- `POST /delete_note`: Soft deletes a note (moves to `/deleted/`)
- `POST /restore_note`: Restores from deleted

### Rename Notes
- `POST /rename_note`: Rename any note

### Tagging
- `POST /add_tags`: Add manual tags
- `POST /merge_tags`: Merge messy/redundant tags
- `POST /predict_tags`: (Stub) Suggests tags by tone/theme

### Timestamped Uploads
- All uploads include auto timestamping (e.g. `20250730_103412_note.txt`)

---

## 🔍 SEARCH & NAVIGATION

### Semantic Search
- `POST /search`: Use natural language to find matching notes

### Vibe-Based Search
- e.g. “storm metaphors” or “grief”

### Memory Timeline
- `GET /memory_map`: View note history chronologically

### Reoccurrence Tracker
- `GET /reoccurrence`: Track reappearing tags/phrases

### Contradiction Finder
- `GET /contradictions`: Flags emotional or logical contradictions

### Unreliable Narrator Detector
- `GET /unreliable_narrator`: Detects euphemisms, distancing language, etc.

---

## 💬 HIGHLIGHTING & REFLECTION

### Manual Highlight Creation
- `POST /highlight_manual`: Mark powerful phrases or lines manually

### AI-Suggested Highlights
- `POST /highlight_auto`: Suggests impactful moments from content

### Unified Highlight Viewer
- `GET /highlights`: Shows all saved highlights

### One-Word Archive Summary
- `GET /archive_summary`: Returns poetic psychological archive summary

### Ritual Generator
- `POST /ritual`: Uses tag combos to build creative reflection prompts

---

## 🗃️ ORGANIZATIONAL TOOLS

### Project Folders
- `POST /create_project`: Groups notes into folders

### Storyline Tracker
- `POST /track_storyline`: Groups notes into narrative arcs

### Archetype Tagger
- `POST /tag_archetype`: Suggests symbolic identities (Oracle, Witch, Survivor)

---

## 🎙️ VOICE & EMOTION

### Whisper Transcription
- `POST /upload_audio`: Transcribes audio file via Whisper

### Real-Time Preview
- `POST /whisper_live`: Stream preview during recording (via proxy mode)

### Emotional Tone Detection
- `POST /tone_analysis`: Detects tone (e.g. rage, numbness, calm)

### Voice-Based Highlighting
- `POST /highlight_from_tone`: Flags emotional turning points in audio

---

## 📤 EXPORT & BACKUP

### Google Drive Sync
- `POST /backup_drive`: Weekly `.zip` and mirrored folder structure

### Manual or Auto Export
- `GET /export_note`: As `.txt`, `.md`, or `.docx`

---

## 🔮 CREATIVE TOOLS

### Polaroid Snapshot Mode
- `GET /snapshot`: Flash memoir scene in 50 words

### Quote Tarot
- `GET /quote_tarot`: Pull 3 reflective quotes

---

## 🧠 SELF-REFLECTION TOOLS

### Shadow Work Companion
- `POST /shadow_work`: Given theme (e.g., shame), surfaces relevant notes

### Haunt Index
- `GET /haunt_index`: Shows most repeated metaphors/themes

---

## 🛠️ SETUP

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
uvicorn main:app --reload
```

3. Access Swagger UI at:
```
http://localhost:8000/docs
```

---

## 🔐 Optional: Google & Notion Setup
- Configure OAuth and token secrets for syncing
- Add `notion_token`, `drive_token` to `.env`

---

## 🤝 Contributing
This API was built to serve memory work, neurodivergent workflows, and story reclamation. Contributions are welcome.
