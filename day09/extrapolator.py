#!/usr/bin/env python3
from itertools import pairwise


def stepdiff(seq: list):
    if not all([x == 0 for x in seq]):
        r = stepdiff([y - x for x, y in pairwise(seq)])
        return (seq[0] - r[0], seq[-1] + r[1])
    else:
        return (0, 0)


def main():
    histsum = [0, 0]
    with open("input", "r") as reader:
        line = reader.readline()
        while line != "":
            line = line.rstrip()
            oasis = [int(x) for x in line.split(" ")]
            histsum[0] += stepdiff(oasis)[0]
            histsum[1] += stepdiff(oasis)[1]
            line = reader.readline()
        print(f"nextsum: {histsum[1]}, prev_sum: {histsum[0]}")


if __name__ == "__main__":
    main()
