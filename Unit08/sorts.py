import random

def random_list(length):
    # lst = []
    # for _ in range(length):
    #     lst.append(random.randint(0, length))
    # return lst

    lst = [random.randint(0, length) for _ in range(length)]
    return lst

def swap(a_list, a, b):
    a_list[a], a_list[b] = a_list[b], a_list[a]

def shift(a_list, index):
    while index != 0 and a_list[index-1] > a_list[index]:
        swap(a_list, index-1, index)
        index -= 1

def insertion_sort(a_list):
    for index in range(len(a_list)):
        shift(a_list, index)

def shift_pt2(a_list, index):
    target = a_list[index]

    while index > 0 and a_list[index-1] > target:
        a_list[index] = a_list[index -1]
        index -= 1

    a_list[index] = target

def insertion_sort_wo_swap(a_list):
    for index in range(len(a_list)):
        shift_pt2(a_list, index)

def split(a_list):
    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]
    return left, right

def merge(left, right):
    ri= 0
    li = 0
    m_lst = []
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            m_lst.append(left[li])
            li += 1
        else:
            m_lst.append(right[ri])
            ri+=1
    if li < len(left):
        m_lst += left[li:]
    else:
        m_lst += right[ri:]

    return m_lst

def partition(a_list, pivot):
    less = []
    same =[]
    more = []
    for value in a_list:
        if value < pivot:
            less.append(value)
        elif value > pivot:
            more.append(value)
        else:
            same.append(value)

    return less, same, more

def choose_first(a_list):
    return a_list[0]
def choose_mid(a_list):
    mid = len(a_list) // 2
    return a_list[mid]
def choose_random(a_list):
    rand = random.randint(0, len(a_list)-1)
    return a_list[rand]

def quicksort(a_list, pivot_picker=choose_first):
    if len(a_list) < 2:
        return a_list
    else:
        pivot = pivot_picker(a_list)
        less, same, more = partition(a_list, pivot)
        sorted_less = quicksort(less, pivot_picker)
        sorted_more = quicksort(more, pivot_picker)
        return sorted_less + same + sorted_more
def quicksort_mid(a_list):
    return quicksort(a_list, choose_mid)

def quicksort_random(a_list):
    return quicksort(a_list, choose_random)


def merge_sort(lst):
    length = len(lst)
    if length < 2:
        return lst
    else:
        left, right = split(lst)
        ls = merge_sort(left)
        rs = merge_sort(right)
        m = merge(ls, rs)
        return m

def main():
    lst = random_list(20)
    q = quicksort(lst)
    s = quicksort(lst, choose_mid)
    r = quicksort(lst, choose_random)
    print(q)
    print(s)
    print(r)
    #left, right = split(lst)
    #print(left, right)
    # print(lst)
    # m = merge_sort(lst)
    # print(m)
    # a_list = random_list(10)
    # print(a_list)
    # insertion_sort_wo_swap(a_list)
    # print(a_list)

    #swap(a_list, 0, 3)
    #print(a_list)
    
if __name__ == "__main__":
    main()


"""
[10, 3, 5, 6] [1, 4, 8, 7]
[10, 3] [5, 6] [1, 4] [8, 7]
[10] [3] [5] [6] [1] [4] [8] [7]
[3, 10] [5, 6] [1, 4] [7, 8]
[3, 5, 6, 10] [1, 4, 7, 8]
[1, 3, 4, 5, 6, 7, 8, 10]
""" 