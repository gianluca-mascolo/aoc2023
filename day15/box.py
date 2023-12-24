#!/usr/bin/env python3
import re
import sys


class Step:
    def __init__(self, s: str):
        tok = re.split("([=-])", s)
        self.label = tok[0]
        self.op = tok[1]
        self.focal = int(f"0{tok[2]}")
        self.number = hashstr(tok[0])


def hashstr(s: str):
    res = 0
    for c in s:
        res = ((res + ord(c)) * 17) % 256
    return res


def main():
    initseq = []
    while line := sys.stdin.readline():
        line = line.rstrip()
        initseq.extend(line.split(","))
    print("Part 1: {}".format(sum(hashstr(x) for x in initseq)))

    boxes = []
    for n in range(256):
        boxes.append([])
    for s in initseq:
        step = Step(s)
        labels = [lab for lab, foc in boxes[step.number]]
        if step.op == "-":
            if step.label in labels:
                boxes[step.number].pop(labels.index(step.label))
        elif step.op == "=":
            if step.label not in labels:
                boxes[step.number].append((step.label, step.focal))
            else:
                boxes[step.number][labels.index(step.label)] = (step.label, step.focal)
    focus_power = 0
    for n, box in enumerate(boxes):
        if box:
            focus_power += sum([(n + 1) * (slot + 1) * lens[1] for slot, lens in enumerate(box)])
    print(f"Part 2: {focus_power}")


if __name__ == "__main__":
    main()
