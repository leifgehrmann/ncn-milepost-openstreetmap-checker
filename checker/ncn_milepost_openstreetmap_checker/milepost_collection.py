from . import Milepost
from typing import List, Optional


class MilepostCollection:
    def __init__(self):
        self.mileposts = {}
        self.unknown_milepost_count = 0

    def add_milepost(self, milepost: Milepost) -> None:
        self.mileposts[milepost.sustrans_ref] = milepost

    def get_milepost_by_sustrans_ref(
            self,
            sustrans_ref: str
    ) -> Optional[Milepost]:
        return self.mileposts.get(sustrans_ref, None)

    def get_or_create_milepost_by_sustrans_ref(
            self,
            sustrans_ref: str
    ) -> Optional[Milepost]:
        milepost = None
        if self._valid_sustrans_ref(sustrans_ref):
            milepost = self.get_milepost_by_sustrans_ref(sustrans_ref)

        # Create a new milepost if None was found
        if milepost is None:
            milepost = self._create_milepost_with_sustrans_ref(sustrans_ref)
            self.add_milepost(milepost)

        return milepost

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

    def _create_milepost_with_sustrans_ref(self, sustrans_ref: str) -> Milepost:
        if not self._valid_sustrans_ref(sustrans_ref):
            self.unknown_milepost_count += 1
            sustrans_ref = 'Unknown Ref %d' % self.unknown_milepost_count

        milepost = Milepost()
        milepost.set_sustrans_ref(sustrans_ref)
        self.add_milepost(milepost)
        return milepost

    @staticmethod
    def _valid_sustrans_ref(sustrans_ref: Optional[str]) -> bool:
        temporary_milepost = Milepost()
        temporary_milepost.set_sustrans_ref(sustrans_ref)
        return temporary_milepost.has_valid_sustrans_ref_as_key()

