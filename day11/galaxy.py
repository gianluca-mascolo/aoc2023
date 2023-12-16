#!/usr/bin/env python3
import sys
from itertools import combinations


def main():
    galaxy = []
    y = 0
    while line := sys.stdin.readline():
        line = line.rstrip()
        x = 0
        for c in line:
            if c == "#":
                galaxy.append((x, y))
            x += 1
        y += 1
    sum_len=0
    for points in set(list(combinations(galaxy, 2))):
        # minimum steps: abs(x1-x2)+abs(y1-y2)
        sum_len+=abs(points[0][0]-points[1][0])+abs(points[0][1]-points[1][1])
    print(sum_len)

if __name__ == "__main__":
    main()
