import os
import json
import random

def load_highlights():
    path = "data/highlights.json"
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_zine_structure(tag=None):
    highlights = load_highlights()

    if tag:
        tagged = [h for h in highlights if tag.lower() in [t.lower() for t in h.get("tags", [])]]
    else:
        tagged = highlights

    if not tagged:
        return {"error": "No matching highlights found."}

    pages = []
    selected = random.sample(tagged, min(6, len(tagged)))

    for idx, h in enumerate(selected):
        layout = {
            "page": idx + 1,
            "title": f"Page {idx + 1} – {tag.title() if tag else 'Zine'}",
            "quote": h.get("text", ""),
            "tags": h.get("tags", []),
            "source": h.get("source", ""),
            "layout_style": random.choice(["centered", "diagonal", "block", "polaroid", "spiral"]),
            "image_placeholder": f"img_placeholder_{idx+1}.png"
        }
        pages.append(layout)

    return {
        "theme": tag or "Unthemed",
        "total_pages": len(pages),
        "pages": pages
    }
