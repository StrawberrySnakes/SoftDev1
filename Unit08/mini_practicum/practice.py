"""Dessa Shapiro"""
import time

def in_place_reverse(a_list):
#Time cemplexity should be O(n) since everything is shifting over
    count = 0
    for _ in range(len(a_list)):
        x = a_list.pop(-1)
        a_list.insert(0 + count, x)
        count += 1

    return a_list

def make_multiplication_table():
    return [[i * j for j in range(1, 11)] for i in range(1, 11)]
    # table = []
    # columns = 10
    # rows = 10
    # value_c = 0
    # value_r = 0
    # for _ in range(columns):
    #     row = []
    #     for _ in range(rows):
    #         value = value_c * value_r
    #         row.append(value)
    #         value_c += 1
    #         value_r += 1

    #     table.append(row)
    # return table
    # table = [table for colunm in range(10) for]


def main():
    table = make_multiplication_table()
    for row in table:
        print(row)
    lst = [1, 2, 3, 4, 5]
    x = in_place_reverse(lst)
    print(x)

if __name__ == "__main__":
    main()
