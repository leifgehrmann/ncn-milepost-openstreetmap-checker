from typing import Optional
import re


class Milepost:
    def __init__(self):
        self.sustrans_ref = None
        self.wiki_sustrans_ref = None
        self.wiki_region = None
        self.wiki_milepost_type = None
        self.wiki_location = None
        self.wiki_osm_link = None
        self.osm_id = None
        self.osm_sustrans_ref = None
        self.osm_milepost_type = None
        self.osm_longitude = None
        self.osm_latitude = None

    def set_sustrans_ref(self, sustrans_ref: str):
        self.sustrans_ref = sustrans_ref

    def set_wiki_sustrans_ref(self, sustrans_ref: str):
        self.wiki_sustrans_ref = sustrans_ref

    def set_wiki_region(self, region: str):
        self.wiki_region = region

    def set_wiki_milepost_type(self, milepost_type: str):
        self.wiki_milepost_type = milepost_type

    def set_wiki_location(self, location: str):
        self.wiki_location = location

    def set_wiki_osm_link(self, osm_link: str):
        self.wiki_osm_link = osm_link

    def set_osm_id(self, osm_id: int):
        self.osm_id = osm_id

    def set_osm_sustrans_ref(self, sustrans_ref: str):
        self.osm_sustrans_ref = sustrans_ref

    def set_osm_milepost_type(self, milepost_type: str):
        self.osm_milepost_type = milepost_type

    def set_osm_longitude(self, longitude: float):
        self.osm_longitude = longitude

    def set_osm_latitude(self, latitude: float):
        self.osm_latitude = latitude

    def has_valid_sustrans_ref(self) -> bool:
        return self._valid_sustrans_ref(self.sustrans_ref)

    @staticmethod
    def _valid_sustrans_ref(sustrans_ref: Optional[str]) -> bool:
        if sustrans_ref is None:
            return False
        return bool(re.match('^MP[0-9]+$', sustrans_ref))
