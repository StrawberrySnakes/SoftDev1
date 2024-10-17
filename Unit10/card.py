class Card:
    __slots__ = ["rank", "suit", "name", "shorthand"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = str(rank) + " of " + suit
        self.shorthand = str(rank) + suit[0]


def print_card(card):
    print(card.rank, card.suit, card.name, card.shorthand)

def main():
    card1 = Card(2, "Hearts")
    # card1.rank= 2
    # card1.suit = "Hearts"
    # card1.name = "2 or Hearts"
    # card1.shorthand = "2H"
    print_card(card1)

if __name__ == "__main__":
    main()



"""

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name = str(self.rank)+"of"+self.suit
        self.shorthand = str(self.rank) + self.suit[0]

def main():
    card1 = Card(2, "Hearts")
    card2=Card(10, "Clubs")
    print(card1.rank, card1.suit)
    print(card2.rank, card2.suit)

main()

"""