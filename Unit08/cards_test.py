"""Dessa Shapiro"""
#test the functions in the card modual
import cards
import random

def test_make_card_10H():
    #setup
    rank = 10
    suit = "Hearts"
    expected = (10, "Hearts", "10 of Hearts", "10H")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_card_5D():
    #setup
    rank = 5
    suit = "Diamonds"
    expected = (5, "Diamonds", "5 of Diamonds", " 5D")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_card_JS():
    #setup
    rank = 11
    suit = "Spades"
    expected = (11, "Spades", "Jack of Spades", " JS")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_card_QC():
    #setup
    rank = 12
    suit = "Clubs"
    expected = (12, "Clubs", "Queen of Clubs", " QC")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_card_QC():
    #setup
    rank = 13
    suit = "Diamonds"
    expected = (13, "Diamonds", "King of Diamonds", " KD")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_card_AH():
    #setup
    rank = 14
    suit = "Hearts"
    expected = (14, "Hearts", "Ace of Hearts", " AH")
    #invoke
    actual = cards.make_card(rank, suit)
    #analyze
    assert actual == expected

def test_make_deck_last():
    #setup
    expected = (14, 'Spades', 'Ace of Spades', ' AS')
    #invoke
    deck = cards.make_deck()
    actual = deck[-1]
    #analyze
    assert actual == expected

def test_make_deck_first():
    #setup
    expected = (2, 'Hearts', '2 of Hearts', ' 2H')
    #invoke
    deck = cards.make_deck()
    actual = deck[0]
    #analyze
    assert actual == expected

def test_make_deck_mid_clu():
    #setup
    expected = (2, 'Clubs', '2 of Clubs', ' 2C')
    #invoke
    deck = cards.make_deck()
    actual = deck[13]
    #analyze
    assert actual == expected

def test_make_deck_mid_di():
    #setup
    expected = (3, 'Diamonds', '3 of Diamonds', ' 3D')
    #invoke
    deck = cards.make_deck()
    actual = deck[27]
    #analyze
    assert actual == expected

def test_suffle_start():
    #setup
    deck = cards.make_deck()
    expected = (2, 'Hearts', '2 of Hearts', ' 2H')
    #invoke
    random.seed(0)
    suffled = cards.suffle(deck)
    actual = suffled[0]
    #analyze
    assert actual != expected

def test_shuffle_mid():
    #setup
    deck = cards.make_deck()
    expected = (3, 'Diamonds', '3 of Diamonds', ' 3D')
    #invoke
    random.seed(0)
    suffled = cards.shuffle(deck)
    actual = suffled[27]
    #analyze
    assert actual != expected

def test_shuffle_end():
    #setup
    deck = cards.make_deck()
    expected = (14, 'Spades', 'Ace of Spades', ' AS')
    #invoke
    random.seed(0)
    suffled = cards.shuffle(deck)
    actual = suffled[3]
    #analyze
    assert actual != expected

def test_deal_one_hand():
    #setup
    deck = cards.make_deck()
    card_num = 5
    expected = (14, 'Spades', 'Ace of Spades', ' AS')
    #invoke
    random.seed(1)
    suffled = cards.deal_one_hand(deck, card_num)
    actual = suffled[3]
    #analyze
    assert actual != expected



