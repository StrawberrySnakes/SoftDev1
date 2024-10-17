#This code lets the user imput a number and get the factorial, square root and truncation??? or whatever it's called
import math

#Return the factorial of x/ only works with ints 
def fact(x):
    x = int(x)
    if x<0:
        return 0
    x = float(math.factorial(x))
    return x

#Returns the square root of parameter x
def root(x):
    if x<0:
        return 0
    x = (math.sqrt(x))
    return x

#returns the trunc of parameter x 
def trunk(x):
    x=float(math.trunc(x))
    return x

#asks user for an integer then calls functions above to print outcomes 
def main():
    x = float((input("Enter a Number: ")))
    f = fact(x)
    print(f)
    r = root(x)
    print(r)
    t = trunk(x)
    print(t)

# So it can be tested through the indavidual functions not main
if __name__ =="__main__":
    main()