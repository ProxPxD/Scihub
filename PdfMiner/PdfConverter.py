import itertools
from dataclasses import dataclass
from io import StringIO
from typing import ClassVar

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


@dataclass
class Constants:
    PLEASE_CITE_INDEX: ClassVar[int] = 18
    PLEASE_CITE_STRING: ClassVar[str] = 'Please cite this article as: '


class PdfConverter:

    def __init__(self, path):
        self._path = path

    def get_title_and_authors(self):
        table: list[str, ...] = self._get_table_of_contents(0)
        please_cite_string = self._get_please_cite_string(table)
        title, authors = self._separate_title_and_author(please_cite_string)
        return title, authors

    def _get_please_cite_string(self, table):
        table = table[Constants.PLEASE_CITE_INDEX:]
        string = table[0].removeprefix(Constants.PLEASE_CITE_STRING)
        for line in table[1:]:
            if line == '':
                break
            string += ' ' + line
        return string

    def _separate_title_and_author(self, cite_string: str):  # -> tuple[str, list[str, ...]]:
        separated = cite_string.split(',')
        title = ','.join(separated[1:-1])
        authors = separated[0]
        return title, authors

    def _get_table_of_contents(self, num=-1):
        text = self.convert_pdf_to_string(num)
        text = text.replace('.', '')
        text = text.replace('\x0c', '')
        table_of_contents_raw = text.split('\n')
        return table_of_contents_raw

    def convert_pdf_to_string(self, num=-1):
        output_string = StringIO()
        with open(self._path, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            pages = PDFPage.create_pages(doc)
            if num >= 0:
                pages = itertools.islice(pages, num, num + 1)
            for page in pages:
                interpreter.process_page(page)

        return (output_string.getvalue())
