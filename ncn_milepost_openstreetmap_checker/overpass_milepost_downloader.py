import logging

import overpass
from . import Milepost
from . import MilepostCollection


class OverpassMilepostDownloader:

    def __init__(
            self,
            api: overpass.API,
            milepost_collection: MilepostCollection
    ):
        self.api = api
        self.milepost_collection = milepost_collection
        self.bbox = (
            49.9599,
            -8.1956,
            60.8842,
            1.7746
        )

        logging.basicConfig()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    @staticmethod
    def _get_sustrans_ref_from_feature(feature) -> str:
        properties = feature.get('properties', {})
        return properties.get('sustrans_ref', None)

    @staticmethod
    def _update_milepost_with_osm_data(milepost: Milepost, feature):
        coordinates = feature['geometry']['coordinates']
        properties = feature.get('properties', {})
        sustrans_ref = properties.get('sustrans_ref', None)
        milepost_type = properties.get('ncn_milepost', None)
        osm_id = feature['id']

        milepost.set_osm_id(osm_id)
        milepost.set_osm_sustrans_ref(sustrans_ref)
        milepost.set_osm_longitude(coordinates[0])
        milepost.set_osm_latitude(coordinates[1])
        milepost.set_osm_milepost_type(milepost_type)

    def download(self) -> None:
        bbox_str = ','.join(map(str, self.bbox))
        self.logger.info('Downloading OSM data')
        response = self.api.get('node[ncn_milepost](%s)' % bbox_str)
        self.logger.info('Downloaded OSM data, now processing OSM data')
        for feature in response['features']:
            sustrans_ref = self._get_sustrans_ref_from_feature(feature)

            # Get an existing milepost if it exists
            milepost = self.milepost_collection.\
                get_or_create_milepost_by_sustrans_ref(sustrans_ref)

            # Before we update it, check if osm data has already been set
            if milepost.osm_id is not None:
                raise Exception('Duplicate OSM entry for %s' % sustrans_ref)

            self._update_milepost_with_osm_data(milepost, feature)
        self.logger.info('Successfully processed OSM data')
