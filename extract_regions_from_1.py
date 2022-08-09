#!/usr/bin/env python3


"""
Extract region from the GeoJSON region files in folder '1'.
Put them into 'regions' folder with county subfolders with the same name as their region.
In these subfolders also put a file with the list of regions ('regions.txt').

Finally, scale down the GeoJSON to 25% with mapshaper.
"""

import json
import os

def main():
    for file in os.listdir('./1'):
        with open('./1/' + file) as f:
            data = json.load(f)

            country_name = file.split('.')[0]
            
            if not os.path.exists(f'./regions/{country_name}'):
                os.mkdir(f'./regions/{country_name}')

            regions = []

            for feature in data['features']:
                region_name = feature['properties']['NAME_1']
                regions.append(region_name)

                with open(f'regions/{country_name}/{region_name}.json', 'w') as f:
                    json.dump(feature, f)


            with open(f'./regions/{country_name}/regions.txt', 'w') as f:
                json.dump('\n'.join(regions), f)


            print(f'Regions from {country_name} extracted.')

            os.system(f'mapshaper ./regions/{country_name}/*.json -simplify dp 25% keep-shapes -o force format=geojson')

            print('GeoJSONs scaled down for {country_name}.')


if __name__ == '__main__':
    main()
