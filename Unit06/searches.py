"""Dessa Shapiro"""
#this code searches through arrays in 3 different ways, linear, binarny, and jump
import arrays
import array_utils
import random
import math

#implements linear seach on an array
def linear_search(an_array, target, start=None, end=None):
    if start == None or start < 0:
        start = 0
    if end == None or end > int(len(an_array)):
        end = len(an_array)
    for index in range(start, end):
        if an_array[index] == target:
            return index
        else:
            pass
    return None

#implements binary seach on an array
def binary_search(an_array, target, start=None, end=None):
    if start is None and end is None:
        start = 0
        end = len(an_array)-1
    if start > end:
        return None
    
    midpoint = (start+end) // 2
    value = an_array[midpoint]
    if target == value:
        return midpoint
    elif value < target:
        start = midpoint + 1
        return binary_search(an_array, target, start, end)
    else:
        end = midpoint - 1
        return binary_search(an_array, target, start, end)

#implements jump seach on an array
def jump_search(an_array, target):
    length = int(len(an_array))
    block_size = int(math.sqrt(length))
    for index in range(0, length, block_size):
        if an_array[index] == target:
            return index
        elif an_array[index] > target:
            for i in range(index - block_size, index):
                if i < 0:
                    continue
                if an_array[i] == target:
                    return i
            return None
            
    for index in range((length // block_size) * block_size, length):
        if an_array[index] == target:
            return index

#calls searches
def main():
    array_a = array_utils.range_array(0, 52, 2)
    print(jump_search(array_a, 50))
    print(array_a)
    print(binary_search(array_a, 0))
    print(binary_search(array_a, 50))
    print(linear_search(array_a, 1))
    print(linear_search(array_a, 50, 45, 51))
    print(linear_search(array_a, 100))
    print(linear_search(array_a, 101))

#code runs here
if __name__ == "__main__":
    main()
