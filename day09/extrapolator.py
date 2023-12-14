#!/usr/bin/env python3
from itertools import pairwise


def stepdiff(seq: list):
    all_zero = True
    for q in [x == 0 for x in seq]:
        all_zero = all_zero and q
    if not all_zero:
        r = stepdiff([y - x for x, y in pairwise(seq)])
        return seq[-1] + r
    else:
        return seq[-1]


def main():
    histsum = 0
    with open("input", "r") as reader:
        line = reader.readline()
        while line != "":
            line = line.rstrip()
            oasis = [int(x) for x in line.split(" ")]
            histsum += stepdiff(oasis)
            line = reader.readline()
        print(histsum)


if __name__ == "__main__":
    main()
