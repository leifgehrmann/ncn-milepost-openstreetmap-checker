import overpass
import csv
from ncn_milepost_openstreetmap_checker import OverpassMilepostDownloader
from ncn_milepost_openstreetmap_checker import WikiMilepostDownloader
from ncn_milepost_openstreetmap_checker import MilepostCollection


milepost_collection = MilepostCollection()

# Load all the mileposts from the wiki
wiki_url = 'https://wiki.openstreetmap.org/wiki/Sustrans_Millennium_Mileposts'
wiki_milepost_downloader = WikiMilepostDownloader(
    wiki_url,
    milepost_collection
)
wiki_milepost_downloader.download()

# Load all the mileposts from overpass
api = overpass.API()
osm_milepost_downloader = OverpassMilepostDownloader(
    api,
    milepost_collection
)
osm_milepost_downloader.download()

with open('output.csv', mode='w') as output_file:
    output_writer = csv.writer(
        output_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    headers = [
        'Sustrans Ref',
        'Wiki Sustrans Ref',
        'OSM Sustrans Ref',
        'Wiki Milepost Type',
        'OSM Milepost Type',
        'Wiki Region',
        'Wiki Location',
        'Wiki OSM link',
        'OSM Id',
        'OSM Longitude',
        'OSM Latitude',
    ]

    output_writer.writerow(headers)

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
            str(milepost.osm_longitude),
            str(milepost.osm_latitude)
        ]
        output_writer.writerow(row)
