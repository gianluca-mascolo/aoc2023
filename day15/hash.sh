#!/bin/bash
set -euo pipefail

TOTAL=0
HASH=0
while read -r -n1 ch; do
    {
        CHAR=$(echo "$ch" | tr -dc '[:graph:]') #chomp
        if [ -n "${CHAR:+is_set}" ]; then
            {
                if [ "$CHAR" = "," ]; then {
                    TOTAL=$((TOTAL + HASH))
                    HASH=0
                }; else
                    {
                        ASCIIVAL=$(printf '%02d' "'$CHAR")
                        HASH=$(((HASH + ASCIIVAL) * 17 % 256))
                    }
                fi
            }
        fi
    }
done
echo $((TOTAL + HASH))
