from pathlib import Path

import httplib2
from bs4 import BeautifulSoup

import Constants
from Downloading.scrapper.AbstractScrapper import AbstractScrapper


class DocumentScrapper(AbstractScrapper):

    @property
    def _related_url(self):
        return 'https://sci.bban.top/pdf/'

    def _create_url(self, doi):
        return self._related_url + doi + '.pdf'

    def scrap(self):
        path = self._create_file_path(self._doi)
        content = self.get_content(self._url)
        self._save_file(path, content)
        return path

    @staticmethod
    def get_content(url, key=None, cert=None):
        http = httplib2.Http(".cache")  # h.add_certificate(key, cert, "")
        resp, content = http.request(url, "GET", headers=DocumentScrapper._get_header())

        while DocumentScrapper._meta_redirect(content):
            resp, content = http.request(DocumentScrapper._meta_redirect(content), "GET", headers=DocumentScrapper._get_header())

        return content

    @staticmethod
    def _meta_redirect(content):
        soup = BeautifulSoup(content)

        result = DocumentScrapper._find_refresh(soup)
        if result:
            wait, text = result["content"].split(";")
            if text.strip().lower().startswith("url="):
                url = text[4:]
                return url
        return None

    @staticmethod
    def _find_refresh(soup):
        # refresh_names = ['Refresh', 'refresh']
        # refresh_exists = map(lambda r: _find_by_refresh_name(soup, r), refresh_names)
        # return reduce(operator.or_, refresh_exists)
        return DocumentScrapper._find_by_refresh_name(soup, 'Refresh') or DocumentScrapper._find_by_refresh_name(soup, 'refresh')

    @staticmethod
    def _find_by_refresh_name(soup: BeautifulSoup, refresh: str):
        return soup.find('meta', attrs={'http-equiv': refresh})

    def _create_file_path(self, doi: str) -> Path:
        return Constants.Paths.DOCUMENTS_PATH / self._purify_doi_part_of_file_name(doi)

    @staticmethod
    def _purify_doi_part_of_file_name(doi: str) -> str:
        return doi.replace('//', '/').replace('/', '.') + '.pdf'

    @staticmethod
    def _save_file(path, content):
        with open(path, 'wb+') as f:
            f.write(content)

