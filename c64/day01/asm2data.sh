#!/bin/bash
set -euo pipefail
ASM_FILE="$1"
# My eyes are bleeding. This is ugly.
# It will convert hex values from an assembler file of 64MON Cartridge (See ASSEMBLER.md)
# and give you data lines to use in a basic program with poke
# e.g. ./asm2data.sh day01-assembler.asm
grep -E '^\.a' "${ASM_FILE}" | \
    sed -re 's/^.{9}//' | \
    sed -re 's/^(.{8})[ ].*/\1/' | \
    tr '[:lower:]' '[:upper:]' | \
    tr '[:blank:]' \\n | grep -v ^$ | \
    while read -r HEX; do echo "obase=10;ibase=16;$HEX" | bc; done | \
    tr \\n \, | sed -re 's/(([^,]+,){5})/\1\n/g' | sed -re 's/(.*),$/data \1/'
echo ""
