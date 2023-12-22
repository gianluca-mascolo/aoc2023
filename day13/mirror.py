#!/usr/bin/env python3


def printmap(valley: list, horizontal: int, vertical: int):
    pmap = []
    for line in valley:
        pmap.append(line.copy())
    for y, line in enumerate(pmap):
        if horizontal > 0 and y == horizontal:
            print("\u2550" * len(line))
        msg = [str(c) for c in line]
        if vertical > 0:
            msg.insert(vertical, "\u2551")
        print("".join(msg))


def reflection(valley: list):
    rowlen = len(valley[0])
    for seek in range(rowlen % 2, rowlen - 1, 2):
        is_mirror = []
        for line in valley:
            for dc in range(int((rowlen - seek) / 2)):
                is_mirror.append(line[seek + dc] == line[rowlen - dc - 1])
        if all(is_mirror):
            return int(seek + (rowlen - seek) / 2)
    return 0


def transpose(valley: list):
    trans = []
    for i in range(len(valley[0])):
        trans.append([""] * len(valley))

    for y, line in enumerate(valley):
        for x, value in enumerate(line):
            trans[x][y] = value
    return trans


def flip(valley: list):
    f = []
    for line in valley:
        f.append(line.copy())
    for line in f:
        line.reverse()
    return f


def main():
    with open("input", "r") as reader:
        count = 1
        line = reader.readline()
        valley = []
        mysum = 0
        while line != "":
            line = line.rstrip()
            if line == "":
                print(f"Valley {count}")
                print("")
                vertical = reflection(valley)
                if not vertical:
                    if vertical := reflection(flip(valley)):
                        vertical = len(valley[0]) - vertical

                horizontal = reflection(transpose(valley))
                if not vertical and not horizontal:
                    if horizontal := reflection(flip(transpose(valley))):
                        horizontal = len(valley) - horizontal
                printmap(valley, horizontal, vertical)
                print("")
                print(f"reflect vertical: {vertical} horizontal: {horizontal}")
                print("")

                mysum += vertical + 100 * horizontal
                valley = []
                count += 1
            else:
                valley.append([c for c in line if c in {".", "#"}])
            line = reader.readline()
        print(f"part1: {mysum}")


if __name__ == "__main__":
    main()
