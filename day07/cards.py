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

class Hand:
    def __init__(self, cards: list[Card]):
        assert len(cards)==5
        self.cards = [c for c in cards]
    def kind(self):
        card_groups = {}
        for card in self.cards:
            if card.value in card_groups:
                card_groups[card.value]+=1
            else:
                card_groups[card.value]=1
        if len(card_groups)==1:
            print("Five of a kind")
        elif len(card_groups)==2:
            if max(card_groups.values())==4:
                print("Four of a kind")
            else:
                print("Full House")
        elif len(card_groups)==3:
            if max(card_groups.values())==3:
                print("Three of a kind")
            else:
                print("Two pairs")
        elif len(card_groups)==4:
            print("One Pair")
        elif len(card_groups)==5:
            print("High Card")

        return card_groups

def main():
    with open('example', 'r') as reader:
        line = reader.readline()
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            print(line)
            line = reader.readline()

    c1 = Card("A")
    c2 = Card("Q")
    c3 = Card("8")
    c4 = Card("9")
    c5 = Card("T")
    print(c1<c2)
    print(c3!=c1)
    print(c1==c4)
    hand = Hand([c1,c2,c3,c4,c5])
    print([ c.value for c in hand.cards])
    hand.cards.sort()
    print([ c.value for c in hand.cards])
    print(hand.kind())
    print(max(hand.kind().values()))
if __name__ == "__main__":
    main()
