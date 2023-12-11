#!/bin/bash
csplit -z -f maps- example '/.*:/' '{*}'
for m in maps-*; do
	MAP_NAME=$(grep -oE "^[^0-9:]+" $m | cut -d ' ' -f 1)
	cat $m  | sed -re 's/^[^0-9]+//' | grep -v ^$ | sort -t ' ' -k 1 -n > ${MAP_NAME}.map
done
rm -f maps-*
