"""Dessa Shapiro"""
import time

# function that hashes the first character
def hash_first_char(a_string):
    if len(a_string) == 0:
        return 0
    code = ord(a_string[0])
    return code

#Hashes all the characters sum
def hash_sum(a_string):
    sum = 0
    if len(a_string) == 0:
        return 0
    for i in range(len(a_string)):
        letter = a_string[i]
        code = ord(letter)
        sum += code
    return sum
#the sum with extra function 
def hash_positional_sum(a_string):
    sum = 0
    if len(a_string) == 0:
        return 0
    for i in range(len(a_string)):
        letter = a_string[i]
        code = ord(letter)
        sum += code * (31**(len(a_string)-(i + 1)))
    return sum

#using long line words creates a dic to detect collisions
def build_collision_counter(hash_func=hash):
    collisions_dict = {}
    
    with open("data/long_line_words.txt") as file:
        for line in file:
            line= line.strip()
            hashed = hash_func(line)
            if hashed in collisions_dict:
                collisions_dict[hashed] += 1
            else:
                collisions_dict[hashed] = 0
            
    return collisions_dict

#test different hash functions for different collision data
def hash_test(collisions_dict, hash_func=hash):
    name = hash_func.__name__
    total_collisions = 0
    max_collisions = 0
    total_keys = len(collisions_dict)
    unique_keys = len([key for key in collisions_dict if collisions_dict[key] == 0])  # Count unique keys with no collisions
    for key in collisions_dict:
        count = collisions_dict[key]
        if count > 0:
            total_collisions += count-1
        if count > max_collisions:
            max_collisions = count

    if total_keys > 0:
        total_collision_rate = (total_collisions/total_keys) *100
    else:
        total_collision_rate = 0

    if total_keys > 0:
        spread = (unique_keys / total_keys) * 100
    else:
        spread = 0

    start = time.perf_counter()
    with open("data/long_line_words.txt") as file:
        for line in file:
            line = line.strip()
            _ = hash_func(line)
    end = time.perf_counter()
    total_time = end - start

    print("Name: ", name)
    print("total collisions rate: ", round(total_collision_rate,2),"%")
    print("maximum collisions: ", max_collisions)
    print("spread: ", round(spread, 2),"%")
    print("speed: ", round(total_time,2),"sec")
    print()


#for each hash function it calls the test to get data
def main():
    hash_functions = [hash, hash_first_char, hash_sum, hash_positional_sum]
    for hash_function in hash_functions:
        collision_counter = build_collision_counter(hash_function)
        hash_test(collision_counter, hash_function)
    # a = str("A") * 100
    # b = "a"
    # print(hash_sum(a))
    # print(hash_sum(b))
    # print(hash_positional_sum(a))
    # print(build_collision_counter())

#code runs here
if __name__ == "__main__":
    main()