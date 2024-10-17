import activities
import random

def test_squared_8():
    #setup
    x = 8
    expected = 64

    #invoke 
    actual = activities.squared(x)

    #analyze 
    assert actual == expected
    
def test_squared_9():
    #setup
    x = -9
    expected = 81

    #invoke 
    actual = activities.squared(x)

    #analyze 
    assert actual == expected

def test_cubed_3():
    #setup
    x = 3
    expected = 27

    #invoke 
    actual = activities.cubed(x)

    #analyze 
    assert actual == expected

def test_cubed_2():
    #setup
    x = -2
    expected = -8

    #invoke 
    actual = activities.cubed(x)

    #analyze 
    assert actual == expected

def test_even_or_odd_12():
    #setup
    x = 12
    expected = "Even"

    #invoke 
    actual = activities.even_or_odd(x)

    #analyze 
    assert actual == expected

def test_even_or_odd_163():
    #setup
    x = 163
    expected = "Odd"

    #invoke 
    actual = activities.even_or_odd(x)

    #analyze 
    assert actual == expected

def test_coin_toss_heads():
    random.seed(1)
    #setup
    expected = "Heads"
    #invoke
    actual = activities.coin_toss()
    #analyze
    assert actual == expected

def test_coin_toss_tails():
    random.seed(5)
    #setup
    expected = "Tails"
    #invoke
    actual = activities.coin_toss()
    #analyze
    assert actual == expected



