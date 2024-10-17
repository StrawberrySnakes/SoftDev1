
class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

BANANA = Fruit("Banana", 2.15)

ORANGE = Fruit("Orange", 1.00)

PINEAPPLE = Fruit("Pineapple", 3.20)

POMOGRANATE = Fruit("Pomogranate", 3.98)

FRUITS = {
    BANANA.name:BANANA,
    ORANGE.name:ORANGE,
    PINEAPPLE.name:PINEAPPLE,
    POMOGRANATE.name:POMOGRANATE
}

def add_to_basket(basket, name):
    if name in FRUITS:
        fruit = FRUITS[name]
        basket.append(fruit)

def total_price(basket):
    total = 0
    for fruit in basket:
        total += fruit.price
    return total 

def count_fruit(basket, fruit):
    count = 0
    for f in basket:
        if f is fruit:
            count+= 1
    return count 

def main():
    sentinel = True
    basket=[]
    while sentinel:
        name = input("fruits: ")
        if name == "":
            sentinel=False
        else:
            add_to_basket(basket, name)
    print("bananas:", count_fruit(basket, BANANA))
    print("oranges:", count_fruit(basket, ORANGE))
    print("pineapples:", count_fruit(basket, PINEAPPLE))
    print("pomgranates:", count_fruit(basket, POMOGRANATE))
    print("total cost:", total_price(basket))




if __name__ =="__main__":
    main()

    
    
    