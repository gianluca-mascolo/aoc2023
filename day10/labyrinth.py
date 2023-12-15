#!/usr/bin/env python3
import sys

SYMBOLS = {"-": "\u2550", "|": "\u2551", "F": "\u2554", "7": "\u2557", "L": "\u255A", "J": "\u255D", "S": "*", ".": "."}

PIPES = {"-": {"east", "west"}, "|": {"north", "south"}, "F": {"south", "east"}, "7": {"south", "west"}, "L": {"north", "east"}, "J": {"north", "west"}}

CONNECTIONS = {"east": "west", "west": "east", "north": "south", "south": "north"}


def printmap(lab: list):
    for line in lab:
        for c in line:
            print(SYMBOLS[c], end="")
        print("")


def findstart(lab: list):
    for y, line in enumerate(lab):
        for x, c in enumerate(line):
            if c == "S":
                return (y, x)


def main():
    labyrinth_map = []
    while line := sys.stdin.readline():
        line = line.rstrip()
        labyrinth_map.append([c for c in line if c in SYMBOLS])
    y, x = findstart(labyrinth_map)
    for start in PIPES:
        labyrinth_map[y][x] = start
        num_connections = 0
        for conn in PIPES[start]:
            if x + 1 < len(labyrinth_map) and labyrinth_map[y][x + 1] in PIPES and conn == "east" and "west" in PIPES[labyrinth_map[y][x + 1]]:
                num_connections += 1
            if y + 1 < len(labyrinth_map) and labyrinth_map[y + 1][x] in PIPES and conn == "south" and "north" in PIPES[labyrinth_map[y + 1][x]]:
                num_connections += 1
            if x - 1 > 0 and labyrinth_map[y][x - 1] in PIPES and conn == "west" and "east" in PIPES[labyrinth_map[y][x - 1]]:
                num_connections += 1
            if y - 1 > 0 and labyrinth_map[y - 1][x] in PIPES and conn == "north" and "south" in PIPES[labyrinth_map[y - 1][x]]:
                num_connections += 1
        if num_connections == 2:
            break
    printmap(labyrinth_map)
    print(x, y)
    walk_to = list(PIPES[labyrinth_map[y][x]])[0]
    steps = 0
    nx = x
    ny = y
    while True:
        print(f"[{steps}] {walk_to} -> ", end="")
        if walk_to == "east":
            dx = 1
            dy = 0
        elif walk_to == "north":
            dy = -1
            dx = 0
        elif walk_to == "south":
            dx = 0
            dy = 1
        elif walk_to == "west":
            dx = -1
            dy = 0
        nx += dx
        ny += dy
        walk_to = list(PIPES[labyrinth_map[ny][nx]] - {CONNECTIONS[walk_to]})[0]
        print(f"{walk_to} {nx} {ny} ({x} {y})")
        if nx == x and ny == y:
            break
        steps += 1
    print(int((steps + 1) / 2))


if __name__ == "__main__":
    main()
