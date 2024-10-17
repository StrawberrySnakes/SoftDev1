def count_down(number):
    sum = number
    while number>0:
        print(number)
        number -= 1
        sum += number
    return sum

def count_up(number):
    count = 0
    sum = count
    while count <= number:
        print(count)
        sum += count
        count += 1
    return sum

def example_loop():
    sum = 0
    while True:
        x = input(">> ")
        x = int(x)
        if x == 0:
            break
        elif x%2 == 0:
            continue
        else:
            sum+x
    print("Done")

def print_range(a_range):
    index=0
    length = len(a_range)
    while index < length:
        value = a_range[index]
        print(value, end=" ")
        index+=1
    print()

def print_range_for(a_range):
    for value in a_range:
        print(value, end=" ")
    print()

def reverse_chars(a_string):
    #use for loop to create a copy of the string in reverse order
    rev = ""
    for character in a_string:
        rev = character + rev
    return rev



def main():
    """
    print("sum: ",count_down(10))
    print("sum: ",count_up(10))
    example_loop()
    """
    print_range(range(11))
    print_range(range(0, 21, 2))
    print_range_for(range(0, 20, 2))

main()
