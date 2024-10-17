import time
import sorts
import random

def sort_timer(a_list, sort_function):
    copy = list(a_list)
    start = time.perf_counter()
    sort_function(copy)
    end = time.perf_counter()
    return end - start

def main():
    a = list(range(3000))
    print("Sorted insertion: ", sort_timer(a, sorts.insertion_sort))
    print("Sorted insertion Wo Swap: ", sort_timer(a, sorts.insertion_sort_wo_swap))
    print("Sorted Merge Sort", sort_timer(a, sorts.merge_sort))
    print("Sorted quickort mid", sort_timer(a, sorts.quicksort_mid))
    print("Sorted quickort rand", sort_timer(a, sorts.quicksort_random))

    b = sorts.random_list(3000)
    print("Random insertion: ", sort_timer(b, sorts.insertion_sort))
    print("Random insertion Wo Swap: ", sort_timer(b, sorts.insertion_sort))
    print("Random Merge Sort", sort_timer(b, sorts.merge_sort))
    print("Random quickort", sort_timer(b, sorts.quicksort))
    print("Random quickort mid", sort_timer(b, sorts.quicksort_mid))
    print("Random quickort rand", sort_timer(b, sorts.quicksort_random))

    c = list(range(3000, 0, -1))
    print("Reverse insertion: ", sort_timer(c, sorts.insertion_sort))
    print("Reverse insertion Wo Swap: ", sort_timer(c, sorts.insertion_sort))
    print("Reverse Merge Sort", sort_timer(c, sorts.merge_sort))
    #print("Reverse quickort", sort_timer(c, sorts.quicksort))
    print("Reverse quickort mid", sort_timer(c, sorts.quicksort_mid))
    print("Reverse quickort rand", sort_timer(c, sorts.quicksort_random))
    


if __name__ == "__main__":
    main()

