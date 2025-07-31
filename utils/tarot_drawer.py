import random

def draw_tarot(highlights, cards=3):
    return random.sample(highlights, min(cards, len(highlights)))