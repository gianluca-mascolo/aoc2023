#!/usr/bin/env python3
import sys

SYMBOLS = {"-": "\u2550", "|": "\u2551", "F": "\u2554", "7": "\u2557", "L": "\u255A", "J": "\u255D", "S": "*", ".": ".", "X": " "}
PIPES = {"-": {"E", "W"}, "|": {"N", "S"}, "F": {"S", "E"}, "7": {"S", "W"}, "L": {"N", "E"}, "J": {"N", "W"}}
CONNECTIONS = {"E": "W", "W": "E", "N": "S", "S": "N"}
WALK = {"E": (1, 0), "W": (-1, 0), "N": (0, -1), "S": (0, 1)}


class Nodo:
    def __init__(self, x: int, y: int, pipe: str):
        self.coord = {"x": x, "y": y}
        self.pipe = pipe
        self.symbol = SYMBOLS[pipe]
        self.connect = PIPES[pipe] if pipe in PIPES else {}


class LabMap:
    def __init__(self):
        self.map = []
        self.sizex = -1
        self.sizey = -1

    def print(self):
        y = 0
        for node in self.map:
            if node.coord["y"] > y:
                y += 1
                print("")
            print(node.symbol, end="")
        print("")

    def get(self, x: int, y: int):
        for node in self.map:
            if node.coord == {"x": x, "y": y}:
                return node
        return None

    def update(self, x: int, y: int, pipe: str):
        for node in self.map:
            if node.coord == {"x": x, "y": y}:
                node.pipe = pipe
                node.connect = PIPES[pipe] if pipe in PIPES else {}
                node.symbol = SYMBOLS[pipe]

    def look(self, x: int, y: int, direction: str):
        if direction == "N" and y > 0:
            return self.get(x, y - 1).connect
        elif direction == "S" and y < self.sizey - 1:
            return self.get(x, y + 1).connect
        elif direction == "W" and x > 0:
            return self.get(x - 1, y).connect
        elif direction == "E" and x < self.sizex - 1:
            return self.get(x + 1, y).connect
        else:
            return {}

    def findstart(self):
        start_node = next(node for node in self.map if node.pipe == "S")
        sx = start_node.coord["x"]
        sy = start_node.coord["y"]
        for pipe in PIPES:
            self.update(sx, sy, pipe)
            total_connections = 0
            for connection in self.get(sx, sy).connect:
                if CONNECTIONS[connection] in self.look(sx, sy, connection):
                    total_connections += 1
            if total_connections == 2:
                break
        return start_node


def main():
    labyrinth = LabMap()
    y = 0
    while line := sys.stdin.readline():
        line = line.rstrip()
        for x, c in enumerate([s for s in line if s in SYMBOLS]):
            node = Nodo(x, y, c)
            labyrinth.map.append(node)
        y += 1
    labyrinth.sizey = y
    labyrinth.sizex = x + 1
    start_node = labyrinth.findstart()
    sx = start_node.coord["x"]
    sy = start_node.coord["y"]
    walk_to = next(iter(start_node.connect))
    x = sx
    y = sy
    steps = 0
    loop_nodes = []
    while True:
        loop_nodes.append({"x": x, "y": y})
        dx, dy = WALK[walk_to]
        walk_to = list(labyrinth.look(x, y, walk_to) - {CONNECTIONS[walk_to]})[0]
        x += dx
        y += dy
        if x == sx and y == sy:
            break
        steps += 1
    for node in labyrinth.map:
        if node.coord not in loop_nodes and node.pipe in PIPES:
            labyrinth.update(node.coord["x"], node.coord["y"], "X")
    labyrinth.print()
    print(f"Loop steps: {steps}")


if __name__ == "__main__":
    main()
