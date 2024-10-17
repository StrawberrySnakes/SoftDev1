""" I plan do study the theory more and look back through the slides on each unit
so that I don't bomb the final multiple choice"""
#UNIT 5
import csv
import re
import array_utils
def starts_with(filename, letter):
    with open(filename) as file:
        count = 0
        for line in file:
            line.strip()
            words = line.split()
            for word in words:
                if word[0].lower() == letter:
                    count+=1
        return count
    
def zip_lookup(filename, zipcode):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            for record in reader:
                if record[0] == zipcode:
                    return record[1]
                else:
                    pass
    except FileNotFoundError:
        print("file does not exist")

    except ValueError:
        print("wrong")

#UNIT 6
import arrays
def is_power(a, b):
    if a == 1:
        return True
    elif a%b == 0 and is_power(a/b, b):
        return True
    return False

def what_power(a, b):
    if a == 1:
        return 0
    elif a%b == 0 and is_power(a/b, b):
        return 1 + what_power(a/b, b)
    raise ValueError

def fill_array(an_array, start=0, step=1, index=0):
    an_array[index] = start
    if index < len(an_array) - 1:
        return fill_array(an_array, start+step, step, index+1)
    
def arrays_equal(array_1, array_2, index=0):
    if len(array_1) != len(array_2):
        return False
    
    if index < len(array_1)-1:
        if array_1[index] == array_2[index]:
            return arrays_equal(array_1, array_2, index+1)
        else:
            return False
    return True

#UNIT 7

def tuplify():
    first = input("Enter first name: ")
    middle = input("Enter middle name: ")
    last = input("Enter Last name")
    if middle == "":
        return(first, last)
    return (first, middle, last)

def cubed(a_list):
    for index in range(len(a_list)):
        value = a_list[index]
        a_list[index] = value ** 3
    return a_list

def reversal(a_list):
    b_list = []
    for _ in range(len(a_list)):
        value = a_list.pop()
        b_list.append(value)
    return b_list










        



    

def main():
    # x = starts_with("data/atotc.txt", "b")
    # print(x)
    # y = zip_lookup("data/zip_codes.csv", "94960")
    # print(y)

    # print(is_power(9, 3))
    # print(is_power(9, 4))
    # print(what_power(9, 3))

    # a = arrays.Array(10)
    # print(fill_array(a))

    # b = arrays.Array(10)
    # print(fill_array(a))

    # print(arrays_equal(a, b))

    a_list = [1, 2, 3, 4]
    print(cubed(a_list))

    print(reversal(a_list))

if __name__ == "__main__":
    main()
