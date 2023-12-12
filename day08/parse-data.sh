#!/bin/bash

for FILE in example example2 example3 input; do
    [ -f "$FILE" ] &&  cat "$FILE" | sed -re 's/[ ()]+//g' | grep -v ^$ > "${FILE}.parsed"
done
