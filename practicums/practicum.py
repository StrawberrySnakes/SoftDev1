"""
Implement your solution to the practicum here.

Dessa Shapiro
"""

def find_smallest(a_list):
    smallest_value = None
    smallest_index = None
    if len(a_list) == 0:
        return None
    for index in range(len(a_list)):
        value = a_list[index]
        if smallest_value == None or value < smallest_value:
            smallest_value = value
            smallest_index = index
        else:
            pass
    tup_1 = (smallest_value, smallest_index)
    return tup_1

def combine_lists(a, b):
    c = []
    set_c = set()
    for value in a:
        set_c.add(value)
        c.append(value)
    for value in b:
        if value in set_c:
            continue
        c.append(value)
    return c
    
#fish sort runs in N^2 time since the find_smallest is an N time complexity and as the origional list gains a value you have to 
# do N more itterations
def fish_sort(a_list):
    copy = [x for x in a_list]
    sorted_lst = []
    while len(sorted_lst) < len(a_list):
        value, index = find_smallest(copy)[0], find_smallest(copy)[1]
        sorted_lst.append(value)
        copy.pop(index)
    return sorted_lst

def are_anagrams(word1, word2):
    same = {}
    same2 = {}
    for character in word1:
        if character == " ":
            pass
        if character not in same:
            same[character] = 1
        else:
            same[character] += 1

    for character in word2:
        if character == " ":
            pass
        # elif character not in same:
        #     return False
        else:
            if character not in same2:
                same2[character] = 1
            else:
                same2[character] += 1
    if same == same2:
        return True
    else:
        return False

def main():
    a = [1, 2, 1, 4, 3, 2, 1, 5, 5]
    print(are_anagrams("dormitory", "dirty room"))
    # a = [a for a in range(10)]
    # b= [b for b in range(10)]
    # print(combine_lists(a, b))
    # lst = [8, 4, 2, 6, 9, 3, 1, 2, 8, 9, 1]
    # print(find_smallest(lst))

if __name__ == "__main__":
    main()
