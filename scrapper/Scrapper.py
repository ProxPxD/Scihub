from pathlib import Path

import Constants
from scrapper import Redirector


class Scrapper:
    _scihub_url = 'https://sci.bban.top/pdf/'

    def __init__(self):
        pass

    def scrap(self, doi: str) -> Path:
        url = self.create_url(doi)
        path = self._create_file_path(doi)
        content = Redirector.get_content(url)
        self._save_file(path, content)
        return path

    def create_url(self, doi: str):
        return self._scihub_url + doi + '.pdf'

    def _create_file_path(self, doi: str) -> Path:
        return Constants.Paths.DOCUMENTS_PATH / self._purify_doi_part_of_file_name(doi)

    @staticmethod
    def _purify_doi_part_of_file_name(doi: str) -> str:
        return doi.replace('//', '/').replace('/', '.') + '.pdf'

    @staticmethod
    def _save_file(path, content):
        with open(path, 'wb+') as f:
            f.write(content)

