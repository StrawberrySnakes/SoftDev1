FOOD="Cheese"
DANCE = 3.1476
A_NUMBER = 12

def print_param(x):
    print(x)

def print_local():
    name = input("What is your name: ")
    print(name)

def print_which():
    FOOD = "Banana"
    print(FOOD)

def main():
    global FOOD
    global DANCE
    global A_NUMBER
    print_param(FOOD)
    print_param(DANCE)
    print_param(A_NUMBER)
    FOOD="Tomato"
    print_local()
    print_which()
    print(FOOD)

main()