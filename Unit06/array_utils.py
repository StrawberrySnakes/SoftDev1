import arrays
import random

def random_array(size, min_vlaue=0, max_vlaue=None):
    array = arrays.Array(size)
    if max_vlaue is None:
        max_value = size

    for index in range(len(array)):
        array[index] = random.randint(min_vlaue, max_value)
    return array

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array



def main():
    """
    random.seed(1)
    an_array = random_array(10)
    print(an_array)
    """
    array_b = range_array(10, 50, 2)
    print(array_b)

if __name__ == "__main__":
    main()
