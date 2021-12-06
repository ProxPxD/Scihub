import click

from cli.download import download


@click.group()
def entry_point():
    """
    Entry point for Scihub scrapper
    """

entry_point.add_command(download)
