import csv
import re
def opener(filename):
    #try to open file
    try:
        with open(filename) as _:
            return True
    except:
        print("File not found")
        return False

    #return true if successful
    #return flase if not
    #close file

def first_only(filename):
    with open(filename) as file:
        reading = csv.reader(file)
        next(reading)
        for record in reading:
            first = record[0]
            print(first)

def names_and_adress(filename):
    with open(filename) as file:
        reading = csv.reader(file)
        next(reading)
        for record in reading:
            first = record[0]
            adress = record[1]
            print("Name: ",first)
            print("Adress: ",adress)

def averages(filname, colunm):
    with open(filname) as file:
        total = 0
        count = 0
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            grade = record[colunm]
            try:
                grade = float(grade)

                total += grade
                count += 1
            except:
                print("there be nothing there")


        return total/count

def zip_check(filename):
    with open(filename) as file:
        reading = csv.reader(file)
        next(reading)
        for record in reading:
            name = record[0]
            adress = record[1]
            if re.findall("[7-9]\d{4}", adress):
                print(name, adress)
            else:
                pass






def main():
    filename = input("Enter a filename: ")
    #print("Opened the file:", opener(filename))
    #print(names_and_adress(filename))
    #print(averages("data/full_grades_010.csv", 5))
    zip_check("data/full_grades_100.csv")


if __name__ == "__main__":
    main()
"""
1, 3, 2
12, 23
7, 7, 7, 7, 7, 7
778, 778
a, b, c, _, 1, 2. 3
_1
"""

"""
[RST][a-zA=Z]*
\d{3}-?\d{4}
\d{5}
\w+@rit.edu
[a-z]{2,3}\d{4}@rit.edu
"""

