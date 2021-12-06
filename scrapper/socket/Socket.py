import requests
from requests import Response

_scihub_url = 'https://sci-hub.ee/'

def _get_header():
    return {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Dnt': '1',
        'Host': 'httpbin.org',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.97 Safari/537.36',
        'X-Amzn-Trace-Id': 'Root=1-5ee7bbec-779382315873aa33227a5df6'}


def get_html(doi: str) -> str:
    url = _scihub_url + doi
    page = _get_page(url)
    if page.status_code != 200:
        _handle_status_codes(page)
    return page.text


def _get_page(url: str) -> Response:
    session = requests.Session()
    session.headers.update({'User-agent': 'Mozilla/5.0'})
    page = session.get(url, allow_redirects=False)
    session.close()
    return page


def _handle_status_codes(page: Response):
    pass