import math
import random

PI = 3.14159

def circumference(r):
    return 2 * PI * r

def aera(r):
    return PI * (r**2)


def squared(x):
    return math.pow(x, 2)

def cubed(x):
    return math.pow(x, 3)

def even_or_odd(n):
    if (n%2) == 0:
        return "Even"
    else:
        return "Odd"

def coin_toss():
    x = random.randrange(1,3)
    if x == 1:
        return "Heads"
    if x == 2:
        return "Tails"

def main():
    
    x = int(input("x: "))
    s=squared(x)
    print(s)
    c=cubed(x)
    print(c)
    e = even_or_odd(x)
    print(e)
    print(circumference(10))
    print(aera(10))
    
    print(coin_toss())
    print(coin_toss())
    print(coin_toss())
    print(coin_toss())
    print(coin_toss())
    """
    random.seed(100)
    print(random.randrange(1, 100))
    print(random.randint(1, 100))
    print(random.random())
    print(random.randrange(25, 75))
    print(random.randint(25, 75))
    print(random.random())
    print(random.random())
    print(random.random())
    print(random.random())
    """

if __name__ == "__main__":
    main()



"""
assert determines weather something is true or false. if true it will do nothing if false it will crash the page
- it is good for testing but not part of published program usually
False
True
True
True
False
False
True
False
True
False


False
True
True
False
False
True
True
False
True
False
True
typeerror 

9/18 monday:
slide 46 - I was able to intuitivly understand some syntext errors such as improper indentations 
Yes I have had to change spelling or tap which is relativly easy 
I know I have run into complicated errors but can't really call the specifics.
 If I remeber right I was working on a game and it would run but for some reason the controls were very glitchy and I couldnt figure out why
 I was finally able to find the problem which was caused by a tabed section thhat shouldnt have been. I had to use a debugger and go throught the code manually step by step.

 name error - z not defined
 indentation error
 syntac error 
 indentation error
 name error
 indentation error, syntext error, name error

 type error
 attribute error
 value error
 attribute error
 type error
 value error, dividebyzero


"""
