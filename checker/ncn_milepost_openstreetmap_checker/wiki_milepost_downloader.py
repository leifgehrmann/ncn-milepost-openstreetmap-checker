import logging
from socket import timeout
from urllib.error import HTTPError

from bs4 import BeautifulSoup
import urllib.request
from ncn_milepost_openstreetmap_checker import MilepostCollection
from ncn_milepost_openstreetmap_checker import WikiMilepostRow


class WikiMilepostDownloader:

    def __init__(self, url: str, milepost_collection: MilepostCollection):
        self.url = url
        self.milepost_collection = milepost_collection

        logging.basicConfig()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def _process_row(self, row) -> None:
        milepost_row = WikiMilepostRow(row)
        sustrans_ref = milepost_row.read_sustrans_ref()

        milepost = self.milepost_collection.\
            get_or_create_milepost_by_sustrans_ref(sustrans_ref)

        milepost.set_wiki_sustrans_ref(sustrans_ref)
        milepost.set_wiki_region(milepost_row.read_region())
        milepost.set_wiki_milepost_type(milepost_row.read_milepost_type())
        milepost.set_wiki_location(milepost_row.read_location())
        milepost.set_wiki_osm_link(milepost_row.read_osm_link())

    def _process_table(self, table: BeautifulSoup) -> None:
        for row in table.select('tr'):
            if len(row.select('th')) > 0:
                continue
            self._process_row(row)

    def _process_page(self, soup: BeautifulSoup) -> None:
        for table in soup.select('.wikitable'):
            self._process_table(table)

    def download(self) -> None:
        attempts = 1
        html = ''
        # We try 5 times because sometimes the OpenStreetMap wiki times out.
        while attempts <= 5:
            self.logger.info('Downloading wiki page (Attempt %d)' % attempts)
            try:
                with urllib.request.urlopen(self.url, timeout=120) as response:
                    html = response.read()
                    break
            except HTTPError:
                self.logger.warning('HTTPError downloading wiki page')
            except timeout:
                self.logger.warning(
                    'socket.timeout error downloading wiki page'
                )
            finally:
                attempts += 1

        if html == '':
            raise Exception('Failed downloading wiki page')

        self.logger.info('Downloaded wiki page, now parsing wiki HTML')
        soup = BeautifulSoup(html, 'html.parser')
        self.logger.info('Parsed wiki HTML, now processing wiki HTML')
        self._process_page(soup)
        self.logger.info('Successfully processed wiki data')
