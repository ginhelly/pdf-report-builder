import os
from pathlib import Path


class FileLockedError(Exception):
    pass

def get_lock_path(path: Path):
    return path.parent / (path.stem + '.reportprj_lock')

def create_lock_file(path: Path):
    lock_path = get_lock_path(path)
    try:
        with open(lock_path, "x+") as file:
            file.write(os.getlogin())
        os.system(f"attrib +h {lock_path}")
    except FileExistsError:
        with open(lock_path, 'r') as lock:
            user = lock.readline()
        raise FileLockedError(f"Файл заблокирован пользователем {user}")