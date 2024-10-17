#This code uses two random integers between -100 and 100 inclusive and finds the absolute difference between the two 
import random
#global variables
MAX = 100
MIN = -100

#This function finds the aboslute difference between two parameters and returnes the result
def absolute_difference(a, b):
    diff = int(a -b)
    if diff < 0:
        abs_diff = diff*-1
        return abs_diff
    return diff

#sets values for a and b and calls absolute difference function 
def main():
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    print("a=",a,", b=",b, ", absolute differnece = ",absolute_difference(a, b), sep="" )
    
#So the tests dont run in main
if __name__ == "__main__":
    main()

    

    