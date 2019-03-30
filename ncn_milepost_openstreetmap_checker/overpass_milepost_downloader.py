import overpass
from . import Milepost
from . import MilepostCollection


class OverpassMilepostDownloader:

    def __init__(self, api: overpass.API):
        self.api = api
        self.bbox = (
            49.959999905,
            -7.57216793459,
            58.6350001085,
            1.68153079591
            # 55.90053358079389,
            # -3.264827728271484,
            # 55.973990318389355,
            # -3.121662139892578
        )

    def download(self) -> MilepostCollection:
        bbox_str = ','.join(map(str, self.bbox))
        response = self.api.get('node[ncn_milepost](%s)' % bbox_str)
        mileposts = MilepostCollection()
        for feature in response["features"]:
            coordinates = feature["geometry"]["coordinates"]
            properties = feature.get("properties", {})
            milepost_type = properties.get("ncn_milepost", None)
            sustrans_ref = properties.get("sustrans_ref", None)
            if not Milepost.valid_sustrans_ref(sustrans_ref):
                sustrans_ref = "Invalid ref: '%s' from OSM (%f, %f)" % \
                               (sustrans_ref, coordinates[0], coordinates[1])

            milepost = Milepost()
            milepost.set_sustrans_ref(sustrans_ref)
            milepost.set_osm_id(feature["id"])
            milepost.set_osm_coordinates(coordinates)
            milepost.set_osm_milepost_type(milepost_type)

            mileposts.add_milepost(milepost)

        return mileposts
