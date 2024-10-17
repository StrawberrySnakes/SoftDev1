"""Dessa Shapiro"""
import csv
import re

def find_rabbit():
    count = 0
    with open("alice.txt") as file:
        for line in file:
            tokens = line.split()
            if len(tokens) <= 0:
                pass
            index = 0
            for token in tokens:
                if token == "Rabbit":
                    count+=1
                    index+=1
                else:
                    index+=1
                    pass
    return count

def find_rabbit_regex():
    count = 0
    
    with open("alice.txt") as file:
        for line in file:
            #print(line)
            if re.findall("Rabbit\W*", line):
                count+= 1
            else:
                pass
    return count

def main ():
    print ("Found Rabbit", find_rabbit(), "times.") #should be 29
    print ("Found Rabbit", find_rabbit_regex(), "times.") #should be 45
    

if __name__ == "__main__":
    main ()