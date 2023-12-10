#!/usr/bin/env python3

BAG = {'red': 12, 'green': 13, 'blue': 14}
COLORS = {"red", "green", "blue"}

class CubeSet:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

class GameLog:
    def __init__(self, log_line: str):
        self.number=int(log_line.split(": ")[0].split(" ")[1])
        self.cubesets=[]
        cl=log_line.split(": ")[1].strip()
        for cube_string in cl.split("; "):
            self.cubesets.append(self.__extract(cube_string))
    def __extract(self, cube_string: str) -> CubeSet:
        cs = CubeSet()
        for cube in cube_string.split(", "):
            setattr(cs,cube.split(" ")[1],int(cube.split(" ")[0]))
        return cs
    def is_possible(self) -> bool:
        for cs in self.cubesets:
            for color in COLORS:
                if getattr(cs,color)>BAG[color]:
                    return False
        return True
    def power(self) -> int:
        f = CubeSet()
        for cs in self.cubesets:
            for color in COLORS:
                if getattr(cs,color)>getattr(f,color):
                    setattr(f,color,getattr(cs,color))
        return f.red*f.blue*f.green
    

def main():
    idsum = 0
    powsum = 0
    with open('input', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            game=GameLog(line)
            print(f"-- Game number: {game.number} is possible: {('No','Yes')[game.is_possible()]} power: {game.power()}")
            powsum += game.power()
            if game.is_possible():
                idsum += game.number
            line = reader.readline()
    print(f"Sum of possibles IDs: {idsum}, Sum of powers: {powsum}")

if __name__ == "__main__":
    main()
