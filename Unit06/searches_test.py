"""Dessa Shapiro"""
#Test searches.py
import searches
import array_utils

#test first target
def test_linear_search_1():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 0
    expected = 0
    #invoke
    actual = searches.linear_search(an_array, target)
    #analyze
    assert actual==expected 

#test last target
def test_linear_search_50():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 50
    expected = len(an_array)-1
    #invoke
    actual = searches.linear_search(an_array, target)
    #analyze
    assert actual==expected 

#test a middle target
def test_linear_search_34():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 34
    expected = 17
    #invoke
    actual = searches.linear_search(an_array, target)
    #analyze
    assert actual==expected 

#test a non-existant target
def test_linear_search_21():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 21
    expected = None
    #invoke
    actual = searches.linear_search(an_array, target)
    #analyze
    assert actual==expected 

#test start end that don't exist
def test_linear_search_start_end_outside_ranges():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 20
    start = -12
    end = 30
    expected = 10
    #invoke
    actual = searches.linear_search(an_array, target, start, end)
    #analyze
    assert actual==expected 

#test start end range end case
def test_linear_search_start_end_ranges():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 22
    start = 0
    end = 11
    expected = None
    #invoke
    actual = searches.linear_search(an_array, target, start, end)
    #analyze
    assert actual==expected 

def test_jump_search_end():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 22
    expected = None
    #invoke
    actual = searches.jump_search(an_array, target)
    #analyze
    assert actual==expected 

def test_jump_search_end():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 50
    expected = 25
    #invoke
    actual = searches.jump_search(an_array, target)
    #analyze
    assert actual==expected 

def test_jump_search_start():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 0
    expected = 0
    #invoke
    actual = searches.jump_search(an_array, target)
    #analyze
    assert actual==expected 

def test_jump_search_mid():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 20
    expected = 10
    #invoke
    actual = searches.jump_search(an_array, target)
    #analyze
    assert actual==expected 

def test_jump_search_outside():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 400
    expected = None
    #invoke
    actual = searches.jump_search(an_array, target)
    #analyze
    assert actual==expected 

def test_binary_search_start():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 0
    expected = 0
    #invoke
    actual = searches.binary_search(an_array, target)
    #analyze
    assert actual==expected 

def test_binary_search_end():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 50
    expected = 25
    #invoke
    actual = searches.binary_search(an_array, target)
    #analyze
    assert actual==expected 

def test_binary_search_mid():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 20
    expected = 10
    #invoke
    actual = searches.binary_search(an_array, target)
    #analyze
    assert actual==expected 

def test_binary_search_outside():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 21
    expected = None
    #invoke
    actual = searches.binary_search(an_array, target)
    #analyze
    assert actual==expected 

def test_binary_search_range_outside():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 22
    start = 0
    end = 10
    expected = None
    #invoke
    actual = searches.binary_search(an_array, target, start, end)
    #analyze
    assert actual==expected 

def test_binary_search_range_inside():
    #setup
    an_array = array_utils.range_array(0, 52, 2)
    target = 12
    start = 0
    end = 10
    expected = 6
    #invoke
    actual = searches.binary_search(an_array, target, start, end)
    #analyze
    assert actual==expected 
    

