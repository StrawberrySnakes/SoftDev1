#this program creates a random passowrd based on user inputs
import random

#returnes the ascii characters from a numerical range
def create_ascii_range_string(start, stop):
    string = ""
    start = int(start)
    stop = int(stop)
    for index in range(start, stop):
        string += chr(start)
        start += 1
    return string
    
#returns one upercase letter
def create_uppercase_letters_sting():
    return create_ascii_range_string(65, 91)

#returns one lowercase letter
def create_lowercase_letters_sting():
    return create_ascii_range_string(97, 123)

#returns one digit 1-9
def create_digits_sting():
    return create_ascii_range_string(48, 58)

#returns one symbol
def create_symbols_string():
    return create_ascii_range_string(33, 48) + create_ascii_range_string(58, 65) + create_ascii_range_string(91, 97) + create_ascii_range_string(123, 127)

#functions picks one character for a random string 
def get_random_char_from_string(string):
    string_len = len(string)
    x = random.randint(0, string_len-1)
    return string[x]

#Creates a random password using all previous functions to get a singe character from different categories 
def generate_random_password(num_upper, num_lower, num_digits, num_symbols):
    total_len = int(num_upper + num_lower + num_digits + num_symbols)
    password = ""
    while total_len > len(password):
        x = random.randint(1, 4)
        if x == 1 and num_upper > 0:
            password += get_random_char_from_string(create_uppercase_letters_sting())
            num_upper -= 1
        elif x == 2 and num_lower > 0:
            password += get_random_char_from_string(create_lowercase_letters_sting())
            num_lower -= 1
        elif x == 3 and num_digits > 0:
            password += get_random_char_from_string(create_digits_sting())
            num_digits -= 1
        elif x == 4 and num_symbols > 0:
            password += get_random_char_from_string(create_symbols_string())
            num_symbols -= 1
        else:
            pass
    return password

#main function with a loop to create random password using inputs and exiting when entering empty string
def main():
    while True:
        inputs = (input("enter <num uppers> <num lowers> <num digits> <num symbols>(with spaces): "))
        values = inputs.split()
        if inputs == "":
            break
        elif len(values) == 4:
            var1 = int(values[0])
            var2 = int(values[1])
            var3 = int(values[2])
            var4 = int(values[3])
            print("Password", generate_random_password(var1, var2, var3, var4))
        else:
            print("Must enter exactaly 4 values")
            pass

# Code is called here
if __name__ == "__main__":
    main()

