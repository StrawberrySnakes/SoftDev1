import array_utils
def threes_and_fives(n):
    """
    if n == 0:
        return 0
    elif n % 3 == 0:
        return n+threes_and_fives(n-1)
    elif n % 5 == 0:
        return n+threes_and_fives(n-1)
    else:
        return threes_and_fives(n-1)
    """
    sum = 0 
    for i in range(n):
        if i%3==0 or i%5==0:
            sum += n
        return sum
    
def main():
    an_array = array_utils.range_array(0, 50, 2)
    print(an_array)
    print(threes_and_fives(1000))

if __name__ =="__main__":
    main()