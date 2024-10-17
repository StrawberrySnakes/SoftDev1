import arrays
import timing
import random
import time

def unique_array(an_array, value):
    #array full of none values
    for index in range(len(an_array)):
        if value == an_array[index]:
            return
        elif an_array[index] is None:
            an_array[index] = value
            return
        
def fill_array(length):
    an_array = arrays.Array(length, None)
    for index in range(length):
        unique_array(an_array, index)
    return an_array

def unique_list(a_list, value):
    for current in a_list:
        if current == value:
            return
    a_list.append(value)
        
def fill_list(length):
    a_list = []
    for value in range(length):
        unique_array(a_list, value)
    return a_list

def unique_set(a_set, value):
    if value not in a_set:
        a_set.add(value)
        
def fill_set(length):
    a_set = set()
    for value in range(length):
        unique_set(a_set, value)
    return a_set

def mixup():
    s = set("abcdefgh")
    for value in s:
        print(value, end=" ")
    print()
    print(sorted(s))

#****** important *******
def coupon_collector(n):
    s = set()
    count = 0
    while len(s) < n:
        coupon = random.randint(1, n)
        s.add(coupon)
        count+=1
    return count



# def sets():
#     s = {1, True, 3.4, 4, "r"}
#     print(s)
#     s.add("oogly")
#     s.add(5)
#     s.add(9)
#     s.add(4)
#     print(s)
#     s1 = set("abcd")
#     print(s1)
def unique_words(filename):
    with open(filename) as file:
        uwords = set()
        for line in file:
            words = line.split()
            for word in words:
                uwords.add(word)
        return uwords

def superset(a, b):
    if len(a) > len(b):
        for vlaue in b:
            if vlaue not in a:
                return False
        return True
    else:
        return False
    
def subset(a, b):
    for vlaue in a:
            if vlaue not in b:
                return False
    return True

def intersection(a, b):
    i = set()
    if len(a) >= len(b):
        for value in a:
            if value in b:
                i.add(value)
    else:
        for value in b:
            if value in a:
                i.add(value)
    return i

def union(a, b):
    u = set()
    for vlaue in a:
        u.add(vlaue)
    for vlaue in b:
        u.add(vlaue)
    return u

def minus(a, b):
    for value in b:
        if value in a:
            a.remove(value)
    return a

def names():
    d = {} # dict()
    d["D"]= "Dessa"
    d["J"]= "Jean"
    d["S"]="Shapiro"
    d["X"]= "hi"
    print(d)
    if "X" in d:
        x = d["X"]
        print(x)
    x, y, z = d["D"], d["J"], d["S"]
    print(x, y, z)

    # for initial in names:
    #     name = names[initial]
    #     print(initial, ":", name)

def count_words(filename):
    with open(filename) as file:
        dic = {}
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word not in dic:
                    dic[word] = 0
                dic[word] += 1
    return dic


def find_maximum(d):
    max_key = None
    max_value = None
    for key in d:
        value = d[key]
        if max_value == None or max_value < value:
            max_value = value
            max_key = key
    return max_key, max_value      

#runs in linear time
def hashes():
    # s = "a" * 1000000
    
    # hc = hash(s)
    # print(hc)
    s1 = "a" * 10000000
    hd = hash(s1)
    print(hd)

def collisions(filename, length, hash_func=hash):
    with open(filename) as file:
        count = 0
        an_array = arrays.Array(length)
        for line in file:
            hash_code = hash_func(line)
            index = hash_code % length
            if an_array[index] is None:
                an_array[index] = line
                count +=1
            elif an_array[index] == line:
                continue
            else:
                break
    return count

def string_hash(a_string):
    max_value = ord(a_string[0])
    for character in a_string[1:]:
        ascii_code = ord(character)
        if ascii_code > max_value:
            max_value = ascii_code
    return max_value * len(a_string)

    
def main():
    col = collisions("data/alice.txt", 100, string_hash)
    print(col)
    # timing.time_function(hashes)
    # word_count = count_words("data/alice.txt")
    # print(word_count)

    # most_word = None
    # most_count = -1
    # for word in word_count:
    #     count = word_count[word]
    #     if count > most_word:
    #         most_count = count
    #         most_word = word

    # tupes = []
    # for word in word_count:
    #     count = word_count[word]
    #     tupe = (count, word)
    #     tupes.append(tupe)
    # tupes.sort(reverse=True)
    # top_20 = tupes[:20]
    # for word in top_20:
    #     print(word[1], ":", word[0])

    #top_20 = sorted([(word_count[key], key)) for key in word_counts], reverse = True[:print(top_20)])
    # names()
    # a = {1, 2, 3, 4, 5}
    # b = {2, 3, 4}
    # c = {3, 4, 5}
    # print(superset(a, b))
    # print(subset(b, a))
    # print(intersection(b, c))
    # print(union(b, c))
    # print(minus(a, b))
    # uw = unique_words("data/alice.txt")
    # print(len(uw))
    # sum = 0
    # count = 0
    # for _ in range(100):
    #     c = coupon_collector(10000)
    #     sum += c
    #     count+=1
    # print(sum/count)

    # an_array = timing.time_function(fill_array, 5000)
    # a_list = timing.time_function(fill_list, 5000)
    # a_set = timing.time_function(fill_set, 5000)
    # mixup()
    # mixup()
    # mixup()


if __name__ == "__main__":
    main()
        

