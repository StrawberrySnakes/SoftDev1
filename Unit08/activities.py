#Sorts... sorting the values in some order
#lst.sort() origonal changed
#sorted(lst) copy made -- only use it if you need to keep the origonal (unless it's not already a list)

def squared(x):
    return x** 2

def double(x):
    return x * 2

def negate(x):
    return -x

def apply_transform(a_list, transform):
    # print(transform.__name__) to get the name of a function
    copy = list(a_list)
    for index in range(len(copy)):
        copy[index] = transform(copy[index])
    return copy



def main():
    a_list = list(range(51))
    print(apply_transform(a_list, squared))
    print(apply_transform(a_list, double))
    print(apply_transform(a_list, negate))

if __name__ == "__main__":
    main()



