from typing import NamedTuple
from enum import Enum
from .base import StructuralElement

class ElementCategory(Enum):
    OTHER = 'Другое'
    UTIL = 'Служебные'
    TEXT = 'Текстовая часть'
    GRAPHICS = 'Графическая часть'

class ElementScheme(NamedTuple):
    dialog_name: str
    element_type: ElementCategory
    element: StructuralElement

element_schemes = [
    ElementScheme(
        'Другой',
        ElementCategory.OTHER,
        StructuralElement(
            name='Структурный элемент',
            code_attr = ''
        )
    ),

    ElementScheme(
        'Титульный лист',
        ElementCategory.UTIL,
        StructuralElement(
            name='Титульный лист',
            enumeration_include=False,
            enumeration_print=False,
            create_bookmark=True
        )
    ),

    ElementScheme(
        'Список исполнителей',
        ElementCategory.UTIL,
        StructuralElement(
            name='Список исполнителей',
            enumeration_include=True,
            enumeration_print=False,
            create_bookmark=True
        )
    ),

    ElementScheme(
        'Содержание тома',
        ElementCategory.UTIL,
        StructuralElement(
            name='Содержание тома',
            code_attr='.С',
            enumeration_include=True,
            enumeration_print=False,
            create_bookmark=True
        )
    ),

    ElementScheme(
        'Состав отчетной технической документации',
        ElementCategory.UTIL,
        StructuralElement(
            name='Состав отчетной технической документации',
            code_attr='.СД',
            enumeration_include=True,
            enumeration_print=False,
            create_bookmark=True
        )
    ),

    ElementScheme(
        'Текстовая часть',
        ElementCategory.TEXT,
        StructuralElement(
            name='Текстовая часть',
            code_attr='.Т',
            enumeration_include=True,
            enumeration_print=False,
            create_bookmark=True
        )
    ),

    ElementScheme(
        'КТГИ',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Картограмма топографо-геодезической изученности, \
совмещенная со схемой выполненных работ и схемой созданной \
планово-высотной геодезической сети',
            code_attr='.1',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Схема опорной сети',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Схема созданной планово-высотной опорной сети \
с указанием привязок к исходным пунктам',
            code_attr='.2',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Схема съемочной сети',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Схема съемочной геодезической сети \
с указанием привязок к исходным пунктам',
            code_attr='.3',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Обзорная схема',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Обзорная схема расположения объекта',
            code_attr='.4',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Топографический план М 1:1000',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Топографический план М 1:1000',
            code_attr='.5',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Топографический план М 1:500',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Топографический план М 1:500',
            code_attr='.6',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True
        )
    ),

    ElementScheme(
        'Продольный профиль (основная ось)',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Продольный профиль трассы газопровода (основная ось) \
масштаб гор. 1:1000, верт. 1:100',
            code_attr='.6',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True,
            inner_enumeration=True
        )
    ),

    ElementScheme(
        'Продольный профиль (отвод)',
        ElementCategory.GRAPHICS,
        StructuralElement(
            name='Продольный профиль трассы газопровода (отвод ) \
масштаб гор. 1:1000, верт. 1:100',
            code_attr='.7',
            enumeration_include=True,
            enumeration_print=True,
            create_bookmark=True,
            code_add=True,
            inner_enumeration=True
        )
    )
]