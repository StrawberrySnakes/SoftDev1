def indexing():
    thing = "smolfrogeatscheese"
    length = len(thing)
    print(length)
    print(thing[0])
    print(thing[-1])

    print(thing[4])
    print(thing[8])

    print(thing[-length])

def concat():
    a = "apples"
    z = a
    b = "bananas"
    a = a + b
    print(a)
    cat = "orange" + "kitty"
    y = ''
    y += "p"
    y += "i"
    y += "g"
    print(y)
    print(cat)

def main():
    indexing()
    concat()

main()