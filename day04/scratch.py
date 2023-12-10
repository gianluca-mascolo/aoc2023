#!/usr/bin/env python3

class ScratchLog:
    def __init__(self, log_line: str):
        sl=log_line.split(": ")[1].strip()
        self.own={int(x) for x in sl.split(" | ")[0].split(" ") if x!=''}
        self.winning={int(x) for x in sl.split(" | ")[1].split(" ") if x!=''}
    def points(self) -> int:
        c = len(self.own)-len(self.own-self.winning)
        if c>0:
            return 2**(c-1)
        else:
            return 0

def main():
    total = 0
    with open('input', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            scratch=ScratchLog(line)
            total+=scratch.points()
            line = reader.readline()
    print(total)

if __name__ == "__main__":
    main()
