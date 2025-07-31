import os

def rename_note(old_path, new_name):
    dir_path = os.path.dirname(old_path)
    new_path = os.path.join(dir_path, new_name)
    os.rename(old_path, new_path)
    return new_path