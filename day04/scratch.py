#!/usr/bin/env python3


class ScratchLog:
    def __init__(self, log_line: str):
        sl = log_line.split(": ")[1].strip()
        self.own = {int(x) for x in sl.split(" | ")[0].split(" ") if x != ""}
        self.winning = {int(x) for x in sl.split(" | ")[1].split(" ") if x != ""}

    def points(self) -> int:
        if self.matching() > 0:
            return 2 ** (self.matching() - 1)
        else:
            return 0

    def matching(self) -> int:
        return len(self.own) - len(self.own - self.winning)


def main():
    sumpoints = 0
    with open("input", "r") as reader:
        line = reader.readline()
        card = 0
        copies = []
        while line != "":
            line = line.rstrip()
            scratch = ScratchLog(line)
            if len(copies) <= card:  # If there are no copies of the card
                copies.append(1)  # put this card on the stack
            else:
                copies[card] += 1  # else count it as an additional copy

            # sum the number of winning (matching)
            for x in range(card + 1, card + 1 + scratch.matching()):
                if len(copies) <= x:
                    copies.append(0)
                copies[x] += copies[card]
            sumpoints += scratch.points()
            line = reader.readline()
            card += 1
    sumcards = 0
    for c in copies:
        sumcards += c
    print(f"Points: {sumpoints} Cards: {sumcards}")


if __name__ == "__main__":
    main()
