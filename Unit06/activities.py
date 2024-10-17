import arrays
import random
import time
import searches
import array_utils

def making_arrays():
    array_1 = arrays.Array(5)
    print(array_1)
    array_2 = arrays.Array(1, 0)
    print(array_2)
    array_3 = arrays.Array(10, "")
    print(array_3)
    array_4 = arrays.Array(20, False)
    print(array_4)

def while_fill(an_array):
    length = len(an_array)
    counter = 0
    while counter < length:
        an_array[counter] = counter
        counter += 1
    return an_array

def for_fill(an_array):
    for index in range(len(an_array)):
        an_array[index] = index
    return an_array

def roll_the_dice(sides):
    return random.randint(1, sides)

def linear_search_timer(an_array, target):
    begin = time.perf_counter()
    searches.linear_search(an_array, target)
    end = time.perf_counter()
    return end - begin

def linear_timer():
    array_a = array_utils.range_array(1, 10000001)
    print(linear_search_timer(array_a, 1))
    print(linear_search_timer(array_a, 2500000))
    print(linear_search_timer(array_a, 7500000))
    print(linear_search_timer(array_a, 10000000))

def print_odds(an_array):
    for index in range(len(an_array)):
        if an_array[index]%2 != 0:
            print(an_array[index], end=" ")
        else:
            pass
            
def print_oods_rec(an_array, index =0):
    if index >= len(an_array):
        print()
    else:
        value = an_array[index]
        if value%2 != 0:
            print(value, end=" ")
        print_oods_rec(an_array, index+1)

def countdown(n):
    if n<0:
        return None
    elif n==0:
        print(0)
        return 0
    else:
        print(n)
        return n + countdown(n-1)

def factorial(n):
    if n<0:
        return None
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def count_up(n):
    if n < 0:
        return None
    elif n == 0:
        print(0)
        return 0
    else:
        print(n)
        sum = count_up(n-1)
        return sum + n
    
def binary_search_timer(an_array, target):
    begin = time.perf_counter()
    searches.binary_search(an_array, target)
    end = time.perf_counter()
    return end - begin

def binary_timer():
    array_a = array_utils.range_array(1, 10000001)
    print(binary_search_timer(array_a, 1))
    print(binary_search_timer(array_a, 2500000))
    print(binary_search_timer(array_a, 7500000))
    print(binary_search_timer(array_a, 10000000))


def main():
    linear_timer()
    binary_timer()
    """
    making_arrays()
    x = arrays.Array(10)
    print(for_fill(x))
    
    random.seed(1)
    for i in range(10):
        print(roll_the_dice(6))
    
    array_a =array_utils.range_array(0, 5)
    print_oods_rec(array_a)

    print("Sum:" ,countdown(2000))
    print(factorial(20))
    print(factorial(100))
    print(factorial(2000))
    count_up(20)
    """
    


if __name__ == "__main__":
    main()
    
"""
0   0   0  2  3
16  7   2  2  2
8   3   1  2
39  12  9  10

log2(n)= m(maximum numeber of iterations it takes to find n)
"""