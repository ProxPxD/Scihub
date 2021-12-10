from pathlib import Path

from Downloading.scrapper.DocumentDataScrapper import DocumentDataScrapper
from Downloading.scrapper.DocumentScrapper import DocumentScrapper


class ScrapperManager:

    def __init__(self, doi=''):
        self._document_scrapper = DocumentScrapper(doi)
        self._document_data_scrapper = DocumentDataScrapper(doi)

    def set_doi(self, doi: str):
        self._document_scrapper.set_doi(doi)
        self._document_data_scrapper.set_doi(doi)

    def scrap_document(self) -> Path:
        if not self._document_scrapper.create_dir_path().exists():
            title, authors = self._document_data_scrapper.scrap()
            self._document_scrapper.scrap(title, authors)
        return self._document_scrapper.get_dir_path()

    def _scrap_document_data(self):
        return self._document_data_scrapper.scrap()
