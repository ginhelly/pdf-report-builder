from typing import NamedTuple

import fitz
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
    chunk = StructuralChunk(
        el.pages_number,
        el.enumeration_include,
        el.enumeration_print
    )
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


def add_text_to_page2(page, text):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, (page.mediabox.width, page.mediabox.height))
    can.setFont('GOST2304A', 14)
    can.drawString(page.mediabox.width - 35, page.mediabox.height - 30, text)
    can.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)
    page.merge_page(new_pdf.pages[0])


def add_text_to_page(page, text):
    """Не работает"""
    damn_point = fitz.Point(page.mediabox.width - 25, 25)
    shape = page.new_shape()
    fontsize = int(round(max(page.rect.height, page.rect.width) ** 0.5))
    shape.insert_text(damn_point, text, fontsize=fontsize, lineheight=5)
    shape.commit()
    
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
        if i[1] == False or i[2] == False:
            output.add_page(page)
            logger.add_to_progress_bar(delta)
            continue
        add_text_to_page2(page, str(i[0]))
        output.add_page(page)
        logger.add_to_progress_bar(delta)
    
    if with_bookmarks:
        logger.writeline(' Расставляю закладки...')
        add_bookmarks(output, tome)
        output.page_mode = '/UseOutlines'
    
    logger.writeline('Сохраняю результат...')
    #doc.save(tome.savepath, incremental=True, encryption=0)
    with open(tome.savepath, 'wb+') as output_file:
        output.write(output_file)
    os.remove(path)
    return to_return