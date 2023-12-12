#!/usr/bin/env python3


class NodeMap:
    def __init__(self, nodes: dict, start: str, directions: list):
        self.nodes = nodes
        self.current = start
        self.directions = directions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self.current
        next_value = self.nodes[current][self.directions[self.index]]
        self.index += 1
        self.index %= len(self.directions)
        self.current = next_value
        return next_value


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
        current_node = "AAA"
        node_map = NodeMap(nodes=nodes, start=current_node, directions=directions)
        node_iter = iter(node_map)
        steps = 0
        while current_node != "ZZZ":
            print(f"{current_node} -> ", end="")
            current_node = next(node_iter)
            print(current_node)
            steps += 1
        print(steps)


if __name__ == "__main__":
    main()
