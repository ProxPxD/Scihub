from pathlib import Path

from Constants import Messages
from Constants import Paths
from Downloading.scrapper.ScrapperManager import ScrapperManager
from utils.Condition import when

full_doi_pattern = 'https://doi.org/'

def get_documents(references: list[str, ...], verbose=False):
    when(not Paths.DOCUMENTS_PATH.exists()).execute(lambda _: Paths.DOCUMENTS_PATH.mkdir())
    when(verbose).print(Messages.DOWNLOAD_INIT)
    dois = get_dois_from_references(references)
    paths = download_documents(dois, verbose)


def download_documents(dois: list[str, ...], verbose=False):
    paths: list[Path, ...] = []
    scrapper = ScrapperManager()
    for i, doi in enumerate(dois, 1):
        when(verbose).print(Messages.DOWNLOAD_DOCUMENT.format(i, doi))
        scrapper.set_doi(doi)
        path = scrapper.scrap_document()
        paths.append(path)
    return paths


def get_dois_from_references(references: list[str, ...]):
    return [get_doi_from_reference(ref) for ref in references]


def get_doi_from_reference(reference: str) -> str:
    if full_doi_pattern in reference:
        return reference.removeprefix(full_doi_pattern)
    return reference