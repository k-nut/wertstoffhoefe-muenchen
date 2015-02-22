# wertstoffhoefe-muenchen
geojson converter and file for the open data dataset of the Wertstoffhöfe in München

The city of Munich/München publishes the location and some attributes of their recycling facilities in their open data portal.
They proivde the data in csv format and this script converts it to geojson for further use.

The link for the datasets is : https://www.opengov-muenchen.de/dataset/wertstoffhoefe

Since the original csv file is published under the [Datenlizenz Deutschland – Namensnennung – Version 2.0](https://www.govdata.de/dl-de/by-2-0) tihs
derivate has the same license.

The small python converter is published under the MIT license and needs python3 to run (because of python2 not being
able to deal with csv and unicode very well)
