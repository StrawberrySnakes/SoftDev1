"""Dessa Shapiro"""
#initiate dictionarys
PRICES = {
    "co":2.30,
    "le":3.00,
    "wa":2.10,
    "ta":3.50,
    "bu":6.00,
    "en":6.50,
    "ch":3.15,
    "sa":1.00,
    "gu":1.80
}

MENU = {
    "Drinks":{"co":"coke","le":"lemonaid","wa":"water"},
    "Entrees":{"ta":"taco", "bu":"burrito", "en":"enchalata"},
    "Sides":{"ch":"chips", "sa":"salsa", "gu":"guacamole"}
}

#class combo which has drink, entree, side and price 
class Combo:
    def __init__(self, drink, entree, side, price):
        self.drink=drink
        self.entree=entree
        self.side=side
        self.price = price

#gruops a dink, entree and side together, and calculates their price
def create_combo(drink, entree, side, prices):
    price = prices[drink] + prices[entree] + prices[side]
    return Combo(drink, entree, side, round(price, 2))

#Prints the menu
def print_menu(menu, prices):
    print("MENU\nAll meals are a combo!\n")
    for meal_type in menu:
        food_items = menu[meal_type]
        print(meal_type)
        for code in food_items:
            name = food_items[code]
            if code in prices:
                price = prices[code]
                print(name + "(" + code + "): $" + str(round(price, 2)), end="")
            print()

#asks the user to input options from menu and returns it
def order(MENU, PRICES):
    order = []
    while True:
        drink = input("What would you like to drink: ").strip()
        entree = input("What would you like for your entree: ").strip()
        side = input("What would you like for your side: ").strip()

        if drink not in PRICES or entree not in PRICES or side not in PRICES:
            print("Invalid item(s). Please select from the menu.")
            continue

        combo = create_combo(drink, entree, side, PRICES)
        order.append(combo)

        add_more = input("Drink: " + MENU['Drinks'][drink] + ", Entree: " + MENU['Entrees'][entree] + ", Side: " + MENU['Sides'][side] + ", Price: $" + str(round(combo.price, 2)) + "\nWould you like to add another combo (Y/N): ")
        
        if add_more.strip().lower() != 'y':
            break
    return order

#prints the users imputed order and price
def print_order(MENU):
    print("Your order is:")
    for combo in order:
        print(f"Drink: {MENU['Drinks'][combo.drink]}, Entree: {MENU['Entrees'][combo.entree]}, Side: {MENU['Sides'][combo.side]}, Price: ${combo.price}")
    
    total_price = sum(combo.price for combo in order)
    print("Total: $", round(total_price, 2))
    
#calls print menu and print order
def main():
    print_menu(MENU, PRICES)
    take_order = order(MENU, PRICES)
    print_order(take_order)

#code runs here
if __name__ =="__main__":
    main()
