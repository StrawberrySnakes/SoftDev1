import node

class Stack:
    __slots__ = ["__top", "__size"]
    def __init__(self):
        self.__top = None
        self.__size = 0

    
    def is_empty(self):
        if self.__top is None:
            return True
        return False
    
    def push(self, value):
        new_node = node.Node(value)
        new_node.set_next(self.__top)
        self.__size += 1
        self.__top = new_node

    def pop(self):
        temp = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return temp


    def peek(self):
        return self.__top.get_value()
    
    def __str_rec(self, node, string=""):
        if node is None:
            return string
        else:
            string = string + ", " + str(node.get_value())
            next = node.get_next()
            return self.__str_rec(next, string)
        
    def __len__(self):
        return self.__size
        # node = self.__top
        # count = 0
        # while node is not None:
        #     count+=1
        #     node = node.get_next()
        # return count
    
    def __str__(self):
        # if self.__top is None:
        #     return "[]"
        # else:
        #     string = "[" + str(self.__top.get_value())
        #     next = self.__top.get_next()
        #     string = self.__str_rec(next, string)
        #     return string + "]"

        if self.__top is None:
            return "[]"
        else:
            string = "[" + str(self.__top.get_value())
            next = self.__top.get_next()
            while next is not None:
                string += ", " + str(next.get_value())
                next = next.get_next()
            return string + "]"


def main():
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)

    print(len(stack))
    while not stack.is_empty():
        value = stack.pop()
        print(value, end="")
    print()
    print(stack.is_empty())


if __name__ == "__main__":
    main()