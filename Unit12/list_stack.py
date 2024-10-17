"""Dessa Shapiro"""

#stack class that does stuff
class Stack:
    __slots__ = ["__items"]
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def is_empty(self):
        return len(self.__items) == 0
    
    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return str(self.__items)
    
    #checks if is empty then show last item in list
    def peek(self):
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self.__items[-1]

    #removes first item from list
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.__items.pop(0)
    