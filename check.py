import overpass
from ncn_milepost_openstreetmap_checker import OverpassMilepostDownloader
from ncn_milepost_openstreetmap_checker import MilepostCollection


milepost_collection = MilepostCollection()

api = overpass.API()
osm_milepost_downloader = OverpassMilepostDownloader(api)
osm_milepost_downloader.download(milepost_collection)

headers = [
    "Sustrans Ref",
    "Wiki Sustrans Ref",
    "OSM Sustrans Ref",
    "Wiki Milepost Type",
    "OSM Milepost Type",
    "Wiki Region",
    "Wiki Location",
    "Wiki OSM link",
    "OSM Id",
    "OSM Longitude",
    "OSM Latitude",
]

print(",".join(headers))
for milepost in milepost_collection.get_mileposts():
    row = [
        str(milepost.sustrans_ref),
        str(milepost.wiki_sustrans_ref),
        str(milepost.osm_sustrans_ref),
        str(milepost.wiki_milepost_type),
        str(milepost.osm_milepost_type),
        str(milepost.wiki_region),
        str(milepost.wiki_location),
        str(milepost.wiki_osm_link),
        str(milepost.osm_id),
        str(milepost.osm_coordinates[0]),
        str(milepost.osm_coordinates[1])
    ]
    print(",".join(row))
