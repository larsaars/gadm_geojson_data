#!/usr/bin/env bash

for i in {0..4}
do
    for file in $(find $i/*.json -type f)
    do
        cat $file | python -mjson.tool > "${file}0" && mv "${file}0" $file
    done
done

