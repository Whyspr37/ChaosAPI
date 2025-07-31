import shutil
import os
from datetime import datetime

def perform_backup(source_dir='notes', backup_dir='backups'):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_name = f"{backup_dir}/notes_backup_{timestamp}.zip"
    shutil.make_archive(zip_name.replace('.zip',''), 'zip', source_dir)
    return zip_name