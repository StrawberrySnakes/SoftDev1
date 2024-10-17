import random_password
#this code tests functions in random_password.py

def test_create_ascii_range_string_abc():
    #setup
    start = 97
    stop = 100
    expected = "abc"
    #invoke
    actual = random_password.create_ascii_range_string(start, stop)
    #analyze
    assert actual == expected

def test_create_uppercase_letters_string():
    #setup
    expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #invoke
    actual = random_password.create_uppercase_letters_sting()
    #analyze
    assert actual == expected

def test_create_lowercase_letters_string():
    #setup
    expected = "abcdefghijklmnopqrstuvwxyz"
    #invoke
    actual = random_password.create_lowercase_letters_sting()
    #analyze
    assert actual == expected

def test_create_digits_string():
    #setup
    expected = "0123456789"
    #invoke
    actual = random_password.create_digits_sting()
    #analyze
    assert actual == expected

def test_create_symbols_string():
    #setup
    expected = '!"' + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    #invoke
    actual = random_password.create_symbols_string()
    #analyze
    assert actual == expected

def test_get_random_char_from_string_abc():
    #setup
    string = "abc"
    expected = "a"
    expected1 = "b"
    expected2 = "c"
    #invoke
    actual = random_password.get_random_char_from_string(string)
    #analyze
    assert actual == expected or actual == expected1 or actual == expected2
