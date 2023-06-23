from typing import NamedTuple, Callable

#import fitz
import io
import os
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter

from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.utils.logger import ProcessingLogger
from pdf_report_builder.algorithms.bookmarks import add_bookmarks

class StructuralChunk(NamedTuple):
    pages_number: int
    enumeration_include: bool
    enumeration_print: bool

def collect_chunks_recursively(el: StructuralElement):
    res = []
    for subel in el.subelements:
        add = collect_chunks_recursively(subel)
        res = res + add
    if len(el.files) > 0:
        chunk = StructuralChunk(
            el.pages_number,
            el.enumeration_include,
            el.enumeration_print
        )
        #print(f'CHUNK={chunk}; EL={el}')
        res.append(chunk)
    return res


class PageEnumerator:
    def __init__(self, tome: Tome, start: int = 1):
        self.tome = tome
        self.counter = start
        chunks = []
        for el in tome.structural_elements:
            add = collect_chunks_recursively(el)
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
    
    def __next__(self):
        if self.left == 0:
            self._change_chunk()
        self.left -= 1
        if self.current_chunk.enumeration_include:
            self.counter += 1
        return (self.counter - 1, self.current_chunk.enumeration_include, self.current_chunk.enumeration_print)


class TextParams(NamedTuple):
    text: str
    coords_function: Callable[[float, float], tuple[float]]


def add_text_to_page_pypdf(page, text_params: list[TextParams]):

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
        can.drawString(x, y, text_param.text)

    # Сохраняем полученную PDF-ку в память
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Поворачиваем весь лист согласно углу поворота страницы, чтобы они совпадали
    new_pdf.pages[0].rotate(page.rotation)

    # Вливаем в исходную PDF-страницу нашу новую с нашим контентом
    page.merge_page(new_pdf.pages[0])
    
def enumerate_tome(tome: Tome, start: int, logger: ProcessingLogger, with_bookmarks: bool = True):
    path = tome.savepath.parent / (str(tome.savepath.name) + '.temp') 
    if not (path.exists() and path.is_file()):
        raise FileNotFoundError()
    
    #doc = fitz.open(tome.savepath)
    doc = PdfReader(path)
    enumerator = PageEnumerator(tome, start)
    to_return = start
    page_in_document = 0
    output = PdfWriter()

    logger.set_progress_bar(0)
    logger.writeline('')
    logger.writeline('Расставляю нумерацию страниц...')
    delta = int(100 / len(doc.pages))

    gost = Path(os.getcwd()) / 'pdf_report_builder' / 'data' / 'GOST2304_TypeA.ttf'
    pdfmetrics.registerFont(TTFont('GOST2304A', gost))

    for i in enumerator:
        to_return = i[0]
        print(i)
        page_in_document += 1
        page = doc.pages[page_in_document - 1] # doc[0]
        if i[1] == True and i[2] == True:
            enum_params = TextParams(
                str(i[0]),
                lambda true_width, true_height: (true_width - 35, true_height - 30)
            )
            add_text_to_page_pypdf(page, [enum_params])
        output.add_page(page)
        logger.add_to_progress_bar(delta)
    
    if with_bookmarks:
        logger.writeline(' Расставляю закладки...')
        add_bookmarks(output, tome)
        output.page_mode = '/UseOutlines'
    
    for page in output.pages:
        page.compress_content_streams()
    
    logger.writeline('Сохраняю результат...')
    #doc.save(tome.savepath, incremental=True, encryption=0)
    with open(tome.savepath, 'wb+') as output_file:
        output.write(output_file)
    os.remove(path)
    return to_return