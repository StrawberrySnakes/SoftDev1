"""Dessa Shapiro"""
import arrays
import array_utils

def max(an_array, index=0, max_val=None):
    if len(an_array) == 0:
        return None 
    if index == len(an_array):
        return max_val
    if max_val is None or an_array[index] > max_val:
        max_val = an_array[index]
    
    return max(an_array, index + 1, max_val)


def power(base, exponent):
    if exponent < 0:
        raise ValueError
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base
    elif exponent % 2 == 0:
        return power(base, exponent//2) * power(base, exponent//2)
    else:
        return base * power(base, exponent//2) * power(base, exponent//2) 
    
    
def main():
    an_array = array_utils.range_array(1, 10)
    largest = max(an_array)
    print(largest)
    result = power(4, 7)
    print(result)

if __name__ == "__main__":
    main()
