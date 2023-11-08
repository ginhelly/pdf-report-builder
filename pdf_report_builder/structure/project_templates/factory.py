from .base_project_template import BaseProjectTemplate
from .igdi_multipart import IGDIMultipartTemplate

PROJECT_TEMPLATES = {
    "ИГДИ - несколько томов": IGDIMultipartTemplate
}

def make_project(template: BaseProjectTemplate | str):
    if isinstance(template, str):
        template = PROJECT_TEMPLATES[template]
    project = template().make_project()
    if project is None:
        raise ValueError('Failed to create a project')
    return project
