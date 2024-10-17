"""
Dessa Shapiro
Implement your solution to the mini-practicum here.
"""
def decreasing_comparator(a, b):
    return b <= a
def increasing_comparator(a, b):
    """
    A comparator function that returns True if a is less than or equal to b, 
    and False otherwise.
    """
    return a <= b

def is_sorted(a_list, comparator=increasing_comparator, index=0):
    if index+1 == len(a_list)-1:
        return comparator(a_list[index], a_list[index+1])
    else:
        result = comparator(a_list[index], a_list[index+1])
        if result == False:
            return result
        else:
            return is_sorted(a_list, comparator, index+1)

def main():
    list1 = [20, 10, 30]
    list2 = [30, 20, 10]
    a = is_sorted(list1)
    b = is_sorted(list2)
    c= is_sorted(list1, decreasing_comparator)
    d= is_sorted(list2, decreasing_comparator)
    print(a)
    print(b)
    print(c)
    print(d)

if __name__ == "__main__":
    main()


