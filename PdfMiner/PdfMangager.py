from pathlib import Path

import PyPDF2


_sciub_front_page_prefix = 'AcceptedManuscript'

class PdfManager:

    def __init__(self, path: Path):
        self._file_directory = path.parent
        self._file_name = str(path)
        self._path = str(path)
        self._reader: PyPDF2.PdfFileReader = PyPDF2.PdfFileReader(self._path)
        self._writer: PyPDF2.PdfFileWriter

    def get_title_and_author(self):
        pass

    # Trimming
    def trim_scihub_front_page_if_exists(self):
        if self._file_has_scihub_front_page():
            self._trim_scihub_front_page()

    def _trim_scihub_front_page(self):
        self._writer = PyPDF2.PdfFileWriter()
        for page in self._reader.pages[1:]:
            self._writer.addPage(page)
        with open(self._path.replace('.pdf', '_0.pdf'), 'wb') as f:
            self._writer.write(f)

    def _file_has_scihub_front_page(self):
        return self._reader.getPage(0).extractText()[:len(_sciub_front_page_prefix)] == _sciub_front_page_prefix