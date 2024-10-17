ASCII_0 = 48

def cast_to_int_loop(a_string):
    index = 0
    int_value = 0
    while index < len(a_string):
        char = a_string[index]
        ascii_value = ord(char)
        digit = ascii_value - ASCII_0
        int_value = int_value * 10 + digit

        index += 1
    return int_value

def cast_to_int_rec(a_string, index=0, int_value=0):
    if index >= len(a_string):
        return int_value
    else:
        char = a_string[index]
        ascii_value = ord(char)
        digit = ascii_value - ASCII_0
        int_value = int_value*10 + digit

        return cast_to_int_rec(a_string, index +1, int_value)




def main():
    x = cast_to_int_rec("1543")
    print(x)

main()


