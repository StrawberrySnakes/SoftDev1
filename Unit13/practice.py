"""Dessa Shapiro"""
import array_queue
import node_stack
import random

def reverse_digits(integer):
    str_int = str(integer)
    results = node_stack.Stack()
    for character in str_int:
        results.push(character)
    new = ""
    while results.__len__() > 0:
        new += results.pop()


    return int(new)

def hot_potato(names):
    order = array_queue.Queue(len(names))
    for name in names:
        order.enqueue(name)
    while order.__len__() > 1:
        tosses = random.randint(1, 5)
        while tosses >= 1:
            first = order.dequeue()
            print(first, "tosses the potato to" ,order.front())
            order.enqueue(first)  
            tosses -=1 
        first = order.dequeue()
        print("The music stops and" ,first, "Is holding the potato")
    else:
        print("The game is over!",order.front()," wins the game!")

def main():
    x = reverse_digits(1234)
    y = reverse_digits(1000)
    print(x, y)
    names = ["Bob", "Jaff", "Jarry"]
    hot_potato(names)


if __name__ == "__main__":
    main()


    