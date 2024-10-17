"""Dessa Shapiro"""
from list_stack import Stack
import re

#adds each line to a stack after making each character an element of a stack
def process_file(filename):
    with open(filename) as file:
        main_stack = Stack()
        for line in file:
            line_stack = Stack()
            for character in line:
                if character != " " and character != "\n":
                    line_stack.push(character)
                main_stack.push(line_stack)
        return main_stack
    
#idk why theyre so spaced out...
#this prints each character on a separate line
def process_stack(main_stack):
    while not main_stack.is_empty():
        line = main_stack.pop()
        while not line.is_empty():
            print(line.pop(), end=" ")
        print("\n")

#tests functions
def main():
    filename = "data/walrus.txt"  # or "strider.txt"
    main_stack = process_file(filename)
    process_stack(main_stack)

#code runs here
if __name__ == "__main__":
    main()



