"""Dessa Shapiro"""
#this code makes a candy land deck, suffles the deck, and 
import random
#makes a deck
def make_deck():
    deck = []

    for color in ["R", "P", "Y", "B", "O", "G"]:
        deck.append((1, color, "S" + color))
        deck.append((2, color, "D" + color))
    #special
    deck.append((9, "X", "CC"))
    deck.append((20, "X", "IC"))
    deck.append((42, "X", "JJ"))
    deck.append((69, "X", "GP"))
    deck.append((92, "X", "LL"))
    deck.append((102, "X", "PS"))
    deck.append((117, "X", "BB"))
    return deck

#This function suffles the deck made in make_deck func
def suffle(deck):
    length = len(deck)
    for index in range(length-1):
          j = random.randint(index, length-1)
          deck[index], deck[j] = deck[j], deck[index]
    return deck
    #for each index i where 0 <= i and i < length-1:
	#	choose a random index j such that i <= j < length:
	#		swap the values at indexes i and j

#this function draws a card from the deck
def draw(deck):
    random.seed(1)
    if len(deck) <= 0:
        return None
    index = random.randint(0, len(deck)-1)
    x = deck.pop(index)
    return x

#Calls other stuff... very cool
def main():
    print(make_deck())
    x = make_deck()
    print(draw(x))
    print(suffle(x))
    
    print(draw(x))

#code runs here
if __name__ == "__main__":
    main()
