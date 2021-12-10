import click

import Downloading.download


@click.command(name='get')
@click.argument('dois', nargs=-1)
def download(dois):
    Downloading.download.get_documents(dois, verbose=True)



