#!/usr/bin/env python3

TILES = {".", "/", "\\", "-", "|"}
MOVE = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
REFLECT = {
    ".": {"R": {"R"}, "L": {"L"}, "U": {"U"}, "D": {"D"}},
    "/": {"R": {"U"}, "L": {"D"}, "U": {"R"}, "D": {"L"}},
    "\\": {"R": {"D"}, "L": {"U"}, "U": {"L"}, "D": {"R"}},
    "-": {"R": {"R"}, "L": {"L"}, "U": {"L", "R"}, "D": {"L", "R"}},
    "|": {"R": {"U", "D"}, "L": {"U", "D"}, "U": {"U"}, "D": {"D"}},
}


class Tile:
    def __init__(self, kind: str):
        self.kind = kind

    def reflect(self, direction: str):
        return REFLECT[self.kind][direction].copy()


class TileMap:
    def __init__(self):
        self.map = []
        self.rows = 0
        self.cols = 0

    def print(self):
        for row in self.map:
            print("".join([tile.kind for tile in row]))

    def fence(self, x: int, y: int):
        return x >= 0 and x < self.cols and y >= 0 and y < self.rows

    def border(self):
        b = []
        b.extend([(x, 0, "D") for x in range(self.cols)])
        b.extend([(x, self.rows - 1, "U") for x in range(self.cols)])
        b.extend([(0, y, "R") for y in range(self.rows)])
        b.extend([(self.cols - 1, y, "L") for y in range(self.rows)])
        return b


class Beam:
    def __init__(self, x: int, y: int, speed: int, direction: str):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction


class BeamMap:
    def __init__(self, grid: TileMap, start: Beam):
        self.start = start
        self.grid = grid

    def __iter__(self):
        self.beam = [[self.start]]
        self.seen = set()
        return self

    def __next__(self):
        touch = set()
        current_position = [path[-1] for path in self.beam]
        for ray, current in enumerate(current_position):
            if current.speed > 0:
                touch.add((current.x, current.y))
                delta = self.grid.map[current.y][current.x].reflect(current.direction)
            else:
                delta = set()

            for fork, new_direction in enumerate(delta):
                r = ray
                if fork > 0:
                    self.beam.append(self.beam[ray].copy())
                    r = -1
                dx, dy = MOVE[new_direction]
                x = current.x + dx
                y = current.y + dy
                if self.grid.fence(x, y) and (x, y, new_direction) not in self.seen:
                    self.beam[r].append(Beam(x, y, 1, new_direction))
                    self.seen.add((x, y, new_direction))
                else:
                    self.beam[r][-1] = Beam(x, y, 0, current.direction)
        if all(r[-1].speed == 0 for r in self.beam) and not touch:
            raise StopIteration
        else:
            return touch


def main():
    grid = TileMap()
    with open("input", "r") as reader:
        y = 0
        line = reader.readline()
        while line != "":
            grid.map.append([])
            line = line.rstrip()
            for x, c in enumerate(line):
                if c in TILES:
                    grid.map[y].append(Tile(c))
            line = reader.readline()
            y += 1
    grid.rows = y
    grid.cols = x + 1
    beam_length = []
    for beam_x, beam_y, beam_direction in grid.border():
        beam = BeamMap(grid=grid, start=Beam(beam_x, beam_y, 1, beam_direction))
        visited_tiles = set()
        for step in beam:
            visited_tiles |= step
        if beam_x == 0 and beam_y == 0 and beam_direction == "R":
            print(f"Part 1: {len(visited_tiles)}")
        beam_length.append(len(visited_tiles))
    print(f"Part 2: {max(beam_length)}")


if __name__ == "__main__":
    main()
