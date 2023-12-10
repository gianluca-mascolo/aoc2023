#!/usr/bin/env python3
import re

class Number:
    def __init__(self):
        self.value = 0
        self.start = -1
        self.end = -1

class Symbol:
    position = -1

class Schematic:
    def __init__(self):
        self.numbers=[]
        self.symbols=[]
        self.partsum=0
        self.size=0
    def insert_number(self, value: int, start: int, end: int, line: int):
        n = Number()
        n.value=value
        n.start=start
        n.end=end
        self.numbers.append((line,n))
    def insert_symbol(self, position: int, line: int):
        s = Symbol()
        s.position=position
        self.symbols.append((line,s))
    def adjacent(self):
        for l,n in self.numbers:
            for sl,sp in self.symbols:
                if sl==l and (sp.position==(n.start-1) or sp.position==(n.end)):
                    self.partsum+=n.value
                elif abs(sl-l)==1 and sp.position>=(n.start-1) and sp.position<=(n.end):
                    self.partsum+=n.value

def main():
    digit_pattern = re.compile(r"\d+")
    symbol_pattern = re.compile(r"[^0-9.]")
    schema = Schematic()
    with open('input', 'r') as reader:
        line = reader.readline()
        line = line.rstrip()
        schema.size=len(line)
        line_number = 0
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            for match in digit_pattern.finditer(line):
                schema.insert_number(value=int(match.group()),start=match.start(),end=match.end(), line=line_number)
            for match in symbol_pattern.finditer(line):
                schema.insert_symbol(position=match.start(), line=line_number)
            line = reader.readline()
            line_number += 1
    schema.adjacent()
    print(f"Part number sum: {schema.partsum}")

if __name__ == "__main__":
    main()
