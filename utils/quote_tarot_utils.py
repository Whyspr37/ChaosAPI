import random
import json
import os

HIGHLIGHTS_FILE = "data/highlights.json"

DEFAULT_POSITIONS = ["Past", "Present", "Future"]

def draw_tarot_quotes(theme: str = None):
    if not os.path.exists(HIGHLIGHTS_FILE):
        return {"error": "No highlights file found."}

    with open(HIGHLIGHTS_FILE, "r", encoding="utf-8") as f:
        highlights = json.load(f)

    if theme:
        filtered = [h for h in highlights if theme.lower() in [t.lower() for t in h.get("tags", [])]]
    else:
        filtered = highlights

    if len(filtered) < 3:
        return {"error": "Not enough quotes available for a full draw."}

    draw = random.sample(filtered, 3)

    result = []
    for i, quote in enumerate(draw):
        result.append({
            "position": DEFAULT_POSITIONS[i],
            "quote": quote.get("text", ""),
            "source": quote.get("source", "Unknown"),
            "tags": quote.get("tags", [])
        })

    return {
        "theme": theme if theme else "Random",
        "draw": result,
        "instructions": "Reflect on each quote in the context of its position: Past / Present / Future."
    }
