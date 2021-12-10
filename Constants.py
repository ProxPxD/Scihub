from pathlib import Path
import pathlib


class Paths:
    MAIN_PATH = Path(__file__).parent
    DOCUMENTS_DIR = 'Documents'
    DOCUMENTS_PATH = MAIN_PATH / DOCUMENTS_DIR
