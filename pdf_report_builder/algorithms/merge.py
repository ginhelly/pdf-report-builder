from typing import NamedTuple, List
from pypdf import PdfWriter

from pdf_report_builder.algorithms.bookmarks import add_bookmarks
from pdf_report_builder.algorithms.enumerate_pages import enumerate_tome
from pdf_report_builder.algorithms.parse_pages_count import ParseReportNode
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.utils.logger import ProcessingLogger


def _collect_files_in_subelements_recursive(el: StructuralElement) -> list:
    chain = []
    for subel in el.subelements:
        chain = chain + _collect_files_in_subelements_recursive(subel)
    chain = chain + el.files
    return chain

def _collect_files_to_merge(tome: Tome):
    files_to_merge = []
    for element in tome.structural_elements:
        files_to_merge += _collect_files_in_subelements_recursive(element)
    for file in files_to_merge:
        print(file)
    return files_to_merge

def _merge_one_tome(
        node: ParseReportNode,
        logger: ProcessingLogger,
        break_on_missing: bool = True,
        with_bookmarks: bool = True,
        enumerate: bool = True,
        enumerate_start: int = 1,
        add_codes: bool = True,
        inner_enumeration: bool = True
    ):
    tome = node.level
    files_to_merge = _collect_files_to_merge(tome)
    if len(files_to_merge) == 0:
        logger.writeline(' (!) Том не содержит входных PDF-файлов. Пропускаю')
        return
    any_text_to_add = enumerate or add_codes or inner_enumeration
    merger = PdfWriter()
    inputs = [
        file.path for file in files_to_merge
    ]
    subsets = [
        list(file.subset) for file in files_to_merge
    ]

    delta = int(100 / len(inputs))
    for obj, subset in zip(inputs, subsets):
        if not (obj.exists() and obj.is_file()):
            if break_on_missing:
                raise FileNotFoundError(f'Файл {obj.name} не найден! Процесс остановлен')
            logger.writeline(f'  (!) Файл {obj.name} не найден! Пропускаю его')
            logger.add_to_progress_bar(delta)
            continue
        if len(subset) == 0:
            merger.append(fileobj=obj, import_outline=False)
        else:
            merger.append(fileobj=obj, pages=subset, import_outline=False)
        logger.add_to_progress_bar(delta)
    
    if with_bookmarks and not any_text_to_add:
        logger.writeline(' Расставляю закладки...')
        add_bookmarks(merger, tome, logger)
        merger.page_mode = '/UseOutlines'

    savepath = tome.savepath.parent / (str(tome.savepath.name) + '.temp') if any_text_to_add else tome.savepath
    if not any_text_to_add:
        logger.writeline(' Оптимизирую объем документа...')
        logger.set_progress_bar(0)
        delta2 = int(100 / len(merger.pages))
        for page in merger.pages:
            page.compress_content_streams()
            logger.add_to_progress_bar(delta2)
    
    with open(savepath, 'wb') as output:
        logger.writeline(' Записываю результат на диск...')
        merger.write(output)
        merger.close()
        if not any_text_to_add:
            logger.writeline(f' Успешно сформирован том {tome.human_readable_name}')
            logger.writeline(f' Путь: {tome.savepath}')
    
    enumerate_end = 0
    if any_text_to_add:
        enumerate_end = enumerate_tome(node, enumerate_start, logger, with_bookmarks) + 1
    print(enumerate_end)
    return enumerate_end

def merge(
        tasks: List[ParseReportNode],
        version_name: str,
        logger: ProcessingLogger,
        break_on_missing: bool = True,
        with_bookmarks: bool = True,
        enumerate: bool = True,
        add_codes: bool = True,
        inner_enumeration: bool = True
    ):
    """Самое-самое главное, ради чего всё это затевалось"""
    if len(tasks) == 0:
        logger.writeline('Ни один том не поступил на сборку.\nСборка отменяется.')
        return
    logger.writeline(f'Начинаю собирать набор техотчетов из версии "{version_name}"')
    tomes = [task.level for task in tasks]
    total_input_files = sum(tome.input_pdfs_number for tome in tomes)
    if total_input_files == 0:
        logger.writeline('Ни один том не содержит входных файлов!\nСборка отменяется.')
        return
    
    for node in tasks:
        logger.writeline(f' Обрабатываю том {node.level.human_readable_name}')
        enum_start = node.current_page_number \
            if not node.level.use_custom_enumeration_start \
            else node.level.custom_enumeration_start
        _merge_one_tome(
            node,
            logger,
            break_on_missing,
            with_bookmarks,
            enumerate,
            enum_start,
            add_codes,
            inner_enumeration
        )
        logger.writeline('')
    
    logger.writeline('Успешно завершено!')
    logger.set_progress_bar(100)