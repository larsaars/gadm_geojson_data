#!/usr/bin/env python3

"""
Create a region-country mapper.
"""

import json
import os


def main():
    """
    Create a region-country mapper.
    """

    mapping = {}

    with open('./countries/countries.txt', 'r') as countries_file:
        countries_countries = countries_file.read().splitlines()

    
    countries_regions = os.listdir('./regions')

    for country in countries_countries:
        if country in countries_regions:
            with open(f'./regions/{country}/regions.txt', 'r') as region_file:
                regions = region_file.read().splitlines()

            mapping[country] = regions
        else:
            mapping[country] = []



    with open('./country_region_mapping.json', 'w') as mapping_file:
        json.dump(mapping, mapping_file)


if __name__ == '__main__':
    main()
