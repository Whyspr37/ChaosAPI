def extract_highlights(text):
    # Mock: return any sentence over 100 characters as a 'highlight'
    return [line.strip() for line in text.split('.') if len(line) > 100]