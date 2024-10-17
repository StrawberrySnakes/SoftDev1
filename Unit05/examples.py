#5.1 notes

"""

#how to open a file 
#put file path in open
#stores file in the variable
my_file = open("data/alice.txt")

my_file.close()


for line in my_file: #each line is a string
    length = len(line)
    print(length)




#when youre done using a file make sure to close it (.close())

def print_lines(filename):
    my_file = open(filename)
    for line in my_file:
        stripped = line.strip() #makes the spaces between go away
        print(stripped)

def main():
    print_lines("data/numbers_01.txt")

if __name__ == "__main__":
    main()


try: 
    x = int(input("x: "))
    y = int(input("y: "))

    print("x + y = " + str(x/y))
except ValueError:
    print("Invalid interger")
    print("try again")
except ZeroDivisionError:
    print("Cannot divide by zero")
except KeyboardInterrupt:
    print("User interrupted")
"""

def guessing_game():
    number = input("Pick a number: ")
    number = int(number)
    if number < 1 or number > 10:
        raise ValueError("Invalid guess!")
    print("You picked:", number)

guessing_game()