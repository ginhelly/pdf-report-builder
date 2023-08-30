import json
import os
from bisect import bisect_right
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.utils.singleton import Singleton
from pdf_report_builder.utils.app_settings import AppSettings

PAPER_FORMATS_PATH = AppSettings.get('DATA_PATH') / 'paper_formats.json'
THRESHOLD = 20

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

class PaperFormat(NamedTuple):
    width: float
    height: float
    name: str
    multiple_of_a4: float


class PaperFormatStorage(metaclass=Singleton):
    def __init__(self) -> None:
        # Читаем все форматы бумаги из файла
        self._formats = []
        if not (
            PAPER_FORMATS_PATH.exists() and
            PAPER_FORMATS_PATH.is_file()):
            raise FileNotFoundError('Не найден файл с описанием форматов листов')
        with open(PAPER_FORMATS_PATH, encoding='utf-8') as f:
            read_formats = json.load(f)
        for format in read_formats['formats']:
            self._formats.append(PaperFormat(
                width=format['width'],
                height=format['height'],
                name=format['name'],
                multiple_of_a4=float(format['multiple_of_a4'])
            ))
        
        # Сортируем по ширине и по высоте
        self._formats_width = sorted(self._formats, key=lambda format: format.width)

        # Формируем словарик для просмотра
        self._formats_dict = {
            format.name.lower(): format
            for format in self._formats
        }
    
    def find_format_by_name(self, name: str) -> PaperFormat:
        return self._formats_dict[name.lower()]

    def find_format_by_size(self, width: float, height: float) -> PaperFormat:
        # Если значения выходят за рамки формата листа не более, чем на THRESHOLD, сдвигаем вниз
        # Чтобы для листа размерами 211*298 выдавало А4, а не что-то большее
        width = width - THRESHOLD
        height = height - THRESHOLD

        # Ищем подмассив, начинающийся с самого маленького числа, большего данной ширины
        width_subset_start = bisect_right(
            self._formats_width,
            width,
            key=lambda format: format.width
        )
        subset_by_width = self._formats_width[width_subset_start:]
        #print(f' subset_by_width: {subset_by_width}')
        if len(subset_by_width) == 0:
            return self._formats_width[-1]
        
        # Сортируем подмассив по полупериметрам
        subset_by_width_sorted = sorted(
            subset_by_width,
            key=lambda format: format.height
        )
        #print(f' subset_by_width_sorted: {subset_by_width_sorted}')

        # Ищем в подмассиве новый подмассив, у которого высота больше заданной
        height_subset_start = bisect_right(
            subset_by_width_sorted,
            height,
            key=lambda format: format.height
        )
        subset_by_height = subset_by_width_sorted[height_subset_start:]
        #print(f' subset_by_height: {subset_by_height}')
        if len(subset_by_height) == 0:
            return subset_by_width_sorted[-1]
        
        return subset_by_height[0]
        

#from pdf_report_builder.paperformats.format import *