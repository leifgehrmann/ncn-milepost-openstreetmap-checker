from . import Milepost
from typing import List, Optional


class MilepostCollection:
    def __init__(self):
        self.mileposts = {}

    def add_milepost(self, milepost: Milepost) -> None:
        self.mileposts[milepost.sustrans_ref] = milepost

    def get_milepost_by_sustrans_ref(
            self,
            sustrans_ref: str
    ) -> Optional[Milepost]:
        return self.mileposts.get(sustrans_ref, None)

    def get_mileposts(self) -> List[Milepost]:
        return list(self.mileposts.values())

    def get_known_mapped_mileposts(self) -> List[Milepost]:
        def filter_mileposts(milepost: Milepost):
            return milepost.osm_id is not None and \
                   milepost.sustrans_ref is not None
        return list(filter(filter_mileposts, self.get_mileposts()))

    def get_unknown_mapped_mileposts(self) -> List[Milepost]:
        def filter_mileposts(milepost: Milepost):
            return milepost.osm_id is not None and \
                   milepost.sustrans_ref is None
        return list(filter(filter_mileposts, self.get_mileposts()))

    def get_known_unmapped_mileposts(self) -> List[Milepost]:
        def filter_mileposts(milepost: Milepost):
            return milepost.osm_id is None and \
                   milepost.sustrans_ref is not None
        return list(filter(filter_mileposts, self.get_mileposts()))

    def get_unknown_unmapped_mileposts(self) -> List[Milepost]:
        def filter_mileposts(milepost: Milepost):
            return milepost.osm_id is None and \
                   milepost.sustrans_ref is None
        return list(filter(filter_mileposts, self.get_mileposts()))
