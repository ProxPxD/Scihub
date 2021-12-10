from Downloading.scrapper.Scrapper import Scrapper


if __name__ == '__main__':
    scr = Scrapper()
    doi = 'https://doi.org/10.1016/j.copsyc.2017.03.030'
    the_path = '/home/proxpxd/Desktop/moje_programy/systemowe/Scihub/Documents/10.1210.er.2017-00246.pdf'
    # print(convert_pdf_to_string(the_path))
    path = scr.scrap(doi)
    # print(path)
    # reader = PyPDF2.PdfFileReader(the_path)
    # print(reader.documentInfo)
    # for page in reader.pages:
    #     print(page.extractText(), ('\n' * 2) + '*' * 20)

