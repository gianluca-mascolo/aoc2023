#!/bin/bash
INPUT_FILE="$1"
TOTAL_DAMAGED=0
LINES=$(cat "$INPUT_FILE" | wc -l)
PROGRESS=1
./bitgenerator.sh "$INPUT_FILE"
while read -r line; do {
    BITS="$(echo "$line" | cut -d ' ' -f 1 | tr -d '\n' | wc -c)"
    SELECT="$(echo "$line" | cut -d ' ' -f 1 | sed -r -e 's/\./0/g' -e 's/\?/./g' -e 's/#/1/g')"
    echo "Processing line $PROGRESS of $LINES ($BITS bits)"
    COMBINATIONS=$(echo "2^${BITS}" | bc)
    REGEX=""
    for DAMAGED in $(echo "$line" | cut -d ' ' -f 2 | tr ',' ' '); do {
        REGEX="${REGEX}1{$DAMAGED}0+"
    }
    done
    REGEX="${REGEX%0+}"
    REGEX="(^|^0+)${REGEX}(0+$|$)"
    COUNT=$(head -n $COMBINATIONS binary-table  | sed -re "s/.*([01]{$BITS})/\1/" | grep -E "$SELECT" | grep -cE "$REGEX")
    echo "Matches: $COUNT"
    TOTAL_DAMAGED=$((TOTAL_DAMAGED+COUNT))
    PROGRESS=$((PROGRESS+1))
}
done < "$INPUT_FILE"
echo "Damaged: $TOTAL_DAMAGED"
exit 0
