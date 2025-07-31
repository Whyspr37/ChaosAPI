def detect_emotion(text):
    # Simple keyword-based mock logic
    if "angry" in text or "rage" in text:
        return "rage"
    elif "numb" in text:
        return "numbness"
    elif "peace" in text or "calm" in text:
        return "calm"
    return "neutral"