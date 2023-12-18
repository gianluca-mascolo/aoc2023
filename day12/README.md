## Part 1

`./repair.sh example`
it will generate a binary-table file with the necessary number of bits (20 in my input) containing all possible values of combinations.
Then the input is interpreted with . = 0 and # = 1 and filtered with grep.

```
]$ ./repair.sh example 
Processing line 1 of 25 (7 bits)
Matches: 1
Processing line 2 of 25 (14 bits)
Matches: 4
Processing line 3 of 25 (15 bits)
Matches: 1
Processing line 4 of 25 (13 bits)
Matches: 1
Processing line 5 of 25 (19 bits)
Matches: 4
Processing line 6 of 25 (12 bits)
Matches: 10
Damaged: 21
```
