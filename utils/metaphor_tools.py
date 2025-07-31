def suggest_metaphor(feeling):
    examples = {
        'grief': 'a stone sinking in molasses',
        'rage': 'a wildfire under ice',
        'joy': 'sunlight through cracked glass'
    }
    return examples.get(feeling.lower(), "a feeling with no form")