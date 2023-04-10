from .base import StructuralElement
from .common import *

ELEMENTS_BY_SCHEME = {i: [] for i in ElementCategory}
for scheme in element_schemes:
    ELEMENTS_BY_SCHEME[scheme.element_type].append(scheme)

def filter_schemes(elements, prompt: str):
    prompt = prompt.strip().lower()
    res = {i: [] for i in ElementCategory}
    for category in elements:
        res[category] = list(filter(
            lambda scheme: prompt in scheme.dialog_name.lower() \
                or prompt in scheme.name.lower(),
            elements[category]
        ))
        if len(res[category]) == 0:
            del res[category]
    return res