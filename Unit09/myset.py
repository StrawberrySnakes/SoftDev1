def make_myset(length, hash_func= hash):
    table = [[] for _ in range(length)]
    return (hash_func, table)

def add(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hash_code = hash_func(element)
    index = hash_code % len(table)
    chain = table[index]
    for value in chain:
        if value == element:
            return
    chain.append(element)
    



def contains(myset, element):
    hash_func = myset[0]
    table = myset[1]
    hash_code = hash_func(element)
    index = hash_code % len(table)
    chain = table[index]
    for value in chain:
        if element == value:
            return True
    return False

def worst_hash_function(value):
    return 4

def main():
    myset = make_myset(7)
    print(myset)
    add(myset, "abc")
    add(myset, "def")
    add(myset, "ghi")
    add(myset, "abc")
    add(myset, "kls")
    print(myset)


if __name__ == "__main__":
    main()