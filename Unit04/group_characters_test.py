#This tests group characters program
import group_characters

def test_is_upper_D():
    #setup
    character = "D"
    expected = True

    #invoke
    actual = group_characters.is_upper(character)

    #analyze
    assert actual == expected

def test_is_lower_f():
    #setup
    character = "f"
    expected = True

    #invoke
    actual = group_characters.is_lower(character)

    #analyze
    assert actual == expected

def test_is_digit_5():
    #setup
    character = "5"
    expected = True

    #invoke
    actual = group_characters.is_digit(character)

    #analyze
    assert actual == expected

def test_group_characters():
    #setup
    string = "rt55EDw2k"
    expected = "552rtwkED"

    #invoke
    actual = group_characters.group_characters(string)

    #analyze
    assert actual == expected