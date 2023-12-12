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
    def integer(self) -> int:
        return DECK.index(self.value)

class Hand:
    def __init__(self, cards: list[Card], bid: int):
        assert len(cards)==5
        self.cards = [c for c in cards]
        self.bid = bid

    def strength(self) -> int:
        s = 0
        deck_base = len(DECK)
        for p,c in enumerate(self.cards):
            s+=c.integer()*(deck_base**(4-p))
        s+=self.__kind()*(deck_base**5)
        return s
        
    def __kind(self) -> int:
        card_groups = {}
        for card in self.cards:
            if card.value in card_groups:
                card_groups[card.value]+=1
            else:
                card_groups[card.value]=1
        if len(card_groups)==1:
            # Five of a kind
            return 7
        elif len(card_groups)==2:
            if max(card_groups.values())==4:
                # Four of a kind
                return 6
            else:
                # Full House
                return 5
        elif len(card_groups)==3:
            if max(card_groups.values())==3:
                # Three of a kind
                return 4
            else:
                # Two pairs
                return 3
        elif len(card_groups)==4:
            # One Pair
            return 2
        else:
            # High Card
            return 1

    def __lt__(self, other):
        return self.strength()<other.strength()
    def __le__(self, other):
        return self.strength()<=other.strength()
    def __eq__(self, other):
        return self.strength()==other.strength()
    def __ne__(self, other):
        return self.strength()!=other.strength()
    def __gt__(self, other):
        return self.strength()>other.strength()
    def __ge__(self, other):
        return self.strength()>=other.strength()
    def __str__(self):
        return "".join([c.value for c in self.cards])
def main():
    with open('input', 'r') as reader:
        line = reader.readline()
        hands = []
        while line != '':  # The EOF char is an empty string
            line = line.rstrip()
            hands.append(
                Hand(
                    cards = [Card(c) for c in line.split(" ")[0]],
                    bid = int(line.split(" ")[1])
                )
            )
            line = reader.readline()
    hands.sort()
    handsum=0
    for i,hand in enumerate(hands):
        handsum+=(i+1)*hand.bid
    print(handsum)

if __name__ == "__main__":
    main()
