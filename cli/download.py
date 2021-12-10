import click

import Downloading.download
from Downloading.scrapper import Scrapper


@click.command(name='get')
@click.argument('dois', nargs=-1)
def download(dois):
    Downloading.download.get_documents(dois, verbose=True)



