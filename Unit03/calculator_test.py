import calculator
import math

#this tests the add function with 5 and 4 
def test_add():
    #setup
    x = 5
    y = 4
    expected = "5 + 4 = 9"

    #invoke
    actual = calculator.add(x, y)

    #analyze 
    assert actual == expected

#This test the subtraction function with 40 - 15
def test_subtract():
    #setup
    x = 40
    y = 15
    expected = "40 - 15 = 25"

    #invoke
    actual = calculator.subtract(x, y)

    #analyze 
    assert actual == expected

#tests multiplication 
def test_multiply():
    #setup
    x = 9
    y = 3
    expected = "9 * 3 = 27"

    #invoke
    actual = calculator.multiply(x, y)

    #analyze 
    assert actual == expected

#tests divide function 15/3
def test_divide():
    #setup
    x = 15
    y = 3
    expected = "15 / 3 = 5.0"

    #invoke
    actual = calculator.divide(x, y)

    #analyze 
    assert actual == expected

#tests divide function 15/3
def test_divide_0():
    #setup
    x = 40
    y = 0
    expected = "40 / 0 = NaN "

    #invoke
    actual = calculator.divide(x, y)

    #analyze 
    assert actual == expected

#tests exponent function
def test_exponent():
    #setup
    x = 4
    y = 3
    expected = "4^3 = 64.0"

    #invoke
    actual = calculator.exponent(x, y)

    #analyze 
    assert actual == expected
