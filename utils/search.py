def search_archive(query, notes):
    return [note for note in notes if query.lower() in note.lower()]