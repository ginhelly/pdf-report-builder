from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileDeletedEvent, \
    FileModifiedEvent, FileMovedEvent
from watchdog.observers.api import ObservedWatch

from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.files.input_pdf import PDFFile
from .singleton import Singleton


class PDFUpdateEventHandler(FileSystemEventHandler):
    def __init__(self, file_watcher):
        super().__init__()
        self.file_watcher = file_watcher

    def on_deleted(self, event):
        if not type(event) == FileDeletedEvent:
            return
        files = self.file_watcher.get_files(event.src_path)
        if len(files) == 0: return
        for file in files:
            file.on_deleted()
        EventChannel().publish('tree_update')
        EventChannel().publish('pdf_files_update')
    
    def on_modified(self, event):
        if not type(event) == FileModifiedEvent:
            return
        files = self.file_watcher.get_files(event.src_path)
        if len(files) == 0: return
        for file in files:
            file.on_modified()
        EventChannel().publish('tree_update')
        EventChannel().publish('pdf_files_update')


@dataclass
class WatchedDirectory:
    watch: ObservedWatch
    filepaths: Dict[Path, List[PDFFile]] = field(default_factory=lambda: {})


class FileWatcher(metaclass=Singleton):
    def __init__(self) -> None:
        self.dirs = {} # Dict[Path, WatchedDirectory]
        self.observer = Observer()
        self.event_handler = PDFUpdateEventHandler(self)
        self.observer.start()
    
    def add_file(self, file: PDFFile):
        parent_dir_path = file.path.parent
        if not parent_dir_path in self.dirs:
            watch = self.observer.schedule(self.event_handler, parent_dir_path)
            self.dirs[parent_dir_path] = WatchedDirectory(
                watch,
                { file.path: [ file ] }
            )
            return
        watched_dir = self.dirs[parent_dir_path]
        if not file.path in watched_dir.filepaths:
            watched_dir.filepaths[file.path] = [ file ]
            return
        watched_dir.filepaths[file.path].append(file)
        
    
    def get_files(self, path: str | Path):
        path = Path(path)
        parent_dir = path.parent
        if not parent_dir in self.dirs:
            return []
        watched_dir = self.dirs[parent_dir]
        if not path in watched_dir.filepaths:
            return []
        return watched_dir.filepaths[path]

    def update_path(self, old_path: str | Path):
        old_path = Path(old_path)
        watched_dir = self.dirs[old_path.parent]
        files = watched_dir.filepaths[old_path]
        for file in files:
            self.add_file(file)
    
    def remove_files_by_path(self, filepath: str | Path):
        filepath = Path(filepath)
        if not filepath.parent in self.dirs:
            raise ValueError('Нет такого файла')
        watched_dir = self.dirs[filepath.parent]
        if not filepath in watched_dir.filepaths:
            raise ValueError('Нет такого файла')
        watched_dir.filepaths[filepath] = []
        if len(watched_dir.filepaths) == 0:
            self.observer.unschedule(watched_dir.watch)
        return
    
    def remove_file(self, file: PDFFile):
        filepath = Path(file.path)
        if not filepath.parent in self.dirs:
            raise ValueError('Нет такого файла')
        watched_dir = self.dirs[filepath.parent]
        if not filepath in watched_dir.filepaths:
            raise ValueError('Нет такого файла')
        all_files = watched_dir.filepaths[filepath]
        try:
            all_files.remove(file)
        except ValueError:
            raise ValueError('Нет такого файла')
    
    def remove_all(self):
        self.observer.unschedule_all()
        self.dirs = {}
        
