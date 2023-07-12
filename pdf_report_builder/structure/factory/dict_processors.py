from pathlib import Path
from typing import List
from pdf_report_builder.project.storage_settings import SettingsStorage

class DictProcessor:
    def __init__(self, d: dict):
        self.d = d
        self.valid_keys = []
    
    def remove_invalid_keys(self, valid_keys: List[str] | None = None):
        """
        Удаляет из словаря все ключи, которых нет в списке.
        Если список не предоставлен, используются
        отработанные ранее ключи
        """
        if valid_keys is None:
            valid_keys = self.valid_keys
        for key in list(self.d.keys()):
            if not key in valid_keys:
                del self.d[key]
        return self
        
    def parse_path(self, key: str):
        """Заменяет внутри словаря d значение по ключу key объектом pathlib.Path"""
        self.valid_keys.append(key)
        if key in self.d:
            if SettingsStorage().settings.paths_relative:
                self.d[key] = SettingsStorage().settings.savepath.parent / self.d[key]
            self.d[key] = Path(self.d[key])
        return self

    def parse_boolean(self, key: str, default: bool):
        """
        Заменяет внутри словаря d строковое значение 'True' или 'False'
        по ключу key на корректное булево значение.
        Если ключа нет в словаре, то используется значение default
        """
        self.valid_keys.append(key)
        if not key in self.d or self.d[key] == str(default):
            self.d[key] = default
            return self.d
        self.d[key] = not default
        return self

    def parse_levels_list(self, key: str, callback: callable):
        """
        Для каждого элемента в списке d[key] вызывает callback,
        который должен генерировать новый уровень структуры,
        и перезаписывает d[key] на список распарсенных элементов
        """
        self.valid_keys.append(key)
        if key in self.d:
            parsed_levels = []
            for level_dict in self.d[key]:
                new_level = callback(level_dict)
                parsed_levels.append(new_level)
            self.d[key] = parsed_levels
        else:
            self.d[key] = []
        return self

    def parse_level(self, key: str, callback: callable, default):
        """
        Берет элемент d[key], применяет к нему callback
        и перезаписывает. Если ключа нет, записывает default
        """
        self.valid_keys.append(key)
        if key in self.d:
            self.d[key] = callback(self.d[key])
        else:
            self.d[key] = default
        return self