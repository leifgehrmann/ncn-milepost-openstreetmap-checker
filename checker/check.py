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

with open('../output/output.csv', mode='w') as output_file:
    output_writer = csv.writer(
        output_file,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_MINIMAL
    )

    headers = [
        'Unique Sustrans Ref',
        'Listed in Wiki',
        'Mapped in OSM',
        'Mapped completely in OSM'
        'Mapped and listed completely in OSM and Wiki'
        'Wiki Sustrans Ref',
        'OSM Sustrans Ref',
        'Valid Wiki Sustrans Ref',
        'Valid OSM Sustrans Ref',
        'Matching Sustrans Ref',
        'Wiki Milepost Type',
        'OSM Milepost Type',
        'Valid Wiki Milepost Type'
        'Valid OSM Milepost Type'
        'Matching Milepost Type'
        'Node Id in wiki',
        'Node Id in OSM',
        'Valid Node Id in Wiki',
        'Matching Node Id',
        'Node longitude',
        'Node latitude',
        'Wiki Region',
        'Wiki Location',
    ]

    output_writer.writerow(headers)

    # True/False to yes/No
    def tf_2_yn(value: bool) -> str:
        return 'Yes' if value else 'No'

    # Format None as "-"
    def none_2_hyphen(value: bool) -> str:
        return value if value is not None else '-'

    for milepost in milepost_collection.get_mileposts():
        row = [
            none_2_hyphen(milepost.sustrans_ref),
            tf_2_yn(milepost.is_in_wiki()),
            tf_2_yn(milepost.is_in_osm()),
            tf_2_yn(milepost.is_mapped_completely_in_osm()),
            tf_2_yn(milepost.is_mapped_and_listed_completely_in_osm_and_wiki()),
            none_2_hyphen(milepost.wiki_sustrans_ref),
            none_2_hyphen(milepost.osm_sustrans_ref),
            tf_2_yn(milepost.has_valid_wiki_sustrans_ref()),
            tf_2_yn(milepost.has_valid_osm_sustrans_ref()),
            tf_2_yn(milepost.has_matching_sustrans_ref()),
            none_2_hyphen(milepost.wiki_milepost_type),
            none_2_hyphen(milepost.osm_milepost_type),
            tf_2_yn(milepost.has_valid_wiki_milepost_type()),
            tf_2_yn(milepost.has_valid_osm_milepost_type()),
            tf_2_yn(milepost.has_matching_milepost_type()),
            none_2_hyphen(milepost.wiki_osm_link),
            none_2_hyphen(milepost.osm_id),
            tf_2_yn(milepost.has_valid_node_id_in_wiki()),
            tf_2_yn(milepost.has_matching_node_id()),
            ('%f' % milepost.osm_longitude) if milepost.osm_longitude is not None else '-',
            ('%f' % milepost.osm_latitude) if milepost.osm_latitude is not None else '-',
            none_2_hyphen(milepost.wiki_region),
            none_2_hyphen(milepost.wiki_location),
        ]
        output_writer.writerow(row)
