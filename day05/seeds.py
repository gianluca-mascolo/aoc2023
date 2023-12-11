#!/usr/bin/env python3

class TranslationMap:
    def __init__(self, src: int, dst: int, span: int):
        self.src = src
        self.dst = dst
        self.span = span
    def translate(self, num: int) -> int:
        if num>=self.src and num<self.src+self.span:
            return num-self.src+self.dst
        else:
            return -1

def main():
    maps = {
        'seed-to-soil': [],
        'soil-to-fertilizer': [],
        'fertilizer-to-water': [],
        'water-to-light': [],
        'light-to-temperature': [],
        'temperature-to-humidity': [],
        'humidity-to-location': [],
    }
    for map_name, map_list in maps.items():
        with open(f'{map_name}.map', 'r') as reader:
            line = reader.readline()
            while line != '':  # The EOF char is an empty string
                line = line.rstrip()
                translation = TranslationMap(
                    src = int(line.split(" ")[1]),
                    dst = int(line.split(" ")[0]),
                    span = int(line.split(" ")[2])
                )
                map_list.append(translation)
                line = reader.readline()

    with open('seeds.map', 'r') as reader:
        seeds = []
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            for x in line.split(" "):
                if x!='':
                    seeds.append(int(x)) 
            line = reader.readline()

    locations = []
    for seed in seeds:
        #print(f"-- Seed: {seed} --")
        orig = seed
        trans = -1
        for map_name, map_list in maps.items():
            for m in map_list:
                if m.translate(orig) != -1:
                    trans = m.translate(orig)
                    break
            if trans == -1:
                trans = orig
            #print(f"{map_name} {orig} -> {trans}")
            orig = trans
        locations.append(trans)
    print(locations)
    locations.sort()
    print(locations[0])

if __name__ == "__main__":
    main()
