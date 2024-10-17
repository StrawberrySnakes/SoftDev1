"""Dessa Shapiro"""

import mixed_fractions

TUPLES = [(3, 1, 2), (3, -1, 1), (2, 0, 1)]
FRACTIONS = [mixed_fractions.Fraction(w, n, d) for w, n, d in TUPLES]

def test_get_fraction():
    fraction1 = mixed_fractions.Fraction(15)
    assert fraction1.get_fraction() == (15, 0, 1)

    fraction2 = mixed_fractions.Fraction(5, -3, -4)
    assert fraction2.get_fraction() == (5, -3, -4)

def test_simplify():
    fraction1 = mixed_fractions.Fraction(5, 4, 3)
    result1 = fraction1.simplify().get_fraction()
    assert result1 == (6, 1, 3)

    fraction2 = mixed_fractions.Fraction(0, 15, -3)
    result2 = fraction2.simplify().get_fraction()
    assert result2 == (-5, 0, 1)

    fraction3 = mixed_fractions.Fraction(-7, -6, -4)
    result3 = fraction3.simplify().get_fraction()
    assert result3 == (-6, 1, 2)

def test_add():
    fraction1 = mixed_fractions.Fraction(3, 1, 2)
    fraction2 = mixed_fractions.Fraction(2, 3, 4)
    result1 = mixed_fractions.Fraction.add(fraction1.get_fraction(), fraction2.get_fraction())
    assert result1 == (13, 5, 4)  # Without simplification

    # Test case 2
    fraction3 = mixed_fractions.Fraction(0, 15, -3)
    fraction4 = mixed_fractions.Fraction(1, 2, 3)
    result2 = mixed_fractions.Fraction.add(fraction3.get_fraction(), fraction4.get_fraction())
    assert result2 == (8, 5, 3)  # Without simplification


''''
def test_unique_sorted_list():
    actual = mixed_fractions.unique_sorted_list(FRACTIONS)  
    assert [FRACTIONS[1], FRACTIONS[0]] == actual
'''

'''    
def test_partition():
    actual = mixed_fractions.partition(FRACTIONS)
    assert 2 == len(actual)
    assert FRACTIONS[0] in actual
    assert FRACTIONS[1] in actual
    assert FRACTIONS[2] in actual
    assert [FRACTIONS[0]] == actual[FRACTIONS[0]]
    assert [FRACTIONS[1], FRACTIONS[2]] == actual[FRACTIONS[1]]
'''

'''
def test_find_all():
    a_partition = mixed_fractions.partition(FRACTIONS) 
     
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[0])                                 
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(2,3,2))  
    assert [FRACTIONS[0]] == actual
    
    actual = mixed_fractions.find_all(a_partition, FRACTIONS[2])                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual
    
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(3,-2,2))                                 
    assert [FRACTIONS[1], FRACTIONS[2]] == actual
'''  
 
'''
def test_find_all_Empty():
    a_partition = mixed_fractions.partition(FRACTIONS)
    actual = mixed_fractions.find_all(a_partition, mixed_fractions.Fraction(1,2,3))                                 
    assert [] == actual
'''