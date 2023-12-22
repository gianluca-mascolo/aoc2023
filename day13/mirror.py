#!/usr/bin/env python3

CHARS = {'.','#'}

def printmap(valley: list,horizontal:int,vertical:int):
    pmap = []
    for line in valley:
        pmap.append(line.copy())
    for y,line in enumerate(pmap):
        if horizontal>0 and y==horizontal:
            print('\u2550'*len(line))
        msg=[str(c) for c in line]
        if vertical>0:
            msg.insert(vertical,'\u2551')
        print("".join(msg))

def reflection(valley: list):
    rowlen = len(valley[0])
    for seek in range(rowlen-1):
        is_mirror=[]
        for line in valley:
            for column in range(rowlen-seek):
                if seek+column == rowlen-column-1:
                    is_mirror.append(False)
                    break
                if seek+column > rowlen-column-1:
                    mirror_col = seek+column
                    break
                is_mirror.append(line[seek+column]==line[rowlen-column-1])
        if all(is_mirror):
            return mirror_col
    return 0

def transpose(valley: list):
    trans=[]
    for i in range(len(valley[0])):
        trans.append(['']*len(valley))
    
    for y,line in enumerate(valley):
        for x,value in enumerate(line):
            trans[x][y]=value
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
                vertical = 0
                horizontal = 0
                vertical = reflection(valley)
                if vertical == 0:
                    vertical=len(valley[0])-reflection(flip(valley))
                    if vertical == len(valley[0]):
                        vertical = 0
                horizontal = reflection(transpose(valley))
                if horizontal == 0:
                    horizontal=len(valley)-reflection(flip(transpose(valley)))
                    if horizontal == len(valley):
                        horizontal = 0
                printmap(valley,horizontal,vertical)
                print("")
                print(f"reflect vertical: {vertical} horizontal: {horizontal}")
                print("")

                mysum += vertical+100*horizontal
                valley = []
                count += 1
            else:
                valley.append([c for c in line if c in CHARS])
            line = reader.readline()
        print(f"part1: {mysum}")


if __name__ == "__main__":
    main()
