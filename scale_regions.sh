#!/usr/bin/env bash

mkdir regions_scaled

for c in $(ls regions)
do
    mkdir regions_scaled/$c

    cd regions/$c
    regions_folder=$(echo *.json)
    cd ../..

    echo "Rescaling $c"

    for r in $(echo "${regions_folder}")
    do
        mapshaper "./regions/${c}/${r}" -simplify dp 25% keep-shapes -o format=geojson "./regions_scaled/${c}/${r}"
        cp "./regions/${c}/regions.txt" "./regions_scaled/${c}/regions.txt"
    done
done

# rm -rf regions
# mv regions_scaled regions
