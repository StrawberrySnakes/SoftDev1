import node

def length(node):
    count = 0
    while node is not None:
        count+=1
        node = node.get_next()
    return count

def total(node):
    sum = 0
    while node is not None:
        sum += node.get_value()
        node = node.get_next()
    return sum

# def length(a_node, count=0):
#     if a_node is None:
#         return count
#     else:
#         count+=1
#         next = node.Node.get_next(a_node)
#         return length(next, count)
    
# def total(a_node, sum=0):
#     if node is None:
#         return sum
#     else:
#         sum += node.Node.get_value(a_node)
#         next = node.Node.get_next(a_node)
#         return total(next, sum)

def main():
    print(length(None))
    sequence = node.Node(5, node.Node(7, node.Node(11, node.Node(13, node.Node(15)))))
    print(length(sequence))
    print(total(sequence))

if __name__ == "__main__":
    main()

