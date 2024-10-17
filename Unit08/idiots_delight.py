"""Dessa Shapiro"""
#creates the iditos_delight game
import cards
import random

#deals a hand of 4 cards
def deal_hand():
    deck = cards.make_deck()
    cards.shuffle(deck)
    hand = cards.deal_one_hand(deck, 4)
    return deck, hand

#discards a certain number of cards from the last 4 cards in a hand
def discard(hand, num_of_cards):
    new_hand = []
    if num_of_cards == 4:
        return hand[:-4]
    elif num_of_cards == 2:
        new = hand[:-3]
        new.append(hand[-1])
        return new
    else: 
        return hand
    
#uses both make hand and discard to play a round of the game. Checks values and suits to determine what to do
def play_round(deck, hand):
    while len(hand) < 4:
        cards.draw(deck, hand)
    print(hand)
    first = hand[-4]
    second = hand[-3]
    third = hand[-2]
    fourth = hand[-1]
    if first[0] == fourth[0]:
        hand = discard(hand, 4)
    else:
        if second[1] == third[1]:
            hand = discard(hand, 2)
    if len(deck) > 0:
        cards.draw(deck, hand)
        print(hand)

    return deck, hand

#checks how many cards are left when deck is gone
def main():
    #random.seed(27)
    deck, hand = deal_hand()
    while len(deck) > 0:
        deck, hand = play_round(deck, hand)
    else:
        if len(hand) == 0:
            print("Game Over. You won! with 0 cards in your hand")
        else:
            print("Game Over. There are",len(hand),"cards left in your hand, try again next time :)")

#function runs here
if __name__ == "__main__":
    main()
