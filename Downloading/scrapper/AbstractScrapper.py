import abc
from abc import ABC, abstractmethod


class AbstractScrapper(ABC):

    @property
    @abstractmethod
    def _related_url(self):
        return self._related_url_value

    @_related_url.setter
    def _related_url(self, url):
        self._related_url_value = url

    @property
    def _doi(self):
        return self._doi_value

    @_doi.setter
    def _doi(self, doi):
        self._doi_value = doi
        self._url = self._create_url(doi)

    def set_doi(self, doi):
        self._doi = doi

    @property
    def _url(self):
        return self._url_value

    @_url.setter
    def _url(self, url):
        self._url_value = url

    def __init__(self, doi: str = None):
        self._url_value = ''
        self._related_url_value = ''
        self._doi_value = ''
        if doi is not None:
            self._doi = doi
        return

    @abstractmethod
    def _create_url(self, doi):
        pass

    @abstractmethod
    def scrap(self):
        pass

    @staticmethod
    def _get_header():
        return {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/83.0.4103.97 Safari/537.36',
        }

    @staticmethod
    def _purify_file_name(doi: str) -> str:
        return doi.replace('//', '/').replace('/', '-')