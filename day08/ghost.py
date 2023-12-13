#!/usr/bin/env python3
import math


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
    current = [n for n in nodes.keys() if n.endswith("A")]
    node_iters = []
    for nd in current:
        node_iters.append(iter(NodeMap(nodes=nodes, start=nd, directions=directions)))
    steps = 0
    ends_with_z = [-1] * len(current)  # record the first step number that ends with a 'Z' for each track
    stop_cycle = False
    while not stop_cycle:
        msg = " ".join(current)
        print(f"[{steps}] {msg} -> ", end="")
        for idx, node_iter in enumerate(node_iters):
            if ends_with_z[idx] == -1:
                current[idx] = next(node_iter)
                if current[idx].endswith("Z"):
                    ends_with_z[idx] = steps + 1
        msg = " ".join(current)
        print(msg)
        steps += 1
        stop_cycle = True
        for q in [x != -1 for x in ends_with_z]:
            stop_cycle = stop_cycle and q
    print(math.lcm(*ends_with_z))


if __name__ == "__main__":
    main()
