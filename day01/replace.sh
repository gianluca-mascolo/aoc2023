#!/bin/bash
for s in subset subset2; do
    while read SUBSET; do LITERAL=$(echo "$SUBSET" | cut -d ':' -f 1); VALUE=$(echo "$SUBSET" | cut -d ':' -f 2); sed -ri "s/$LITERAL/$VALUE/g" input; done < $s
done
