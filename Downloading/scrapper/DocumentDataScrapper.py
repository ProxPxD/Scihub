import httplib2
from bs4 import BeautifulSoup

from Downloading.scrapper.AbstractScrapper import AbstractScrapper


class DocumentDataScrapper(AbstractScrapper):
    @property
    def _related_url(self):
        return 'https://sci-hub.ee/'

    def _create_url(self, doi):
        return self._related_url + doi

    def scrap(self):  # TODO idea: removing the last part of the title
        http = httplib2.Http(".cache")
        resp, content = http.request(self._url, "GET", headers=self._get_header())
        soup = BeautifulSoup(content)
        citation = soup.find('div', id='citation')
        authors = self._purify_input(citation.contents[0])
        title = self._purify_input(citation.contents[1].text)
        return title, authors

    @staticmethod
    def _purify_input(string: str) -> str:
        string = string.strip()
        if string[-1] == '.':
            string = string[:-1]
        return string

    '''
            <div id="citation" onclick="clip(this)">
                Joel, Daphna (2011).
                <i>Male or Female? Brains are Intersex. Frontiers in Integrative Neuroscience, 5(), –.</i>
                doi:10.3389/fnint.2011.00057&nbsp;
            </div>
    '''