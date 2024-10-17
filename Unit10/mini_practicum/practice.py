"""Dessa Shapiro"""
import re 

#creates a dictionary holding each a-z letter and how often
#it appears in a file
def make_letter_frequency(filename):
    with open(filename) as file:
        letters_dict = {}
        for line in file:
            line.strip()
            words = line.split()
            for word in words:
                word = word.lower()
                for character in word:
                    if re.findall("[a-z]", character):
                        if character in letters_dict:
                            letters_dict[character] += 1
                        else:
                            letters_dict[character] = 1
                    else:
                        pass
    return letters_dict

#Prints out a dict with each key and value on a separate line
#also gits the key with the largest numerical value
def print_letter_frequency(letter_dict):
    largest = 0
    largest_key = 0
    for key in letter_dict:
        print(key, ":" ,letter_dict[key])
        if letter_dict[key] > largest:
            largest= letter_dict[key]
            largest_key = key
    print("The most popular letter:" ,largest_key, largest)

#does some SUPER cool stuff 
def main():
    letter_dict1 = make_letter_frequency("../data/rit_mission.txt")
    letter_dict2 = make_letter_frequency("../data/alice.txt")
    print("Charaters from rit_mission.txt:")
    print_letter_frequency(letter_dict1)
    print("\nCharaters from alice.txt:")
    print_letter_frequency(letter_dict2)

#code runs here
if __name__ == "__main__":
    main()