#!/usr/bin/env python3
import csv
import geojson
import requests

def main():
    request = requests.get("https://www.opengov-muenchen.de/dataset/a1982d8e-7afe-4f23-a2f3-3189f1d0b652/resource/ea74add7-b61a-4511-86df-02c9263257ce/download/141212lhmwertstoffhoefealleattributebearb.csv")
    text = request.text.split("\n")
    content = csv.DictReader(text, delimiter=";")

    locations = []
    for line in content:
        point = geojson.Point((float(line["longitude"]),
                               float(line["latitude"])
                              ))
        locations.append(geojson.Feature(geometry=point, properties=line))

    feature_collection = geojson.FeatureCollection(locations)

    with open("wertstoffhoefe-muenchen.geojson", "w") as outfile:
        geojson.dump(feature_collection, outfile, indent=2)

if __name__ == "__main__":
    main()
