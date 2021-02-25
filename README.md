# ncn-milepost-openstreetmap-checker
A script to check National Cycle Network mileposts with OpenStreetMap data.

## NCN mileposts?

All across the UK there are these things called [Millennium Mileposts].
Keep an eye out for them while cycling around!

## What is this script for?

According to the [OpenStreetMap wiki][Sustrans Millennium Mileposts], there
are ~1000 known mileposts. OpenStreetMap.org does not map all of these mileposts,
and even for the ones that are, it's possible the data is incomplete, such as missing
reference number or having the incorrect milepost type.

To make sure the wiki and or map is up to date and consistent, this script
can be used as a tool to identify which mileposts are missing or incorrect.

## Data sources

* Sustrans IDs and other milepost data are from the OpenStreetMap wiki page on 
  [Sustrans Millennium Mileposts]
* OSM data from using the [Overpass API]

## Usage

Make sure to install python3.

```
cd checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python check.py
```

This will generate a CSV file in the `output` folder.

## Viewing the data

While the CSV is useful, I've also created a viewer to render the CSV data into something more accessible at:
https://ncn-milepost-openstreetmap-checker.leifgehrmann.com

You can run the viewer on your own machine by running the following:

(Make sure to install [NPM](https://nodejs.org/en/download/) and [Hugo](https://gohugo.io/getting-started/installing/))

```
cd viewer
npm install
hugo server
```

[Millennium Mileposts]: https://en.wikipedia.org/wiki/National_Cycle_Network#Mileposts
[Sustrans Millennium Mileposts]: https://wiki.openstreetmap.org/wiki/Sustrans_Millennium_Mileposts
[Overpass API]: https://overpass-api.de
