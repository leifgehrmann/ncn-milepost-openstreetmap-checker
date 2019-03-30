# ncn-milepost-openstreetmap-checker
A script to check National Cycle Network mileposts with OpenStreetMap data.

## NCN mileposts?

All across the UK there are these things called [Millennium Mileposts].
Keep an eye out for them while cycling around!

## What is this script for?

According to the [OpenStreetMap wiki][Sustrans Millennium Mileposts], there
are 846 known mileposts (Although in theory there should be 1000 of them).
However, only 394 mileposts have been added to OpenStreetMap as of 2019-03-30.

To make sure the wiki and or map is up to date and consistent, this script
can be used as a tool to identify which mileposts are missing or incorrect.

## Data sources

* Sustrans IDs are requested from the OpenStreetMap wiki page on 
  [Sustrans Millennium Mileposts]
* OSM data is requested using the [Overpass API]

## Usage

Make sure python3 is installed.

```
make install
make check
```


[Millennium Mileposts]: https://en.wikipedia.org/wiki/National_Cycle_Network#Mileposts
[Sustrans Millennium Mileposts]: https://wiki.openstreetmap.org/wiki/Sustrans_Millennium_Mileposts
[Overpass API]: https://overpass-api.de
