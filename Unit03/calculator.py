#Creates a calculator that does addition, subtration, mult, division, and exponent
import math

#Addition function that returnes a string
def add(x, y):
    sum = x + y
    sum_string = "" + str(x) + " + " + str(y) + " = " + str(sum)+""
    return sum_string

#Subtraction function that returnes a string
def subtract(x, y):
    diff = x - y
    diff_string = "" + str(x) + " - " + str(y) + " = " + str(diff)+""
    return diff_string

#Multiplication function that returnes a string
def multiply(x, y):
    product = x*y
    product_string = "" + str(x) + " * " + str(y) + " = " + str(product)+""
    return product_string

#Division function that returnes a string
def divide(x, y):
    if y == 0:
        return "" + str(x) + " / " + str(y) + " = NaN " ""
    quotient = float(x/y)
    quotient_string = "" + str(x) + " / " + str(y) + " = " + str(quotient)+""
    return quotient_string

#Exponent function that returnes a string
def exponent(x, y):
    answer = math.pow(x, y)
    answer_string = quotient_string = "" + str(x) + "^" + str(y) + " = " + str(answer)+""
    return answer_string

# Calls all the math functions
def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print(add(x, y))
    print(subtract(x, y))
    print(multiply(x, y))
    print(divide(x, y))
    print(exponent(x, y))

#runs main 
if __name__ == "__main__":
    main()

# berries and cream fr fr