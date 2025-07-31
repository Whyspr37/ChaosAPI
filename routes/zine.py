from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional
import random

router = APIRouter()

# Placeholder highlights
demo_highlights = [
    "I survived things no one saw.",
    "Grief speaks in echoes.",
    "I was taught to vanish before I learned to speak.",
    "Shame isn't mine, but I carried it like it was.",
    "This body is still here — that's the rebellion."
]

class ZinePage(BaseModel):
    title: str
    content: str
    layout_hint: Optional[str] = None

@router.get("/zine_scaffold", response_model=List[ZinePage])
def generate_zine_scaffold(theme: str = Query("Survival")):
    page_titles = [
        f"{theme.upper()} — TITLE PAGE",
        "Fragment 1",
        "Fragment 2",
        "Poetic Disruption",
        "Closing Page"
    ]

    layout_hints = ["quote-center", "two-column", "image-overlay", "handwritten-style", "blackout-poem"]

    pages = []
    for title in page_titles:
        pages.append(ZinePage(
            title=title,
            content=random.choice(demo_highlights),
            layout_hint=random.choice(layout_hints)
        ))

    return pages
