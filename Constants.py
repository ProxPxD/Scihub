from pathlib import Path


class Paths:
    MAIN_PATH = Path(__file__).parent
    DOCUMENTS_DIR = 'Documents'
    DOCUMENTS_PATH = MAIN_PATH / DOCUMENTS_DIR


class Messages:
    DOWNLOAD_INIT = 'Starting downloading...'
    DOWNLOAD_DOCUMENT = 'Downloading {}: {}'