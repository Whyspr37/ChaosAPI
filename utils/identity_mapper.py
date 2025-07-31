def map_identities(notes):
    themes = ['survivor', 'queer', 'creator', 'child', 'orphan']
    found = {theme: [] for theme in themes}
    for note in notes:
        for theme in themes:
            if theme in note:
                found[theme].append(note)
    return found