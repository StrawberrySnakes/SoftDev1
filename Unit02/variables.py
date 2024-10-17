def variable_practice():
    age = 18 * 12
    num_of_days = 365
    first_pet = "Fishy"
    five_digits_of_pi = 3.1415
    print(age,num_of_days,first_pet,five_digits_of_pi)

def expressions_practice():
    x = 20
    y= 4+2+11
    z = 2**3
    a = 20 // 3
    b = 4 % 3
    c = 4*(3+12)
    d = (20 // ((4+3)*3))^2

    print(x,y,z,a,b,c,d)

def prompt_and_print():
    num1 = int(input("input a number: "))
    num2 = int(input("input a number: "))
    # you could also to x = int(x) after doing a normal input
    x = num1 + num2
    y = num1 - num2
    z = num1 * num2
    a = num1 / num2

    print(x, y, z, a)

def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()

main()