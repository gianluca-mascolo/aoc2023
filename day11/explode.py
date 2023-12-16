#!/usr/bin/env python3
import argparse
import sys
from itertools import combinations


class Space:
    def __init__(self, galaxy: bool):
        self.galaxy = galaxy
        self.size = 1


class Universe:
    def __init__(self):
        self.map = []
        self.sizex = 0
        self.sizey = 0

    def append(self, x: int, y: int, s: Space):
        self.map.append({"coord": (x, y), "space": s})
        if x >= self.sizex:
            self.sizex = x + 1
        if y >= self.sizey:
            self.sizey = y + 1

    def print(self):
        y = 0
        for p in self.map:
            if p["coord"][1] > y:
                y += 1
                print("")
            if p["space"].size == 1:
                c = "."
            else:
                c = "+"
            print((c, "#")[p["space"].galaxy], end="")
        print("")

    def expand(self, inflation: int):
        for y in range(self.sizey):
            if not any(p["space"].galaxy for p in self.map if p["coord"][1] == y):
                for i in self.map:
                    if i["coord"][1] == y:
                        i["space"].size = inflation
        for x in range(self.sizex):
            if not any(p["space"].galaxy for p in self.map if p["coord"][0] == x):
                for i in self.map:
                    if i["coord"][0] == x:
                        i["space"].size = inflation

    def galaxies(self):
        return [p["coord"] for p in self.map if p["space"].galaxy]

    def travel(self, p1: tuple, p2: tuple):
        if p1[0] < p2[0]:
            x1 = p1[0]
            x2 = p2[0]
        else:
            x1 = p2[0]
            x2 = p1[0]
        if p1[1] < p2[1]:
            y1 = p1[1]
            y2 = p2[1]
        else:
            y1 = p2[1]
            y2 = p1[1]
        x_segment = [p["space"].size for p in self.map if p["coord"][0] > x1 and p["coord"][0] <= x2 and p["coord"][1] == y1]
        y_segment = [p["space"].size for p in self.map if p["coord"][1] > y1 and p["coord"][1] <= y2 and p["coord"][0] == x2]
        return sum(x_segment) + sum(y_segment)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--speed", help="Expansion speed", type=int, default=2)
    parser.add_argument("-p", "--print", help="Print expanded universe", action="store_true")
    args = parser.parse_args()
    universe = Universe()
    y = 0
    while line := sys.stdin.readline():
        line = line.rstrip()
        x = 0
        for c in line:
            universe.append(x, y, Space(c == "#"))
            x += 1
        y += 1
    universe.expand(args.speed)
    if args.print:
        universe.print()
    travel_sum = 0
    combos = len(set(list(combinations(universe.galaxies(), 2))))
    step = 1
    for points in set(list(combinations(universe.galaxies(), 2))):
        d = universe.travel(*points)
        if args.print:
            print(f"[{step}/{combos}] Travel between {points}: {d}")
        travel_sum += d
        step += 1
    print(travel_sum)


if __name__ == "__main__":
    main()
