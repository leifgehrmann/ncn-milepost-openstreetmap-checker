import overpass
from ncn_milepost_openstreetmap_checker import OverpassMilepostDownloader


api = overpass.API()
osm_milepost_downloader = OverpassMilepostDownloader(api)
mileposts = osm_milepost_downloader.download()

for milepost in mileposts.get_mileposts():
    print(milepost.to_osm_string())
