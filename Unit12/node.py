class Node:
    __slots__ = ["__value", "__next"]
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next
    
    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value
    
    def get_next(self):
        return self.__next
    
    def set_next(self, next):
        self.__next = next
    
    def __str__(self):
        return str(self.__value) + " -> " + str(self.__next)
    


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node3.set_next(node2)
    node2.set_next(node1)
    print(node3)

    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    print(node3)

    sequence = Node(3, Node(2, Node(1)))
    print(sequence)
    
    
    
    
    print(node3)




if __name__ == "__main__":
    main()

    