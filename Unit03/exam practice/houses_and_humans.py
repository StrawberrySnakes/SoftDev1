import random
def roll_dice(number_of_sides, quantity):
    x = random.randint(1, number_of_sides)
    y = x*quantity
    return y
    
    
def main():
    print(roll_dice(6, 3))

main()

