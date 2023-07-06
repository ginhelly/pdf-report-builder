from typing import NamedTuple, Callable

#import fitz
import io
import os
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

from .parse_pages_count import ParseReportNode, NodeType
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.utils.logger import ProcessingLogger
from pdf_report_builder.algorithms.bookmarks import add_bookmarks

class StructuralChunk(NamedTuple):
    pages_number: int
    enumeration_include: bool
    enumeration_print: bool
    code_add: bool
    code: str

class PageParams(NamedTuple):
    index: int
    enumeration_include: bool
    enumeration_print: bool
    code_add: bool
    code: str

def collect_chunks_recursively(node: ParseReportNode):
    res = []
    subelement_nodes = [child for child in node.children if child.type == NodeType.ELEMENT]
    for subel in subelement_nodes:
        add = collect_chunks_recursively(subel)
        res = res + add
    if len(node.level.files) > 0:
        chunk = StructuralChunk(
            node.level.pages_number,
            node.level.enumeration_include,
            node.level.enumeration_print,
            node.level.code_add,
            node.code
        )
        #print(f'CHUNK={chunk}; EL={el}')
        res.append(chunk)
    return res


class PageEnumerator:
    def __init__(self, node: ParseReportNode, start: int = 1):
        self.tome = node.level
        self.node = node
        self.counter = start
        chunks = []
        for child in self.node.children:
            add = collect_chunks_recursively(child)
            chunks = chunks + add
        for c in chunks:
            print(c)
        self.chunks = chunks
        self.left = 0

    def __iter__(self):
        return self
    
    def _change_chunk(self):
        if len(self.chunks) == 0:
            raise StopIteration
        self.current_chunk = self.chunks[0]
        self.chunks = self.chunks[1:]
        self.left = self.current_chunk.pages_number
    
    def __next__(self) -> PageParams:
        if self.left == 0:
            self._change_chunk()
        self.left -= 1
        if self.current_chunk.enumeration_include:
            self.counter += 1
        return PageParams(
            self.counter - 1,
            self.current_chunk.enumeration_include,
            self.current_chunk.enumeration_print,
            self.current_chunk.code_add,
            self.current_chunk.code
        )


class TextParams(NamedTuple):
    text: str
    coords_function: Callable[[float, float], tuple[float]]


def add_text_to_page_pypdf(page, text_params: list[TextParams]):
    if len(text_params) == 0:
        return

    # Создаем холст reportlab (одновременно создается макет страницы)
    packet = io.BytesIO()
    dimensions = (page.mediabox.width, page.mediabox.height)
    can = canvas.Canvas(packet, dimensions)
    can.setFont('GOST2304A', 14)

    # Сдвигаем холст относительно макета
    if page.rotation == 90:
        translate_params = (page.mediabox.width, 0)
    elif page.rotation == 180:
        translate_params = (page.mediabox.width, page.mediabox.height)
    elif page.rotation == 270:
        translate_params = (0, page.mediabox.height)
    else:
        translate_params = (0, 0)
    can.translate(*translate_params)

    # Поворачиваем весь холст отн. его левого нижнего угла на угол поворота страницы (чтобы были повернуты символы)
    can.rotate(page.rotation)

    # Считаем реальные ширину и высоту (т.е. какие они будут отображаться в просмотрщике)
    true_width = page.mediabox.height if page.rotation % 180 == 90 else page.mediabox.width
    true_height = page.mediabox.width if page.rotation % 180 == 90 else page.mediabox.height

    # Рисуем всю фигню
    for text_param in text_params:
        x, y = text_param.coords_function(true_width, true_height)
        can.drawCentredString(x, y, text_param.text)

    # Сохраняем полученную PDF-ку в память
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Поворачиваем весь лист согласно углу поворота страницы, чтобы они совпадали
    new_pdf.pages[0].rotate(page.rotation)

    # Вливаем в исходную PDF-страницу нашу новую с нашим контентом
    page.merge_page(new_pdf.pages[0])
    
def enumerate_tome(node: ParseReportNode, start: int, logger: ProcessingLogger, with_bookmarks: bool = True):
    tome = node.level
    path = tome.savepath.parent / (str(tome.savepath.name) + '.temp') 
    if not (path.exists() and path.is_file()):
        raise FileNotFoundError()
    
    #doc = fitz.open(tome.savepath)
    doc = PdfReader(path)
    enumerator = PageEnumerator(node, start)
    to_return = start
    page_in_document = 0
    output = PdfWriter()

    logger.set_progress_bar(0)
    logger.writeline(' Расставляю нумерацию страниц...')
    delta = int(100 / len(doc.pages))

    gost = Path(os.getcwd()) / 'pdf_report_builder' / 'data' / 'GOST2304_TypeA.ttf'
    pdfmetrics.registerFont(TTFont('GOST2304A', gost))

    for page_params in enumerator:
        to_return = page_params.index
        print(page_params)
        page_in_document += 1
        page = doc.pages[page_in_document - 1] # doc[0]
        all_texts = []
        if page_params.enumeration_include and page_params.enumeration_print:
            enum_params = TextParams(
                str(page_params.index),
                lambda true_width, true_height: (true_width - 29, true_height - 29)
            )
            all_texts.append(enum_params)
        if page_params.code_add:
            all_texts.append(TextParams(
                page_params.code,
                lambda true_width, true_height: (true_width - 180, 152)
            ))
        add_text_to_page_pypdf(page, all_texts)
        output.add_page(page)
        logger.add_to_progress_bar(delta)
    
    if with_bookmarks:
        logger.writeline(' Расставляю закладки...')
        add_bookmarks(output, tome, logger)
        output.page_mode = '/UseOutlines'
    
    logger.writeline(' Оптимизирую объем документа...')
    logger.set_progress_bar(0)
    delta2 = int(100 / len(output.pages))
    for page in output.pages:
        page.compress_content_streams()
        logger.add_to_progress_bar(delta2)
    
    logger.writeline('Сохраняю результат...')
    #doc.save(tome.savepath, incremental=True, encryption=0)
    with open(tome.savepath, 'wb+') as output_file:
        output.write(output_file)
    os.remove(path)
    logger.writeline(f' Успешно сформирован том {tome.human_readable_name}')
    logger.writeline(f' Путь: {tome.savepath}')
    return to_return