from typing import NamedTuple

class ElementScheme(NamedTuple):
    name: str
    official: bool
    code_attr: str

text_report = ElementScheme(
    'Текстовая часть',
    True,
    'Т'
)

ktgi = ElementScheme(
    'Картограмма топографо-геодезической изученности, \
совмещенная со схемой выполненных работ и схемой созданной \
планово-высотной геодезической сети',
    True,
    'Г.1'
)

base_net = ElementScheme(
    'Схема созданной опорной геодезической сети',
    True,
    'Г.2'
)

survey_net = ElementScheme(
   'Схема съемочной сети',
    True,
    'Г.3'
)

overview = ElementScheme(
   'Обзорная схема',
    True,
    'Г.4'
)

topoplan = ElementScheme(
   'Топографический план',
    True,
    'Г.5'
)

profiles = ElementScheme(
   'Продольные профили по трассе проектируемого газопровода',
    True,
    'Г.6'
)
