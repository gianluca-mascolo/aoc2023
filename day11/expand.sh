#!/bin/bash
set -euo pipefail

transpose() {
    local FILENAME
    local n
    local line
    n=0
    while read -r line; do
        {
            FILENAME=$(printf "trans%04d" $n)
            echo "$line" | sed -re 's/(.)/\1\n/g' >"/tmp/$FILENAME"
            n=$((n + 1))
        }
    done
    paste --delimiters="" /tmp/trans* | grep -v ^$
    rm -f /tmp/trans*
}

expand() {
    local line
    while read -r line; do
        {
            echo "$line"
            echo "$line" | grep --color=never -E "^\.+$" || true
        }
    done
}

TMP_MAP=$(mktemp)
TMP_TRANS="$(mktemp)"
expand >"$TMP_MAP"
transpose <"$TMP_MAP" >"$TMP_TRANS"
expand <"$TMP_TRANS" >"$TMP_MAP"
transpose <"$TMP_MAP" >"$TMP_TRANS"
cat "$TMP_TRANS"
[ -f "$TMP_MAP" ] && rm -f "$TMP_MAP"
[ -f "$TMP_TRANS" ] && rm -f "$TMP_TRANS"
