#!/usr/bin/env python3

"""
Create a region-country mapper.

Also contain information about the centroid of each region.
"""

import json
import os
from shapely.geometry import shape


def main():
    mapping = {}

    with open('./countries/countries.txt', 'r') as countries_file:
        countries_countries = countries_file.read().splitlines()

    
    countries_regions = os.listdir('./regions')

    for country in countries_countries:
        # add values to the mapper
        if country in countries_regions:
            with open(f'./regions/{country}/regions.txt', 'r') as region_file:
                regions = list(filter(None, region_file.read().splitlines()))

            mapping[country] = {}

            # for every region find the centroid and add it to the mapper as well
            for region in regions:
                with open(f'./regions/{country}/{region.replace(" ", "_")}.json', 'r') as region_file:
                    region_json = json.load(region_file)
                    region_geometry = shape(region_json['features'][0]['geometry'])
                    centroid = region_geometry.centroid.coords[0]

                    mapping[country][region] = {'lat': centroid[1], 'lon': centroid[0]}
        else:
            mapping[country] = {}

    




    with open('./country_region_mapping.json', 'w') as mapping_file:
        json.dump(mapping, mapping_file)


if __name__ == '__main__':
    main()
