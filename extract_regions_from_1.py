#!/usr/bin/env python3


"""
Extract region from the GeoJSON region files in folder '1'.
Put them into 'regions' folder with county subfolders with the same name as their region.
In these subfolders also put a file with the list of regions ('regions.txt').
"""

import json
import os
import re
from unidecode import unidecode

def main():
    for file in os.listdir('./1'):
        with open('./1/' + file) as original_region_file:
            data = json.load(original_region_file)

            country_name = file.split('.')[0]
            
            if not os.path.exists(f'./regions/{country_name}'):
                os.mkdir(f'./regions/{country_name}')

            regions_names = []

            for feature in data['features']:
                # for keyword search make sure to use lowercase, unidecoded etc.
                region_name = str(feature['properties']['NAME_1'])
                
                # make sure text is lowercase, trimmed string with only alphanumeric characters
                region_name = re.sub(r"(\w)([A-Z])", r"\1 \2", region_name).strip().lower()  # split camelcase, afterwards strip and lowercase
                region_name = re.sub(r'[^a-z0-9 ]+', '', region_name)  # lower alphanumeric characters only
                region_name = re.sub(r'\s+', ' ', region_name)  # remove multiple spaces and put a space in front to be able to find if keyword is at beginning of text

                regions_names.append(region_name)

                region_name_file = region_name.replace(' ', '_')
                with open(f'regions/{country_name}/{region_name_file}.json', 'w') as region_file:
                    json.dump(feature, region_file)


            with open(f'./regions/{country_name}/regions.txt', 'w') as regions_list_file:
                regions_list_file.write('\n'.join(regions_names))


            print(f'Regions from {country_name} extracted.')



if __name__ == '__main__':
    main()
