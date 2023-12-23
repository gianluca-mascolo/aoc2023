#!/usr/bin/env python3
    
class RockPlatform:
    def __init__(self):
        self.map = []
        self.cols = 0
        self.rows = 0
    def column(self,x: int):
        return([t for t in self.map if t[0]==x])
    def row(self,y: int):
        return([t for t in self.map if t[1]==y])
    def rollup(self,rock: tuple, s: int):
        x,y,c = rock
        if c == 'O' and s<y:
            self.write(x,y,'.')
            self.write(x,s,'O')

    def write(self,x:int,y:int,c:str):
        for pos,t in enumerate(self.map):
            if t[0]==x and t[1]==y:
                self.map[pos]=(x,y,c)

    def print(self):
        for r in range(self.rows):
            print("".join([ c for x,y,c in self.row(r) ]))
        print("")


def main():
    with open("input", "r") as reader:
        line = reader.readline()
        y = 0
        plat = RockPlatform()
        while line != "":  # The EOF char is an empty string
            line = line.rstrip()
            for x,c in enumerate(line):
                plat.map.append((x,y,c))
            line = reader.readline()
            y+=1
    plat.cols = x+1
    plat.rows = y
    for col in range(plat.cols):
        stop = -1
        for x,y,c in plat.column(col):
            if c == '#':
                stop = y
            elif c == 'O':
                stop += 1
                plat.rollup((x,y,c),stop)

    balance = 0
    for r in range(plat.rows):
        balance += sum([int(c=='O') for x,y,c in plat.row(r)])*(plat.rows-r)
    print(balance)

if __name__ == "__main__":
    main()
