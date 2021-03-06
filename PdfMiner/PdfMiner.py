import pathlib

import Constants

name = '10.1016.j.copsyc.2017.03.030''.pdf'
# name = '10.1210.er.2017-00246''.pdf'
dir_to = pathlib.Path(__file__)
dir_from = Constants.Paths.DOCUMENTS_PATH
the_path = str(dir_from / name)


def convert_title_to_filename(title):
    filename = title.lower()
    filename = filename.replace(' ', '_')
    return filename


def split_to_title_and_pagenum(table_of_contents_entry):
    title_and_pagenum = table_of_contents_entry.strip()

    title = None
    pagenum = None

    if len(title_and_pagenum) > 0:
        if title_and_pagenum[-1].isdigit():
            i = -2
            while title_and_pagenum[i].isdigit():
                i -= 1

            title = title_and_pagenum[:i].strip()
            pagenum = int(title_and_pagenum[i:].strip())

    return title, pagenum

#####
import PyPDF2
import csv


##############
def get_title_pagenum_list():
    title_list = []
    pagenum_list = []
    title_formatted_list = []
    for item in table_of_contents_raw:
        title, pagenum = split_to_title_and_pagenum(item)
        if title != None:
            title_list.append(title)
            pagenum_list.append(pagenum)
            title_formatted_list.append(convert_title_to_filename(title))

    # for page_list, we need to add the last page as well
    pagenum_list.append(num_of_pages + 1)
    return title_list, pagenum_list, title_formatted_list


title_list, pagenum_list, title_formatted_list = get_title_pagenum_list()

##################

for i in range(1, len(title_formatted_list)):
    title_formatted = title_formatted_list[i]
    page_start = pagenum_list[i] - 1
    page_end = pagenum_list[i + 1] - 2

    writer = PyPDF2.PdfFileWriter()

    for page in range(page_start, page_end + 1):
        writer.addPage(reader.getPage(page))

    output_filename = Constants.Paths.DOCUMENTS_PATH / (title_formatted + '.pdf')

    with open(output_filename, 'wb') as output:
        writer.write(output)

#################

year_written = []
# first element is Preface, where year is not applicable
year_written.append('n/a')

for title_formatted in title_formatted_list[1:]:

    text = convert_pdf_to_string(Constants.Paths.DOCUMENTS_PATH / (title_formatted + '.pdf'))

    # exclude the year after the title, collect in a list
    i = 0
    while text[i] != '(':
        i += 1
    year = text[i + 1:i + 5]
    text = text[:i] + text[i + 6:]
    year_written.append(year)

    # replace 'Return to Table of Contents', which is not part of the text
    text = text.replace('Return to Table of Contents', '')

    # replace Fin from the end of the last title
    if title_formatted == 'the_haunter_of_the_dark':
        text = text[:-15]

    # save in a txt file
    text_file = open(Constants.Paths.DOCUMENTS_PATH / (title_formatted + '.txt'), 'w')
    n = text_file.write(text)
    text_file.close()

###########
with open(Constants.Paths.DOCUMENTS_PATH / ('table_of_contents' + '.csv'), 'a') as f:
    writer = csv.writer(f)
    writer.writerows(zip(title_list, pagenum_list, title_formatted_list, year_written))
