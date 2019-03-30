from bs4 import BeautifulSoup
import urllib.request
from ncn_milepost_openstreetmap_checker import MilepostCollection
from ncn_milepost_openstreetmap_checker import WikiMilepostRow


class WikiMilepostDownloader:

    def __init__(self, url: str, milepost_collection: MilepostCollection):
        self.url = url
        self.milepost_collection = milepost_collection

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
        with urllib.request.urlopen(self.url) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            self._process_page(soup)
