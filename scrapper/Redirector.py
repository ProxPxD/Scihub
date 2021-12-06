import httplib2
from bs4 import BeautifulSoup



def get_content(url, key=None, cert=None):
    http = httplib2.Http(".cache")  # h.add_certificate(key, cert, "")
    resp, content = http.request(url, "GET", headers=_get_header())

    while _meta_redirect(content):
        print('respo:::::', resp)
        resp, content = http.request(_meta_redirect(content), "GET")

    return content

def _get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
    }

def _meta_redirect(content):
    soup = BeautifulSoup(content)

    result = _find_refresh(soup)
    print('\n' * 3, '#' * 30, '\n' * 5)
    print(soup.prettify())
    if result:
        wait, text = result["content"].split(";")
        if text.strip().lower().startswith("url="):
            url = text[4:]
            return url
    return None


def _find_refresh(soup):
    result = _find_by_refresh_name(soup, 'Refresh')
    if not result:
        result = soup.find("meta", attrs={"http-equiv": "refresh"})
    return result

def _find_by_refresh_name(soup: BeautifulSoup, refresh: str):
    return soup.find('meta', attrs={'http-equiv': refresh})
