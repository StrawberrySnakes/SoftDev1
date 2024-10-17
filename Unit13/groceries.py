import csv
import random
import array_queue
import node_stack

class GroceryItem:
    __slots__ = ["__name", "__weight", "__price"]
    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_price(self):
        return self.__price
    
    def __repr__(self):
        return "Grocery Item: "+\
                "\n Name:" + self.__name+\
                "\n Weight: " + str(self.__weight)+"lbs"+\
                "\n Price: $" + str(self.__price)
    def __str__(self):
        return self.__name +" ("+ str(self.__weight)+", $"+str(self.__price)+")"

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__name == other.__name
        else:
            return False

    def __hash__(self):
        return hash(self.__name)

    def __lt__(self, other):
        if type(self) == type(other):
            return self.__weight < other.__weight
        else:
            return False
        

class Customer:
    __slots__ = ["__shopping_list", "__cart", "__bags"]
    def __init__(self, shopping_list):
        self.__shopping_list = shopping_list
        self.__cart = set()
        self.__bags = []

    def get_bags(self):
        return self.__bags
    
    def shop(self, store):
        for name in self.__shopping_list:
            item = store[name]
            self.__cart.add(item)

    def unload(self, belt):
        for item in self.__cart:
            belt.enqueue(item)

    def checkout(self, belt):
        total = 0
        if len(belt) > 0:
            bag = node_stack.Stack()
            item = belt.dequeue()
            total += item.get_price()
            bag.push(item)

            while len(belt) > 0:
                item = belt.dequeue()
                total += item.get_price()
                if item.get_weight() <= bag.peek().get_weight():
                    bag.push(item)
                else:
                    self.__bags.append(bag)
                    bag = node_stack.Stack()
                    bag.push(item)
            self.__bags.append(bag)
        return total
    
    def unpack(self):
        bag_num = 0
        while len(self.__bags) > 0:
            bag_num += 1
            print("Bag #"+ str(bag_num)) 
            bag = self.__bags.pop()
            while len(bag) > 0:
                item = bag.pop()
                print(item)



            

        """
        if length bag 0 add item 
        if not check if the weight is less than or equil to next
        if it iss add it to bag
        if not add bag to a stack 
        """


    

def stock_store(filename):
    stock = {}
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            name = record[0]
            weight = int(record[1])
            price = int(record[2])
            item = GroceryItem(name, weight, price)
            stock[name] = item
    return stock

def main():
    stock = stock_store("data/groceries.csv")
    all_items = list(stock.keys())
    random.shuffle(all_items)
    shopping_list = all_items[:25]
    customer = Customer(shopping_list)

    belt = array_queue.Queue()
    customer.shop(stock)
    customer.unload(belt)
    # print(belt)

    total = customer.checkout(belt)
    print("$",total)

    customer.unpack()





    # print(stock)
    # groceries = [
    #     GroceryItem("Chocolate Chex", 1, 4),
    #     GroceryItem("Gummy Bears", 2, 8.99),
    #     GroceryItem("Roasted Chicken", 2.5, 9.99),
    #     GroceryItem("Bread", .75, 5.50),
    #     GroceryItem("Cap'n Crunch", 1.25, 5.50),
    # ]

    # print(groceries)
    # groceries.sort()






if __name__ == "__main__":
    main()