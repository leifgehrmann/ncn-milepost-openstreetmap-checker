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
        self.wiki_milepost_type = milepost_type.lower()

    def set_wiki_location(self, location: str):
        self.wiki_location = location

    def set_wiki_osm_link(self, osm_link: str):
        self.wiki_osm_link = osm_link

    def set_osm_id(self, osm_id: int):
        self.osm_id = osm_id

    def set_osm_sustrans_ref(self, sustrans_ref: str):
        self.osm_sustrans_ref = sustrans_ref

    def set_osm_milepost_type(self, milepost_type: str):
        self.osm_milepost_type = milepost_type.lower()

    def set_osm_longitude(self, longitude: float):
        self.osm_longitude = longitude

    def set_osm_latitude(self, latitude: float):
        self.osm_latitude = latitude

    # General Info
    def is_in_wiki(self) -> bool:
        return self.wiki_sustrans_ref is not None

    def is_in_osm(self) -> bool:
        return self.osm_id is not None

    # Mapping/Listing validation
    def is_mapped_completely_in_osm(self) -> bool:
        return self.is_in_osm() and \
               self.has_valid_osm_sustrans_ref() and \
               self.has_valid_osm_milepost_type()

    def is_mapped_and_listed_completely_in_osm_and_wiki(self) -> bool:
        return self.is_mapped_completely_in_osm() and \
               self.is_in_wiki() and \
               self.has_matching_sustrans_ref() and \
               self.has_matching_milepost_type() and \
               self.has_matching_node_id()

    # Sustrans Ref validation
    def has_valid_sustrans_ref_as_key(self) -> bool:
        return self._valid_sustrans_ref(self.sustrans_ref)

    def has_valid_wiki_sustrans_ref(self) -> bool:
        return self._valid_sustrans_ref(self.wiki_sustrans_ref)

    def has_valid_osm_sustrans_ref(self) -> bool:
        return self._valid_sustrans_ref(self.osm_sustrans_ref)

    def has_matching_sustrans_ref(self) -> bool:
        return self.wiki_sustrans_ref == self.osm_sustrans_ref

    # Milepost type validation
    def has_valid_wiki_milepost_type(self) -> bool:
        return self._valid_milepost_type(self.wiki_milepost_type)

    def has_valid_osm_milepost_type(self) -> bool:
        return self._valid_milepost_type(self.osm_milepost_type)

    def has_matching_milepost_type(self) -> bool:
        return self.wiki_milepost_type == self.osm_milepost_type

    # Node id validation
    def has_valid_node_id_in_wiki(self) -> bool:
        return self.wiki_osm_link is not None and self.wiki_osm_link

    def has_matching_node_id(self) -> bool:
        return self.wiki_osm_link is not None and self.osm_id is not None and \
               int(self.wiki_osm_link) == int(self.osm_id)

    @staticmethod
    def _valid_sustrans_ref(sustrans_ref: Optional[str]) -> bool:
        if sustrans_ref is None:
            return False
        return bool(re.match('^MP[0-9]+$', sustrans_ref))

    @staticmethod
    def _valid_milepost_type(milepost_type: Optional[str]) -> bool:
        if milepost_type is None:
            return False
        return bool(re.match('^(dudgeon|mccoll|mills|rowe)$', milepost_type))
