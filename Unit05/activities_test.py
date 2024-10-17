import activities

def test_exponent_5():
    #setup
    base = 5
    power = 3
    expected = 125
    #invoke
    actual = activities.exponent(base, power)
    #analyze
    assert actual == expected

def test_exponent_negative():
    #setup
    base = 3
    power = -1

    try:
        #Ivoke
        activities.exponent(base, power)
        assert False, "Negative power"

    except ValueError:
        assert True