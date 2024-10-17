"""Dessa Shapiro"""
#tests functions from idiots_delight
import idiots_delight
import random

def test_deal_hand():
    #setup
    random.seed(1)
    deck, hand = idiots_delight.deal_hand()
    expected = 4
    #invoke
    actual = len(hand)
    assert actual == expected

def test_discard_4():
    #setup
    deck, hand = idiots_delight.deal_hand()
    num_of_cards = 4
    expected = []
    #invoke
    actual = idiots_delight.discard(hand, num_of_cards)
    #analyze
    assert actual == expected

def test_discard_2():
    #setup
    random.seed(1)
    deck, hand = idiots_delight.deal_hand()
    num_of_cards = 2
    expected = [(8, 'Diamonds', '8 of Diamonds', ' 8D'), (3, 'Spades', '3 of Spades', ' 3S')]
    #invoke
    actual = idiots_delight.discard(hand, num_of_cards)
    #analyze
    assert actual== expected

def test_discard_0():
    #setup
    random.seed(1)
    deck, hand = idiots_delight.deal_hand()
    num_of_cards = 0
    expected = [(8, 'Diamonds', '8 of Diamonds', ' 8D'), (4, 'Spades', '4 of Spades', ' 4S'), (11, 'Hearts', 'Jack of Hearts', ' JH'), (3, 'Spades', '3 of Spades', ' 3S')]
    #invoke
    actual = idiots_delight.discard(hand, num_of_cards)
    #analyze
    assert actual== expected

def test_play_round_hand_size():
    # Setup
    random.seed(1)
    deck, hand = idiots_delight.deal_hand()
    expected = 5

    # Invoke
    new_deck, new_hand = idiots_delight.play_round(deck, hand)
    actual = len(new_hand)

    # Analyze
    assert actual == expected

def test_play_round_discard_4_cards():
    deck = []
    hand = [('6', 'Hearts'), ('4', 'Dimonds'), ('5', 'Hearts'), ('6', 'Hearts')]
    expected_hand_size = 0

    # Invoke the play_round function
    new_deck, new_hand = idiots_delight.play_round(deck, hand)

    # Analyze: Check if the deck is empty and the hand is empty after discarding 4 cards
    assert len(new_hand) == expected_hand_size

def test_play_round_discard_2_cards():
    deck = []
    hand = [('6', 'Spades'), ('12', 'Dimonds'), ('2', 'Dimonds'), ('10', 'Hearts')]
    expected_hand_size = 2

    # Invoke the play_round function
    new_deck, new_hand = idiots_delight.play_round(deck, hand)

    # Analyze: Check if the deck is empty and the hand is empty after discarding 4 cards
    assert len(new_hand) == expected_hand_size


    

