from fastapi import APIRouter, Query
from typing import Optional
from utils.quote_tarot_utils import draw_tarot_quotes

router = APIRouter()

@router.get("/quote_tarot")
def quote_tarot_route(theme: Optional[str] = Query(None, description="Optional tag or theme for filtered draw")):
    """
    Draw 3 quotes from the archive as a tarot-style prompt.
    Can be random or filtered by theme/tag.
    """
    return draw_tarot_quotes(theme)
