import os
import shutil
from datetime import datetime

def save_note(content, filename, notes_dir='notes'):
    os.makedirs(notes_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    path = os.path.join(notes_dir, f"{timestamp}_{filename}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return path

def delete_note(filename, notes_dir='notes', deleted_dir='deleted'):
    os.makedirs(deleted_dir, exist_ok=True)
    src = os.path.join(notes_dir, filename)
    dst = os.path.join(deleted_dir, filename)
    shutil.move(src, dst)
    return dst

def restore_note(filename, notes_dir='notes', deleted_dir='deleted'):
    src = os.path.join(deleted_dir, filename)
    dst = os.path.join(notes_dir, filename)
    shutil.move(src, dst)
    return dst