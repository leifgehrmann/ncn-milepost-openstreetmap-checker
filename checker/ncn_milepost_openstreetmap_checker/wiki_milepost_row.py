from bs4 import BeautifulSoup
from typing import Optional


class WikiMilepostRow:

    def __init__(self, row: BeautifulSoup):
        self.row = row

    def read_region(self) -> Optional[str]:
        return self.row.select_one('td:nth-of-type(1)').get_text().strip()

    def read_sustrans_ref(self) -> Optional[str]:
        return self.row.select_one('td:nth-of-type(2)').get_text().strip()

    def read_milepost_type(self) -> Optional[str]:
        return self.row.select_one('td:nth-of-type(3)').get_text().strip()\
            .lower()

    def read_location(self) -> Optional[str]:
        return self.row.select_one('td:nth-of-type(4)').get_text().strip()

    def read_osm_link(self) -> Optional[str]:
        anchor = self.row.select_one('td:nth-of-type(5) a.text')
        if anchor is None:
            return None
        return anchor.get_text().strip()
