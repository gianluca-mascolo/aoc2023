#!/usr/bin/env python3

TILES = {".", "/", "\\", "-", "|"}
MOVE = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


class Beam:
    def __init__(self, x: int, y: int, speed: int, direction: str):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.speed == other.speed and self.direction == other.direction


class Tile:
    def __init__(self, kind: str):
        self.kind = kind
        self.energized = False

    def reflect(self, direction: str):
        if self.kind == ".":
            return {direction}
        if self.kind == "/":
            if direction == "R":
                return {"U"}
            elif direction == "L":
                return {"D"}
            elif direction == "U":
                return {"R"}
            elif direction == "D":
                return {"L"}
        if self.kind == "\\":
            if direction == "R":
                return {"D"}
            elif direction == "L":
                return {"U"}
            elif direction == "U":
                return {"L"}
            elif direction == "D":
                return {"R"}
        if self.kind == "-":
            if direction == "R" or direction == "L":
                return {direction}
            elif direction == "U" or direction == "D":
                return {"L", "R"}
        if self.kind == "|":
            if direction == "U" or direction == "D":
                return {direction}
            elif direction == "L" or direction == "R":
                return {"U", "D"}


class TileMap:
    def __init__(self, startbeam: Beam):
        self.map = []
        self.rows = 0
        self.cols = 0
        self.startbeam = startbeam

    def print(self):
        for row in self.map:
            print("".join([tile.kind for tile in row]))

    def printenergy(self):
        for row in self.map:
            print("".join([(".", "#")[tile.energized] for tile in row]))

    def xray(self):
        for ray, path in enumerate(self.beam):
            print([(ray, b.x, b.y, b.speed, b.direction) for b in path])

    def __iter__(self):
        self.beam = [[self.startbeam]]
        self.seen = set()
        return self

    def __next__(self):
        touch = set()
        last_ray = []
        for path in self.beam:
            last_ray.append(path[-1])
        for ray, last in enumerate(last_ray):
            if last.speed > 0:
                touch.add((last.x, last.y))
                self.map[last.y][last.x].energized = True
                delta = self.map[last.y][last.x].reflect(last.direction)
            else:
                delta = set()
            if len(delta) == 1:
                newdir = delta.pop()
                dx, dy = MOVE[newdir]
                if last.x + dx >= 0 and last.x + dx < self.cols and last.y + dy >= 0 and last.y + dy < self.rows and (last.x + dx, last.y + dy, newdir) not in self.seen:
                    self.beam[ray].append(Beam(last.x + dx, last.y + dy, 1, newdir))
                    self.seen.add((last.x + dx, last.y + dy, newdir))
                else:
                    self.beam[ray][-1] = Beam(last.x, last.y, 0, last.direction)
            elif len(delta) == 2:
                self.beam.append(self.beam[ray].copy())
                for r in [ray, -1]:
                    newdir = delta.pop()
                    dx, dy = MOVE[newdir]
                    if last.x + dx >= 0 and last.x + dx < self.cols and last.y + dy >= 0 and last.y + dy < self.rows and (last.x + dx, last.y + dy, newdir) not in self.seen:
                        self.beam[r].append(Beam(last.x + dx, last.y + dy, 1, newdir))
                        self.seen.add((last.x + dx, last.y + dy, newdir))
                    else:
                        self.beam[r][-1] = Beam(last.x, last.y, 0, last.direction)
        if all(r[-1].speed == 0 for r in self.beam):
            raise StopIteration
        else:
            return touch


def main():
    grid = iter(TileMap(Beam(0, 0, 1, "R")))
    with open("example", "r") as reader:
        y = 0
        line = reader.readline()
        while line != "":  # The EOF char is an empty string
            grid.map.append([])
            line = line.rstrip()
            for x, c in enumerate(line):
                if c in TILES:
                    grid.map[y].append(Tile(c))
            # print(line)
            line = reader.readline()
            y += 1
    grid.rows = y
    grid.cols = x + 1
    print("Original map\n")
    grid.print()
    print("")
    for step in grid:
        pass

    print("Energized map\n")
    grid.printenergy()
    print("")
    total = 0
    for row in grid.map:
        for tile in row:
            if tile.energized:
                total += 1
    print(f"Energized tiles:  {total}")


if __name__ == "__main__":
    main()
