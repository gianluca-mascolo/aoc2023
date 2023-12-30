#!/bin/bash
set -euo pipefail
BASIC_FILE="$1"
D64_FILE="${BASIC_FILE%.bas}.d64"
PRG_FILE="${BASIC_FILE%.bas}.prg"
PRG_NAME="${BASIC_FILE%.bas}"

echo "Converting inputs to PETSCII"
for f in input example; do ./ascii2petscii.sh $f; done
echo "Compile BASIC $BASIC_FILE into $PRG_FILE"
./mospeed.sh "${BASIC_FILE}" -target="${PRG_FILE}" -platform=c64
echo "Creating disk $D64_FILE"
c1541 -format aoc2023,01 d64 "${D64_FILE}" -attach "${D64_FILE}" -write "${PRG_FILE}" "${PRG_NAME}" -write example.petscii "example,s" -write input.petscii "input,s"
echo "Running on Commodore 64"
x64 -autostart "${D64_FILE}"
