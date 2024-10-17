"""Dessa Shapiro"""
import candy_land_card
import random

def test_make_deck_1RSR():
    #setup
    expected = (1, "R", "SR")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_2GGD():
    #setup
    expected = (2, "G", "DG")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_pink():
    #setup
    expected = (1, "P", "SP")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_yellow():
    #setup
    expected = (2, "Y", "DY")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_Blue():
    #setup
    expected = (1, "B", "SB")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_orange():
    #setup
    expected = (1, "O", "SO")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_117xBB():
    #setup
    expected = (117, "X", "BB")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected in actual

def test_make_deck_none_color():
    #setup
    expected = (2, "I", "ID")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected not in actual

def test_make_deck_none_spec():
    #setup
    expected = (30, "X", "CC")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected not in actual

def test_make_deck_none_num():
    #setup
    expected = (3, "P", "DP")
    #invoke
    actual = candy_land_card.make_deck()
    #analyze
    assert expected not in actual

def test_suffle_start():
    #setup
    deck = candy_land_card.make_deck()
    expected = (1, 'R', 'SR')
    #invoke
    random.seed(0)
    suffled = candy_land_card.suffle(deck)
    actual = suffled[0]
    #analyze
    assert actual != expected

def test_suffle_end():
    #setup
    deck = candy_land_card.make_deck()
    expected = (2, 'P', 'DP')
    #invoke
    random.seed(0)
    suffled = candy_land_card.suffle(deck)
    actual = suffled[3]
    #analyze
    assert actual != expected

def test_draw_in():
    deck = candy_land_card.make_deck()
    actual = candy_land_card.draw(deck)
    expected = (1, 'Y', 'SY')
    assert actual == expected

def test_draw_0():
    deck = []
    actual = candy_land_card.draw(deck)
    expected = None
    assert actual == expected

def test_draw_out():
    deck = candy_land_card.make_deck()
    actual = candy_land_card.draw(deck)
    expected = (9, 'X', 'CC')
    assert actual != expected