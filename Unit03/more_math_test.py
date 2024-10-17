#this code tests the math functions in the more_math.py file 
import math
import more_math

#test the factorial function for a value of 4
def test_fact_4():
    #setup
    x = 4
    expected = 24

    #invoke 
    actual = more_math.fact(x)

    #analyze
    assert actual == expected

#test the square root function for the value of 4
def test_root_4():
    #setup
    x = 4
    expected = 2

    #invoke 
    actual = more_math.root(x)

    #analyze
    assert actual == expected

#test the square root function with a float value of 6.2 
def test_root_6():
    #setup
    x = 6.2
    expected = 2.4899799196

    #invoke 
    actual = more_math.root(x)

    #analyze
    #makes it more likely to be equal bc there may be very small differences 
    assert math.isclose(actual, expected)

#this function tests the trunk function with a value of 6.3
def test_trunk_6():
    #setup
    x = 6.3
    expected = 6

    #invoke 
    actual = more_math.trunk(x)

    #analyze
    assert actual == expected
