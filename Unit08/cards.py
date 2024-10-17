"""Dessa Shapiro"""
#this function makes a list the contains all the cards in a 52 playing card deck and used that to suffle and draw hands.
import random
import re

#Creates a card as a tuple with 4 values
def make_card(rank, suit):
    try:
        if (rank > 2 and rank < 14) or re.findall('Hearts|Diamonds|Clubs|Spades', suit):
            if rank == 11:
                rank_word = "Jack"
                letter = " J" + suit[0]
            elif rank == 12:
                rank_word = "Queen"
                letter = " Q" + suit[0]
            elif rank == 13:
                rank_word = "King"
                letter = " K" + suit[0]
            elif rank == 14:
                rank_word = "Ace"
                letter = " A" + suit[0]
            else:
                rank_word = str(rank)
                if rank == 10:
                    letter = rank_word + suit[0]
                else:
                    letter = " " + rank_word + suit[0]
            # if suit == "Hearts" or suit == "Diamonds":
            #     letter = "\033[31m " + letter + "\033[37m"
            # else:
            #     letter = "\033[34m " + letter + "\033[37m"
            combined = rank_word + " of " + suit
            card_tup = (rank, suit, combined, letter)
            return card_tup
    except:
        print("Invalid Parameters")

#Creates a full deck of cards in suit and number order
def make_deck():
    deck = []
    for name in ["Hearts", "Clubs", "Diamonds", "Spades"]:
        for i in range(2, 11):
            deck.append(make_card(i, name))
        for i in range (11, 15):
            deck.append(make_card(i, name))
    

    #     deck.append(make_card(i, "Clubs"))
    #     deck.append(make_card(i, "Diamonds"))
    #     deck.append(make_card(i, "Spades"))

    # for i in range (11, 15):
    #     deck.append(make_card(i, "Hearts"))
    #     deck.append(make_card(i, "Clubs"))
    #     deck.append(make_card(i, "Diamonds"))
    #     deck.append(make_card(i, "Spades"))
    
    return deck

#shuffles the deck of cards
def shuffle(deck):
    length = len(deck)
    for index in range(length-1):
          j = random.randint(index, length-1)
          deck[index], deck[j] = deck[j], deck[index]
    return deck

#draws a card from your hand
def draw(deck, hand):
    if len(deck) <= 0:
        return None
    card = deck.pop()
    hand.append(card)
    return card

#gives the player a list of cards given the deck and the number of cards they want
def deal_one_hand(deck, card_num):
    hand = []
    for _ in range(card_num):
        draw(deck, hand)
    return hand

# calls all the functions
def main():
    # card = make_card(10, "Diamonds")
    # card2 = make_card(10, "Dimons")
    # card3 = make_card(17, "Diamonds")
    # print(card, card3, card2)
    random.seed(1)
    deck = make_deck()
    deal = deal_one_hand(deck, 5)
    print(deal)
    suffled = shuffle(deck)
    #print(suffled)

#code runs here
if __name__ == "__main__":
    main()
