import os
import shutil
from copy import deepcopy
from pathlib import Path
from wx import ID_CANCEL

from .base_project_template import BaseProjectTemplate
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.common import *
from pdf_report_builder.ui.dialogs.igdi_multipart_dialog import IGDIMultipartDialog
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog


class IGDIMultipartTemplate(BaseProjectTemplate):
    def make_project(self):
        with IGDIMultipartDialog(None) as settings_dialog:
            if settings_dialog.ShowModal() == ID_CANCEL:
                return None
            self._project.settings.savepath = settings_dialog.save_location
            ret = self.populate_linkage_folder(
                settings_dialog.save_location.parent / 'Сборка',
                settings_dialog.tome_contents_template
            )
            if ret == 1:
                return None
            self.max_km = settings_dialog.max_km
            self.taps = settings_dialog.taps

            tomes = self.make_default_project_structure(settings_dialog.n_tomes)
            ver = self._project.get_current_version()
            for tome in ver.tomes:
                ver.remove_tome(tome)
            for tome in tomes:
                ver.append_tome(tome)
            
            self._update_tome_savepaths()
            self._update_code_attrs()
            self._project.settings.name = settings_dialog.save_location.stem

        return self._project
    
    def populate_linkage_folder(self, linkage_folder: Path, tome_contents_template_path: Path):
        if not (linkage_folder.exists() and linkage_folder.is_dir()):
            os.mkdir(linkage_folder)
        if not (tome_contents_template_path.exists() and tome_contents_template_path.is_file()):
            dlg = ErrorDialog(None, 'Не найден шаблон содержания тома!', 'Неправильные настройки')
            dlg.ShowModal()
            dlg.Close()
            return 1
        try:
            shutil.copy2(tome_contents_template_path, linkage_folder)
        except Exception as e:
            dlg = ErrorDialog(None, e, 'Не удалось скопировать шаблон содержания тома')
            dlg.ShowModal()
            dlg.Close()

        self.linkage_folder = linkage_folder
        self.tome_contents_template_path = linkage_folder / (tome_contents_template_path.name)
        return 0
    
    def _make_titles_umbrella(self, pdf_temp_filename: str):
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
        tome_contents_auto.doc_template = self.tome_contents_template_path
        tome_contents_auto.pdf_temp_path = self.linkage_folder / pdf_temp_filename
        docs_contents = get_element_by_name('Состав отчетной технической документации')

        titles_umbrella.add_subelement(titles_upper)
        titles_umbrella.add_subelement(titles_base)
        titles_umbrella.add_subelement(executors_list)
        titles_umbrella.add_subelement(tome_contents_auto)
        titles_umbrella.add_subelement(docs_contents)

        return deepcopy(titles_umbrella)
    
    def _make_text_tome(self):
        tome1 = Tome(
            basename='-ИГДИ1',
            human_readable_name='Том 1 - Текстовая часть',
        )
        titles_umbrella = self._make_titles_umbrella(pdf_temp_filename='Содержание_ТЧ.pdf')
        text_part = get_element_by_name('Текстовая часть')
        tome1.add_element(titles_umbrella)
        tome1.add_element(text_part)
        return tome1
    
    def _make_first_graphics_tome(self, only: bool = True):
        hr_name = 'Том 2 - Графическая часть'
        if not only:
            hr_name = hr_name + '. Книга 1'
        tome2_1 = Tome(
            basename='-ИГДИ2' if only else '-ИГДИ2.1',
            human_readable_name=hr_name
        )

        titles_umbrella_graphics = self._make_titles_umbrella(
            pdf_temp_filename='Содержание_ГЧ1.pdf'
        )
        graphics_part = get_element_by_name('Графическая часть')
        ktgi = get_element_by_name('КТГИ')
        base_net = get_element_by_name('Схема опорной сети')
        survey_net = get_element_by_name('Схема съемочной сети')
        overview_scheme = get_element_by_name('Обзорная схема')
        topoplan = get_element_by_name('Топографический план М 1:1000')
        topoplan_500 = get_element_by_name('Топографический план М 1:500')

        graphics_part.add_subelement(ktgi)
        graphics_part.add_subelement(base_net)
        graphics_part.add_subelement(survey_net)
        graphics_part.add_subelement(overview_scheme)
        graphics_part.add_subelement(topoplan)
        graphics_part.add_subelement(topoplan_500)

        if only:
            elevation_profile = get_element_by_name('Продольный профиль (основная ось)')
            graphics_part.add_subelement(elevation_profile)
        
        tome2_1.add_element(titles_umbrella_graphics)
        tome2_1.add_element(graphics_part)
        return tome2_1

    
    def _make_graphics_tome(self, i: int, n: int):
        if i == 1:
            return self._make_first_graphics_tome(n == 1)
        tome2_i = Tome(
            basename=f'-ИГДИ2.{i}',
            human_readable_name=f'Том 2 - Графическая часть. Книга {i}'
        )
        
        titles_umbrella_graphics = self._make_titles_umbrella(
            pdf_temp_filename=f'Содержание_ГЧ{i}.pdf'
        )
        graphics_part = get_element_by_name('Графическая часть')
        
        elevation_profile = get_element_by_name('Продольный профиль (основная ось)')
        graphics_part.add_subelement(elevation_profile)

        if i == n:
            for tap in self.taps:
                tap_profile = get_element_by_name('Продольный профиль (отвод)')
                tap_profile.name = f'Продольный профиль трассы газопровода (отвод {tap}) \
масштаб гор. 1:1000, верт. 1:100'
                graphics_part.add_subelement(tap_profile)
        
        tome2_i.add_element(titles_umbrella_graphics)
        tome2_i.add_element(graphics_part)
        return tome2_i


    def _update_tome_savepaths(self):
        for tome in self._project.get_current_version().tomes:
            tome.savepath = self.linkage_folder / (tome.human_readable_name + '.pdf')

    def _update_code_attrs(self):

        def update_code_attrs_recursive(el: StructuralElement, counter: int):
            if 'MAX_KM' in el.code_attr:
                code = str(el.code_attr)
                code = code.replace('MAX_KM', str(self.max_km))
                code = f'.{counter}({code.split("(")[1]}'
                el.code_attr = code
                print(1, code)
                counter += 1
            for subel in el.subelements:
                counter = update_code_attrs_recursive(subel, counter)
            return counter

        counter = 1
        for tome in self._project.get_current_version().tomes[1:]:
            print(tome.human_readable_name)
            for el in tome.structural_elements:
                counter = update_code_attrs_recursive(el, counter)
                
            

    def make_default_project_structure(self, n_tomes: int):
        tome_text = self._make_text_tome()
        tomes = [tome_text]
        for i in range(n_tomes):
            new_tome = self._make_graphics_tome(i + 1, n_tomes)
            tomes.append(new_tome)
        return tomes
    
## TODO:
# 1. Не считаются MAX_KM - он туда вообще не заходит
# 2. Для путей сохранения исключить символы типа /\
# 3. Показывать сначала диалог шаблона, а потом закрывать старый проект
# 4. shutil.SameFileError