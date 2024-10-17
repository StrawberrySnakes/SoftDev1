#like the code is in the actual file
from guessing_game import *
import random

def test_secret_number():
    #setup
    random.seed(1)
    expected = 18

    #ivoke
    actual = secret_number()

    #analyze
    assert expected == actual

def test_check_guess_too_high():
    #setup
    random.seed(1)
    secret = 57
    guess = 72
    expected = "Too High"

    #ivoke
    actual = check_guess(secret, guess)

    #analyze
    assert expected == actual

def test_check_guess_too_low():
    #setup
    random.seed(1)
    secret = 12
    guess = 8
    expected = "Too Low"

    #ivoke
    actual = check_guess(secret, guess)

    #analyze
    assert expected == actual

def test_check_guess_correct():
    #setup
    random.seed(1)
    secret = 60
    guess = 60
    expected = "Correct"

    #ivoke
    actual = check_guess(secret, guess)

    #analyze
    assert expected == actual