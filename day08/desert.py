#!/usr/bin/env python3
def main():
    with open("input.parsed", "r") as reader:
        line = reader.readline()
        line.rstrip()
        directions = [d == "R" for d in list(line) if d == "R" or d == "L"]
        nodes = {}
        line = reader.readline()
        while line != "":  # The EOF char is an empty string
            line = line.rstrip()
            nodes[line.split("=")[0]] = tuple(line.split("=")[1].split(","))
            line = reader.readline()
        step = "AAA"
        count = 0
        index = 0
        while step != "ZZZ":
            print(nodes[step])
            step = nodes[step][directions[index]]
            count += 1
            index += 1
            index %= len(directions)
        print(count)


if __name__ == "__main__":
    main()
