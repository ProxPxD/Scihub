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

    def scrap(self, title: str=None, authors: str=None):
        path = self._create_file_path(title, authors)
        content = self.get_content()
        self._save_file(path, content)
        return self._dir_path

    def get_content(self, key=None, cert=None):
        http = httplib2.Http(".cache")  # h.add_certificate(key, cert, "")
        resp, content = http.request(self._url, "GET", headers=self._get_header())

        while self._meta_redirect(content):
            resp, content = http.request(DocumentScrapper._meta_redirect(content), "GET", headers=self._get_header())

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
        return DocumentScrapper._find_by_refresh_name(soup, 'Refresh') or DocumentScrapper._find_by_refresh_name(soup, 'refresh')

    @staticmethod
    def _find_by_refresh_name(soup: BeautifulSoup, refresh: str):
        return soup.find('meta', attrs={'http-equiv': refresh})

    def create_dir_path(self):
        self._dir_path: Path = Constants.Paths.DOCUMENTS_PATH / self._purify_file_name(self._doi)
        return self._dir_path

    def get_dir_path(self):
        return self._dir_path or self.create_dir_path()

    def _create_dir(self):
        self._dir_path.mkdir(exist_ok=True)
    
    def _create_file_path(self, title: str, authors: str) -> Path:
        self.create_dir_path()
        self._create_dir()
        return self._dir_path / (title + ' - ' + authors + '.pdf')

    @staticmethod
    def _save_file(path: Path, content):
        if len(str(path)) >= 260:
            print('ERROR: Path to long')
            return
        with path.open('wb+') as f:
            f.write(content)

