from Downloading.scrapper.AbstractScrapper import AbstractScrapper


class DocumentScrapper(AbstractScrapper):
    @property
    def _related_url(self):
        return 'https://sci-hub.ee/'

    def _create_url(self, doi):
        return self._related_url + doi

    def scrap(self):
        '''
        <div id="citation" onclick="clip(this)">
            Joel, Daphna (2011).
            <i>Male or Female? Brains are Intersex. Frontiers in Integrative Neuroscience, 5(), –.</i>
            doi:10.3389/fnint.2011.00057&nbsp;
        </div>
        '''

