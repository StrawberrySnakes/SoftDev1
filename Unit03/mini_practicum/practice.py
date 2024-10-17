
#This program first gets your height in inches and translates it to feet and inches then it uses ASCII to find the 3 letters in the alphebet after the one you input as a parameter

#This function converts height in inches to height in feet and inches
def convert_height():
    height_inches = int(input("Enter your height in inches: "))
    hight_feet = height_inches//12
    height_inches_two = height_inches % 12
    print("You are ",hight_feet,"'",height_inches_two,'" tall.', sep="")

#This function takes a letter and finds the 3 letters that come after in alphabeticaly
def before(letter):
    letter_code = ord(letter)
    first_letter = letter_code + 1 
    first_letter_char = chr(first_letter)
    second_letter = letter_code + 2 
    second_letter_char = chr(second_letter)
    third_letter = letter_code + 3 
    third_letter_char = chr(third_letter)

    print(letter)
    print(first_letter_char)
    print(second_letter_char)
    print(third_letter_char)

#This function calls convert_height and then calla before with the parameter of the string a
def main():
    convert_height()
    before("h")

#This is where the code runs
main()