from pathlib import Path

import Downloading.download
import PdfMiner.PdfMangager
from Downloading.scrapper.ScrapperManager import ScrapperManager


if __name__ == '__main__':
    doi = 'https://doi.org/10.1016/j.copsyc.2017.03.030'
    doi = '10.1111/j.1529-1006.2007.00032.x'
    doi = 'https://doi.org/10.3389/fpsyg.2019.03050'
    doi = 'https://doi.org/10.3389/fnint.2011.00057'
    the_path = '/home/proxpxd/Desktop/moje_programy/systemowe/Scihub/Documents/10.1210.er.2017-00246.pdf'
    the_path = '/home/proxpxd/Desktop/moje_programy/systemowe/Scihub/Documents/10.1016.j.copsyc.2017.03.030.pdf'
    the_path = '/home/proxpxd/Desktop/moje_programy/systemowe/Scihub/Documents/10.3389.fpsyg.2019.03050.pdf'

    doi = Downloading.download.get_doi_from_reference(doi)
    scr = ScrapperManager(doi)
    the_path = scr.scrap_document()
    manager = PdfMiner.PdfMangager.PdfManager(the_path)
    title, authors = manager.get_title_and_author()
    print(title)
    # manager.trim_scihub_front_page_if_exists()

    # print(convert_pdf_to_string(the_path))
    # path = scr.scrap(doi)
    # print(path)
    # reader = PyPDF2.PdfFileReader(the_path)
    # print(reader.documentInfo)
    # for page in reader.pages:
    #     print(page.extractText(), ('\n' * 2) + '*' * 20)

