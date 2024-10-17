"""Dessa Shapiro"""
import random
import arrays
import array_utils
import time
#Cant change a tuple
def tuples(a_tuple):
    print(len(a_tuple))
    print(a_tuple)
    for element in a_tuple:
        print(element)

def packer():
    a = 30
    b ="fjif"
    c = 45.3
    return a, b, c

def lists():
    list_a = [ "a", 15, "ty", 21.45, False, [1, 2, 3], (3, "a")]
    for index in range(len(list_a)):
        print(index,":",list_a[index])
    list_a[2] = 30.6
    return list_a

def make_list(a_sequence):
    lst = []
    for value in a_sequence:
        lst.append(value)
        print(lst, len(lst))

    return lst

def scale(a_list, scalar):
    for index in range(len(a_list)):
        a_list[index] = a_list[index] * scalar
    return a_list
    

def mutator(a_list, a_int):
    print(a_list, a_int)
    a_list[0] *= 5
    a_int *= 5
    print(a_list, a_int)

def cat(a_list, b_list):
    a_list = a_list + b_list
    return a_list

def extender(a_list, b_list):
    a_list += b_list
    return a_list

def inserter(a_list, value):
    index = len(a_list)//2
    a_list.insert(index, value)

def popper(a_list):
    if len(a_list) == 0:
        return 
    else:
        rand = random.randrange(len(a_list))
        value = a_list.pop(rand)
        print(a_list, value)
        popper(a_list)

def array_insert(an_array, index, value):
    length = len(an_array)
    copy = arrays.Array(length+1)
    for i in range(index):
        copy[i]= an_array[i]

    copy[index] = value

    for i in range(index, length):
        copy[i+1] = an_array[i]

    return copy, an_array

def array_pop(an_array, index):
    length = len(an_array)
    copy = arrays.Array(length-1)
    for i in range(index):
        copy[i] = an_array[i]
    
    popped = an_array[index]

    for i in range(index+1, length):
        copy[i]= an_array[i-1]
    
    return copy, popped

def reverse_sequence(a_sequence):
    copy = []
    start = time.perf_counter()
    for index in range(len(a_sequence)-1, -1, -1):
        copy.append(a_sequence[index])
    end = time.perf_counter()
    print("time: ",(end-start))
    return copy

def slice(lst, start, stop, step):
    copy = []
    for index in range(start, stop, step):
        copy.append(lst[index])
    return copy

def slices():
    quote = "You're a god damned genius Gump"
    lst = []
    for character in quote:
        lst.append(character)
    print(lst)
    print(lst[:6])
    print(lst[7:8])
    print(lst[10:13])
    print(lst[14:20])

def dices(a_list):
    if len(a_list) == 0:
        return
    else:
        index = random.randrange(0, len(a_list))
        elements = a_list[index:index+1]
        print(a_list, elements)
        left = a_list[index]
        right = a_list[index+1]
        dices(left + right)

def swapper(a_list):
    mid = len(a_list)//2
    lst = []

    for index in range(mid, len(a_list)):
        lst.append(a_list[index])

    for index in range(0, mid):
        lst.append(a_list[index])

    return lst

def chuncky(a_list, size):
    start = 0 
    while start < len(a_list):
        slice = a_list[start:start+size]
        print(slice)
        start+= size


def list_comp():
    #creates a list with 15 0s
    a = [0 for _ in range(15)]
    #this copies the value into the list
    b = [x for x in range(15)]
    c = [x*2 for x in range(15)]
    # can add conditionals to list
    d = [n for n in range(200, 401) if n%4 == 0]

def comprehension():
    a = [letter for letter in str("foobar")]
    print(a)
    b = [0 for _ in range(15)]
    print(b)
    c = [x for x in range(0, 13)]
    print(c)
    d = [x for x in range(0, 21) if x%2 == 0]
    print(d)
    e = [x for x in range(0, 51) if x < 50 and (x%3 == 0 or x%5==0)]
    print(e)

def make_table(rows, columns, value):
    table = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(value)
        table.append(row)

    return table
    #list comp
    #return [[value for _ in range(columns)] for _ in range(rows)]

def random_list(size):
    lst = []
    for _ in range(size):
        lst.append(random.randint(0, 100))
    return lst
    #return [random.rantint(0, 100) for _ in range(size)]

def sorted_test(a_list):
    print(a_list)
    copy = sorted(a_list)
    print(a_list)
    print(copy)
    
def sort_test(a_list):
    print(a_list)
    a_list.sort()
    print(a_list)

def other():
    """Reverse"""
    a =[5, 6, 3, 4, 2, 7, 3, 9, 1]
    #stays the same
    b = sorted(a, reverse=False)
    #reverses the order
    b = sorted(a, reverse=True)
    a.sort(reverse=True)

    """Key Function"""
    x = ["Zoo", "Monkey", "aardvark", "donkey"]
    #if we want to sort by length
    x.sort(ken=len)
    #does len revered
    x.sort(key=len, reverse=True)
    #String.. this will turn to lowercase
    a = str.lower("ABC")
    #
    x.sort(key=str.lower)

def suit_key(card):
    value = 0
    if card[1] == "Dimonds":
        value+= 100
    elif card[1] == "Hearts":
        value+= 200
    elif card[1] == "Spades":
        value+= 300

    return value + card[0]

def main():
    hand = [
        (10, "Hearts"),
        (2, "Spades"),
        (5, "Clubs"),
        (10, "Dimonds"),
        (2, "Clubs")
    ]

    hand.sort(key = suit_key)
    print(hand)
    """
    a_list = [3, 6, 2, 7, 9, 5, 4, 7]
    print(random_list(10))
    sorted_test(a_list)
    sort_test(a_list)

    
    table = make_table(4, 6, 0)
    print(table)
    for row in table:
        print(row)
    
    comprehension()
    
    lst = list(range(100))
    chuncky(lst, 7)
    
    print(swapper(lst))
    X
    lst = list(range(1, 51))
    copy = slice(lst, 9, 31, 3)
    print(copy)
    
    rng = range(1, 100)
    lst = reverse_sequence(rng)
    an_array = arrays.Array(4)
    an_array[0]= "a"
    an_array[1]= "b"
    an_array[2]= "c"
    an_array[3]= "d"

    print(array_insert(an_array, 2, "v"))
    print(an_array)

    blah, pop = array_pop(an_array, 2)
    print(blah, pop)
    
    tupa = (1, 2, "a", 4)
    tuples(tupa)
    x = packer()
    print(x)
    x, y, z = packer()
    print(x)
    print(y)
    print(z)
   
    x = lists()
    print(x)
    
    
    lst1 = [2.2, 4.4, 8.8, 16.16]
    print(scale(lst, 3))
    print(scale(lst1, .5))
    print(lst, int)
    mutator(lst, int)
    print(lst, int)
    
    lsta = [1, 2, 3, 4]
    lstb = [5, 6, 7, 8]
    extender(lsta, lstb)
    lstc = extender(lsta, lstb)
    print(lstc)
    print(lsta, lstb)
    for i in range(10):
        inserter(lst, i)
        print(lst)

    popper(lst)
    """

if __name__ == "__main__":
    main()

"""
a = [1, 2, 3]
b = a
a.append(2)
a
a is b 
True
x = 5
y = 5
x is y true
z=5.0
x is z False
x == z True
a == b True
c = [1, 2, 3]
a is c Flase
a == c True
copares memorary adresses for is(shallow)
"""

