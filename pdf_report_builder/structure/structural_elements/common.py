from typing import NamedTuple
from enum import Enum

class ElementCategory(Enum):
    OTHER = 'Другое'
    UTIL = 'Служебные'
    TEXT = 'Текстовая часть'
    GRAPHICS = 'Графическая часть'

class ElementScheme(NamedTuple):
    dialog_name: str
    element_type: ElementCategory
    name: str
    official: bool
    code_attr: str
    enumeration_include: bool = True
    enumeration_print: bool = True

element_schemes = [
    ElementScheme(
        'Другой',
        ElementCategory.OTHER,
        'Структурный элемент',
        False,
        ''
    ),

    ElementScheme(
        'Титульный лист',
        ElementCategory.UTIL,
        'Титульный лист',
        True,
        '',
        False,
        False
    ),

    ElementScheme(
        'Список исполнителей',
        ElementCategory.UTIL,
        'Список исполнителей',
        True,
        '',
        True,
        False
    ),

    ElementScheme(
        'Содержание тома',
        ElementCategory.UTIL,
        'Содержание тома',
        True,
        'С',
        True,
        False
    ),

    ElementScheme(
        'Состав отчетной технической документации',
        ElementCategory.UTIL,
        'Состав отчетной технической документации',
        True,
        'СД',
        True,
        False
    ),

    ElementScheme(
        'Текстовая часть',
        ElementCategory.TEXT,
        'Текстовая часть',
        True,
        'Т',
        True,
        False
    ),

    ElementScheme(
        'КТГИ',
        ElementCategory.GRAPHICS,
        'Картограмма топографо-геодезической изученности, \
совмещенная со схемой выполненных работ и схемой созданной \
планово-высотной геодезической сети',
        True,
        'Г.1'
    ),

    ElementScheme(
        'Схема опорной сети',
        ElementCategory.GRAPHICS,
        'Схема созданной планово-высотной опорной сети \
с указанием привязок к исходным пунктам',
        True,
        'Г.2'
    ),

    ElementScheme(
        'Схема съемочной сети',
        ElementCategory.GRAPHICS,
        'Схема съемочной геодезической сети \
с указанием привязок к исходным пунктам',
        True,
        'Г.3'
    ),

    ElementScheme(
        'Обзорная схема',
        ElementCategory.GRAPHICS,
        'Обзорная схема расположения объекта',
        True,
        'Г.4'
    ),

    ElementScheme(
        'Топографический план М 1:1000',
        ElementCategory.GRAPHICS,
        'Топографический план М 1:1000',
        True,
        'Г.5'
    ),

    ElementScheme(
        'Топографический план М 1:500',
        ElementCategory.GRAPHICS,
        'Топографический план М 1:500',
        True,
        'Г.5'
    ),

    ElementScheme(
        'Продольный профиль (основная ось)',
        ElementCategory.GRAPHICS,
        'Продольный профиль трассы газопровода (основная ось) \
масштаб гор. 1:1000, верт. 1:100',
        True,
        'Г.6'
    ),

    ElementScheme(
        'Продольный профиль (отвод)',
        ElementCategory.GRAPHICS,
        'Продольный профиль трассы газопровода (отвод ) \
масштаб гор. 1:1000, верт. 1:100',
        True,
        'Г.7'
    )
]