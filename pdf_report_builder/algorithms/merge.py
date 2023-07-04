from pypdf import PdfWriter

from pdf_report_builder.algorithms.bookmarks import add_bookmarks
from pdf_report_builder.algorithms.enumerate_pages import enumerate_tome
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
        tome: Tome,
        logger: ProcessingLogger,
        delta: int,
        break_on_missing: bool = True,
        with_bookmarks: bool = True,
        enumerate: bool = True,
        enumerate_start: int = 1
    ):
    files_to_merge = _collect_files_to_merge(tome)
    if len(files_to_merge) == 0:
        logger.writeline(' (!) Том не содержит входных PDF-файлов. Пропускаю')
        return
    merger = PdfWriter()
    inputs = [
        file.path for file in files_to_merge
    ]
    subsets = [
        list(file.subset) for file in files_to_merge
    ]
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
    
    if with_bookmarks and not enumerate:
        logger.writeline(' Расставляю закладки...')
        add_bookmarks(merger, tome)
        merger.page_mode = '/UseOutlines'

    savepath = tome.savepath.parent / (str(tome.savepath.name) + '.temp') if enumerate else tome.savepath
    if not enumerate:
        for page in merger.pages:
            page.compress_content_streams()
    
    with open(savepath, 'wb') as output:
        logger.writeline(' Записываю результат на диск...')
        merger.write(output)
        merger.close()
        logger.writeline(f' Успешно сформирован том {tome.human_readable_name}')
        logger.writeline(f' Путь: {tome.savepath}')
    
    enumerate_end = 0
    if enumerate:
        enumerate_end = enumerate_tome(tome, enumerate_start, logger, with_bookmarks) + 1
    print(enumerate_end)
    return enumerate_end

def merge(
        project: ReportProject,
        logger: ProcessingLogger,
        break_on_missing: bool = True,
        with_bookmarks: bool = True,
        enumerate: bool = True
    ):
    """Самое-самое главное, ради чего всё это затевалось"""
    ver = project.get_current_version()
    logger.writeline(f'Начинаю собирать набор техотчетов из версии "{ver.name}"')
    total_input_files = sum(tome.input_pdfs_number for tome in ver.tomes)
    if total_input_files == 0:
        logger.writeline('Ни один том не содержит входных файлов!\nСборка отменяется.')
        return
    delta_progress_bar = int(round(100 / total_input_files, 0))

    enumerate_counter = 1
    for tome in ver.tomes:
        if tome.use_custom_enumeration_start:
            enumerate_counter = tome.custom_enumeration_start
        logger.writeline(f' Обрабатываю том {tome.human_readable_name}')
        enumerate_counter = _merge_one_tome(tome, logger, delta_progress_bar, break_on_missing, with_bookmarks, enumerate, enumerate_counter)
        print(enumerate_counter)
        logger.writeline('')
    
    logger.writeline('Успешно завершено!')
    logger.set_progress_bar(100)