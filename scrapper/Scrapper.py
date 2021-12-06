import httplib2 as httplib2
import urllib3
from bs4 import BeautifulSoup

from scrapper import Redirector
from scrapper.socket import Socket
import scrapper.Redirector

class Scrapper:
    _scihub_url = 'https://sci.bban.top/pdf/'
    _scihub_add = 'https://sci.bban.top/pdf/10.1210/er.2017-00246.pdf'

    def __init__(self):
        pass

    def scrap(self, doi: str):
        content = Redirector.get_content(self._scihub_url + doi + '.pdf', None, None)
        with open('eee.pdf', 'wb+') as f:
            f.write(content)
        # print(BeautifulSoup(content).prettify())

        # html_document = Socket.get_html(doi)
        # print(html_document)

        # soup = BeautifulSoup(html_document)
        # print(soup.prettify())

