import click

from scrapper.Scrapper import Scrapper


@click.command(name='get')
@click.argument('dois', nargs=-1)
def download(dois):
    scr = Scrapper()
    for doi in dois:
        scr.scrap(doi)



