import warnings

import httplib2
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


def _get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
    }


def get_content(url, key=None, cert=None):
    http = httplib2.Http(".cache")  # h.add_certificate(key, cert, "")
    resp, content = http.request(url, "GET", headers=_get_header())

    while _meta_redirect(content):
        resp, content = http.request(_meta_redirect(content), "GET", headers=_get_header())

    return content


def _meta_redirect(content):
    soup = BeautifulSoup(content, 'lxml')

    result = _find_refresh(soup)
    if result:
        wait, text = result["content"].split(";")
        if text.strip().lower().startswith("url="):
            url = text[4:]
            return url
    return None


def _find_refresh(soup):
    # refresh_names = ['Refresh', 'refresh']
    # refresh_exists = map(lambda r: _find_by_refresh_name(soup, r), refresh_names)
    # return reduce(operator.or_, refresh_exists)
    return _find_by_refresh_name(soup, 'Refresh') or _find_by_refresh_name(soup, 'refresh')


def _find_by_refresh_name(soup: BeautifulSoup, refresh: str):
    return soup.find('meta', attrs={'http-equiv': refresh})
