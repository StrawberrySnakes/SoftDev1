from practicum import *

def test_find_smallest_empty():
    # setup
    a_list = []
    expected = None

    # invoke
    actual = find_smallest(a_list)

    # analyze
    assert expected == actual

def test_find_smallest_one():
    # setup
    a_list = [5]
    expected = (5, 0)

    # invoke
    actual = find_smallest(a_list)

    # analyze
    assert expected == actual

def test_find_smallest_many():
    # setup
    a_list = [3, 2, 1, 4, 5]
    expected = (1, 2)

    # invoke
    actual = find_smallest(a_list)

    # analyze
    assert expected == actual

def test_find_smallest_duplicates():
    # setup
    a_list = [3, 1, 2, 1, 4, 1, 5]
    expected = (1, 1)

    # invoke
    actual = find_smallest(a_list)

    # analyze
    assert expected == actual

def test_combine_lists_both_empty():
    # setup
    a = []
    b = []
    expected = []

    # invoke
    actual = combine_lists(a, b)

    # analyze
    assert actual is not a
    assert actual is not b
    assert expected == actual

def test_combine_lists_b_empty():
    # setup
    a = [1, 2]
    b = []
    expected = [1, 2]

    # invoke
    actual = combine_lists(a, b)

    # analyze
    assert actual is not a
    assert actual is not b
    assert expected == actual

def test_combine_lists_a_empty():
    # setup
    a = []
    b = [5, 3]
    expected = [5, 3]

    # invoke
    actual = combine_lists(a, b)

    # analyze
    assert actual is not a
    assert actual is not b
    assert expected == actual

def test_combine_lists_duplicates():
    # setup
    a = [1, 2]
    b = [2, 1]
    expected = [1, 2]

    # invoke
    actual = combine_lists(a, b)

    # analyze
    assert actual is not a
    assert actual is not b
    assert expected == actual

def test_combine_lists_all():
    # setup
    a = [1, 2, 3]
    b = [4, 3, 2, 5]
    expected = [1, 2, 3, 4, 5]

    # invoke
    actual = combine_lists(a, b)

    # analyze
    assert actual is not a
    assert actual is not b
    assert expected == actual

def test_fish_sort_empty():
    # Setup
    pond = []
    expected = []

    # Invoke
    barrel = fish_sort (pond)

    # Analysis
    assert barrel == expected

def test_fish_sort_one():
    # setup
    pond = [1]
    expected = [1]

    # invoke
    actual = fish_sort(pond)

    # analyze
    assert pond is not actual
    assert expected == actual

def test_fish_sort_several():
    # setup
    pond = [3, 2, 1, 5, 4]
    expected = [1, 2, 3, 4, 5]

    # invoke
    actual = fish_sort(pond)

    # analyze
    assert pond is not actual
    assert expected == actual

def test_fish_sort_duplicates():
    # setup
    pond = [1, 2, 3, 3, 2, 1]
    expected = [1, 1, 2, 2, 3, 3]

    # invoke
    actual = fish_sort(pond)

    # analyze
    assert pond is not actual
    assert expected == actual

def test_are_anagrams_one_true():
    # setup
    word1 = str("a")
    word2 = str("a")

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert anagram

def test_are_anagrams_one_false():
    # setup
    word1 = str("a")
    word2 = str("b")

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert not anagram

def test_are_anagrams_many_true():
    # setup
    word1 = "silent"
    word2 = "listen"

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert anagram

def test_are_anagrams_many_false():
    # setup
    word1 = "catt"
    word2 = "caat"

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert not anagram

def test_are_anagrams_spaces_true():
    # setup
    word1 = "dormitory"
    word2 = "dirty room"

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert anagram

def test_are_anagrams_spaces_false():
    # setup
    word1 = "dormitory"
    word2 = "dirty rom"

    # invoke
    anagram = are_anagrams(word1, word2)

    # analyze
    assert not anagram
