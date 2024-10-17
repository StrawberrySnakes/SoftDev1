VAR_A = ord("A")

def convert_to_ascii(character):
    #character = input("Enter a single character: ")
    code = ord(character)
    print(code)

def convert_from_ascii(code):
    #code = int(input("Enter a ascii code: "))
    char2 = chr(code)
    print(code," = ",char2)

def alphabet_position(letter):
    code = ord(letter)
    position = code - VAR_A + 1
    print(letter," is in position",position,"of the alphabet.")


def main():
    convert_to_ascii("g")
    convert_to_ascii("%")
    convert_to_ascii("l")
    convert_from_ascii(101)
    convert_from_ascii(121)
    convert_from_ascii(40)
    alphabet_position("D")
    alphabet_position("M")
    alphabet_position("L")

main()
