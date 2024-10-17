#This code reorganized characters to make them appear in number/lowercase/upercase order

#function determines is a character is uppercase
def is_upper(character):
    char_code = ord(character)
    result = char_code >= 65 and char_code <=90
    return result

#function determines if a character is lowercase
def is_lower(character):
    char_code = ord(character)
    result = char_code >= 97 and char_code <=122
    return result

#function determines if a character is a digit 0-9
def is_digit(character):
    char_code = ord(character)
    result = char_code >= 48 and char_code <=57
    return result

#reorganizes an input string and changes the order using conditionals 
def group_characters(string):
    string = str(string)
    new_string_num = ""
    new_string_lower = ""
    new_string_upper = ""
    index = 0
    while index < len(string):
        if is_upper(string[index]) == True:
            new_string_upper += string[index]
            index+=1
        elif is_lower(string[index]) == True:
            new_string_lower += string[index]
            index+=1
        elif is_digit(string[index]) == True:
            new_string_num += string[index]
            index+=1
    new_string = new_string_num + new_string_lower + new_string_upper
    return new_string

#creates while loop where group_charaters is called in a valid string is input
def main():
    while True:
        unordered_string = input("Enter a string consisting of letters and digits: ")
        if len(unordered_string) <= 0:
            print("Goodbye!")
            break
        else:
            print(group_characters(unordered_string))
        
#The code runs here
if __name__ == "__main__":
    main()

    