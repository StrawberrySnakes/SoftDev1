import practice
# this code test the mathmatical function in the practice.py file

#tets the absolute difference between 5 and 8
def test_absolute_difference_3():
    #setup
    a = 5
    b = 8
    expected = 3

    #invoke
    actual = practice.absolute_difference(5, 8)

    #analyze
    assert actual == expected

#tets the absolute difference between 10 and 2
def test_absolute_difference_8():
    #setup
    a = 10
    b = 2
    expected = 8

    #invoke
    actual = practice.absolute_difference(10, 2)

    #analyze
    assert actual == expected

#tets the absolute difference between 0 and 0
def test_absolute_difference_0():
    #setup
    a = 0
    b = 0
    expected = 0

    #invoke
    actual = practice.absolute_difference(0, 0)

    #analyze
    assert actual == expected