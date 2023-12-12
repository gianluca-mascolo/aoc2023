#!/usr/bin/env python3
DECK=[ "2","3","4","5","6","7","8","9","T","J","Q","K","A" ]

class Card:
    def __init__(self, value: str):
        assert value in DECK
        self.value = value
    def __lt__(self, other):
        return DECK.index(self.value)<DECK.index(other.value)
    def __le__(self, other):
        return DECK.index(self.value)<=DECK.index(other.value)
    def __eq__(self, other):
        return DECK.index(self.value)==DECK.index(other.value)
    def __ne__(self, other):
        return DECK.index(self.value)!=DECK.index(other.value)
    def __gt__(self, other):
        return DECK.index(self.value)>DECK.index(other.value)
    def __ge__(self, other):
        return DECK.index(self.value)>=DECK.index(other.value)

def main():
    with open('example', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            print(line)
            line = reader.readline()

    c1 = Card("T")
    c2 = Card("2")
    c3 = Card("Q")
    c4 = Card("T")
    print(c1<c2)
    print(c3!=c1)
    print(c1==c4)
if __name__ == "__main__":
    main()
