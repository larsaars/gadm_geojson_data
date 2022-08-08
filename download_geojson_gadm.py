#!/usr/bin/env python3

"""
Download geojson files form GADM for given level, unzip and put in folder.
"""

import requests
import os
import zipfile
import sys


def printerr(*args, **kwargs):
    """
    Print error message to stderr.
    """
    print(*args, file=sys.stderr, **kwargs)


def download(level):

    if not os.path.exists(f'./{level}'):
        os.mkdir(f'./{level}')


    with open('./countries.txt', 'r') as f:
        countries = f.read().splitlines()

    for country in countries:
        try:
            with open(f'./{level}/{country}.json', 'wb') as f:
                f.write(requests.get(f'https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_{country.upper()}_{level}.json').content)
            

            print(f'{country} downloaded for level {level}')
        except Exception as e:
            printerr(f'Error downloading {country} for level {level}')



if __name__ == '__main__':
    for i in range(5):
        download(i)
        print(f'Level {i} done')
