from copy import deepcopy

from .tome import Tome
from .structural_elements.common import *

def make_default_project_structure():
    titles_umbrella = StructuralElement(
        "Шапка",
        enumeration_include=False,
        enumeration_print=False,
        create_bookmark=False,
        expanded=True,
        inner_enumeration=False
    )
    titles_upper = StructuralElement(
        "Титульники вышестоящих",
        enumeration_include=False,
        enumeration_print=False,
        create_bookmark=False,
        inner_enumeration=False
    )
    titles_base = get_element_by_name('Титульный лист')
    executors_list = get_element_by_name('Список исполнителей')
    tome_contents_auto = get_element_by_name('Содержание тома (автосбор)')
    docs_contents = get_element_by_name('Состав отчетной технической документации')

    titles_umbrella.add_subelement(titles_upper)
    titles_umbrella.add_subelement(titles_base)
    titles_umbrella.add_subelement(executors_list)
    titles_umbrella.add_subelement(tome_contents_auto)
    titles_umbrella.add_subelement(docs_contents)

    text_part = get_element_by_name('Текстовая часть')

    tome1 = Tome(
        basename='-ИГДИ1',
        human_readable_name='Том 1 - Текстовая часть'
    )
    tome1.add_element(titles_umbrella)
    tome1.add_element(text_part)


    titles_umbrella_graphics = deepcopy(titles_umbrella)
    graphics_part = get_element_by_name('Графическая часть')

    ktgi = get_element_by_name('КТГИ')
    base_net = get_element_by_name('Схема опорной сети')
    survey_net = get_element_by_name('Схема съемочной сети')
    overview_scheme = get_element_by_name('Обзорная схема')
    topoplan = get_element_by_name('Топографический план М 1:1000')
    topoplan_500 = get_element_by_name('Топографический план М 1:500')
    elevation_profile = get_element_by_name('Продольный профиль (основная ось)')

    graphics_part.add_subelement(ktgi)
    graphics_part.add_subelement(base_net)
    graphics_part.add_subelement(survey_net)
    graphics_part.add_subelement(overview_scheme)
    graphics_part.add_subelement(topoplan)
    graphics_part.add_subelement(topoplan_500)
    graphics_part.add_subelement(elevation_profile)

    tome2 = Tome(
        basename='-ИГДИ2',
        human_readable_name='Том 2 - Графическая часть'
    )
    tome2.add_element(titles_umbrella_graphics)
    tome2.add_element(graphics_part)

    return [tome1, tome2]