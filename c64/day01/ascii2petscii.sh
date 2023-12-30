#!/bin/sh
cat "$1" | tr '[:lower:]' '[:upper:]' | perl -pe 's/\n/\r/' > "${1}.petscii"
