#!/bin/bash

TMPBIN=$(mktemp)
TMPREV=$(mktemp)
TMPOUT=$(mktemp)
TMPOUT2=$(mktemp)
MAXBITS="$(cat "$1" | cut -d ' ' -f 1 | wc -L)"
[ -f binary-table ] && rm -f binary-table
echo -e "0\n1" > "$TMPBIN"
for ((n=1;n<=MAXBITS-1;n++)); do {
    cat $TMPBIN | sed -re 's/.*([01])$/\1/' > "$TMPOUT"
    tac "$TMPOUT" > $TMPREV
    paste -d '' $TMPOUT $TMPBIN > $TMPOUT2
    paste -d '' "$TMPREV" "$TMPBIN"  >> $TMPOUT2
    cat $TMPOUT2 | sort -n > $TMPBIN
}
done
cat $TMPBIN > binary-table
[ -f "$TMPBIN" ] && rm -f "$TMPBIN"
[ -f "$TMPREV" ] && rm -f "$TMPREV"
[ -f "$TMPOUT" ] && rm -f "$TMPOUT"
[ -f "$TMPOUT2" ] && rm -f "$TMPOUT2"
