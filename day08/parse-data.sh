cat example | sed -re 's/[ ()]+//g' | grep -v ^$ > example.parsed
cat example2 | sed -re 's/[ ()]+//g' | grep -v ^$ > example2.parsed
cat input | sed -re 's/[ ()]+//g' | grep -v ^$ > input.parsed
