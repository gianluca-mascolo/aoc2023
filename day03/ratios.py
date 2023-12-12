#!/usr/bin/env python3
import math
import re


class Number:
    def __init__(self):
        self.value = 0
        self.start = -1
        self.end = -1


class Symbol:
    def __init(self):
        self.position = -1
        self.value = "."

    def is_star(self) -> bool:
        return self.value == "*"


class Schematic:
    def __init__(self):
        self.numbers = []
        self.symbols = []
        self.partsum = 0
        self.size = 0
        self.ratiosum = 0

    def insert_number(self, value: int, start: int, end: int, line: int):
        n = Number()
        n.value = value
        n.start = start
        n.end = end
        self.numbers.append((line, n))

    def insert_symbol(self, value: str, position: int, line: int):
        s = Symbol()
        s.position = position
        s.value = value
        self.symbols.append((line, s))

    def adjacent(self):
        for sl, sp in self.symbols:
            gear = []
            for nl, n in self.numbers:
                if abs(sl - nl) <= 1 and sp.position >= (n.start - 1) and sp.position <= (n.end):
                    self.partsum += n.value
                    if sp.is_star():
                        gear.append(n.value)
            if len(gear) > 1:
                self.ratiosum += math.prod(gear)


def main():
    digit_pattern = re.compile(r"\d+")
    symbol_pattern = re.compile(r"[^0-9.]")
    schema = Schematic()
    with open("input", "r") as reader:
        line = reader.readline()
        line = line.rstrip()
        schema.size = len(line)
        line_number = 0
        while line != "":  # The EOF char is an empty string
            line = line.rstrip()
            for match in digit_pattern.finditer(line):
                schema.insert_number(
                    value=int(match.group()),
                    start=match.start(),
                    end=match.end(),
                    line=line_number,
                )
            for match in symbol_pattern.finditer(line):
                schema.insert_symbol(value=match.group(), position=match.start(), line=line_number)
            line = reader.readline()
            line_number += 1
    schema.adjacent()
    print(f"Part number sum: {schema.partsum}")
    print(f"Ratio sum: {schema.ratiosum}")


if __name__ == "__main__":
    main()
