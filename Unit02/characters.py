#This program coverts characters to Ascii and vice versa

#This function converst two characters into their ascii values and adds them
def add_chars(x, y):
    x_code = ord(x)
    y_code = ord(y)
    num_code_sum = x_code + y_code
    sum_char = chr(num_code_sum)
    print(x,"+",y,"=",num_code_sum, end=", ")
    print(num_code_sum,"'s ASCII character = ",sum_char, sep="")

#This function converst two characters into their ascii values and subtracts them
def subtract_chars(x, y):
    x_code = ord(x)
    y_code = ord(y)
    num_code_diff = x_code - y_code
    diff_char = chr(num_code_diff)
    print(x,"-",y,"=",num_code_diff, end=", ")
    print(num_code_diff,"'s ASCII character = ",diff_char, sep="")

#This function askes for a user to input two characters and then calls functions add and subtract
def main():
    num_1 = input("Input a character: ")
    num_2 = input("Input a character: ")
    add_chars(num_1, num_2)
    subtract_chars(num_1, num_2)

#This is where the code runs
main()
"""
1)When I run the code it seems to work and there are no errors or strange characters.
When I look at the ACSII table the math seems to have worked fine and the translations have worked.
After trying some more combinations I found that Some numbers may not be able to translate to a charater beacuse the numbers are not in range for ascii,
 or the such as being negative 

2) When I try to type two characters an error occurs when it tries to execute and says
TypeError: ord() expected a character, but string of length 2 found
Meaning that the ord() operation does not recognize more then one character input 
"""






