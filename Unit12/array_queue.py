import arrays
from node import *

class Queue:
    __slots__ = ["__elements", "__front", "__back", "__size"]
    def __init__(self):
        self.__elements = arrays.Array(3)
        self.__front = 0
        self.__back = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0
    
    def __len__(self):
        return self.__size
    
    def __increment(self, index):
        return (index + 1) % len(self.__elements)
    
    def resize(self):
        size = self.__size * 2
        new = arrays.Array(size)
        source = self.__front
        for dest in range(self.__size):
            new[dest] = self.__elements[source]
            source = self.__increment(source)
        self.__front = 0
        self.__back = self.__size
        self.__elements = new

    
    def enqueue(self, value):
        self.__elements[self.__back] = value
        self.__back = self.__increment(self.__back)
        self.__size += 1

    def dequeue(self):
        if self.__size == 0:
            raise IndexError("Empty")
        temp = self.__elements[self.__front]
        self.__elements[self.__front] = None
        self.__front = self.__increment(self.__front)
        self.__size -= 1
        return temp
    
    def __str__(self):
        if self.__size == 0:
            return "[]"
        else:
            string = "[" + str(self.__elements[self.__front])
            index = self.__increment(self.__front)
            while index != self.__back:
                string += ", " + str(self.__elements[index])
                index = self.__increment(index)
            return string + "]"
        


    def front(self):
        if self.__size == 0:
            raise IndexError("Empty")
        return self.__elements[self.__front]
    
    def back(self):
        if self.__size == 0:
            raise IndexError("Empty")
        index = self.__back - 1
        if index < 0:
            index = len(self.__elements) - 1
        return self.__elements[index]
