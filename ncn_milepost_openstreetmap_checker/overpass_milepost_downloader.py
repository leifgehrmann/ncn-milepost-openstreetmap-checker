import overpass
import uuid
from . import Milepost
from . import MilepostCollection


class OverpassMilepostDownloader:

    def __init__(self, api: overpass.API):
        self.api = api
        self.bbox = (
            49.9599,
            -7.5721,
            60.8842,
            1.6815
            # 55.90053358079389,
            # -3.264827728271484,
            # 55.973990318389355,
            # -3.121662139892578
        )

    @staticmethod
    def _get_sustrans_ref_from_feature(feature) -> str:
        properties = feature.get("properties", {})
        return properties.get("sustrans_ref", None)

    @staticmethod
    def _create_new_milepost(sustrans_ref: str) -> Milepost:
        if not Milepost.valid_sustrans_ref(sustrans_ref):
            sustrans_ref = "Unknown-%s" % uuid.uuid4()

        milepost = Milepost()
        milepost.set_sustrans_ref(sustrans_ref)
        return milepost

    @staticmethod
    def _update_milepost_with_osm_data(milepost: Milepost, feature):
        coordinates = feature["geometry"]["coordinates"]
        properties = feature.get("properties", {})
        sustrans_ref = properties.get("sustrans_ref", None)
        milepost_type = properties.get("ncn_milepost", None)
        osm_id = feature["id"]

        milepost.set_osm_id(osm_id)
        milepost.set_osm_sustrans_ref(sustrans_ref)
        milepost.set_osm_coordinates(coordinates)
        milepost.set_osm_milepost_type(milepost_type)

    def download(self, milepost_collection: MilepostCollection) -> None:
        bbox_str = ','.join(map(str, self.bbox))
        response = self.api.get('node[ncn_milepost](%s)' % bbox_str)
        for feature in response["features"]:
            sustrans_ref = self._get_sustrans_ref_from_feature(feature)

            # Get an existing milepost if it exists
            milepost = None
            if Milepost.valid_sustrans_ref(sustrans_ref):
                milepost = milepost_collection.get_milepost_by_sustrans_ref(
                    sustrans_ref
                )

            # Create a new milepost if None was found and add it to the
            # collection
            if milepost is None:
                milepost = self._create_new_milepost(sustrans_ref)
                milepost_collection.add_milepost(milepost)

            # Before we update it, check if osm data has already been set
            if milepost.osm_id is not None:
                raise Exception("Duplicate OSM entry for %s" % sustrans_ref)

            self._update_milepost_with_osm_data(milepost, feature)
