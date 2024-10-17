"""Dessa Shapiro"""
#This program creates a big wheel game
import array_utils
import random
import arrays

#this function creates any array with values from 5-100 in steps of 5
def create_big_wheel():
    an_array = array_utils.range_array(5, 105, 5)
    return an_array

#This function prints the values in the array gotten from create_big_wheel func
def print_big_wheel_values(big_wheel_array):
    print("Big wheel values:")
    for index in range(len(big_wheel_array)):
        print(big_wheel_array[index], end = ", ")

#This function outputs a random value in an array with the length of 20
def spin_wheel(big_wheel_array):
    index = random.randint(0, 19)
    return big_wheel_array[index]

#This function runs a round using the big)wheel_array, and compares it to the threshold 
def run_round(big_wheel_array, spin_threshold):
    spin = spin_wheel(big_wheel_array)
    if spin >= spin_threshold:
        return spin
    else:
        return spin + spin_wheel(big_wheel_array)

#This function prints the numbers indavidually from the results array
def print_results(results_array, index=0):
    if index > len(results_array)-1:
        return None
    elif len(results_array) == 1:
        print(results_array[index])
    else:
        print(results_array[index])
        print_results(results_array, index+1)

#this function returns the sum of all the numbers in the results array
def results_sum(results_array, index=0):
    if index > len(results_array)-1:
        return 0
    elif len(results_array) == 1:
        return results_array[index]
    else:
        sum = results_sum(results_array, index+1)
        return results_array[index] + results_sum(results_array, index+1)
        #sum = int(results_array[index])
        #return sum + results_sum(results_array, index+1)

#this function determines how many values in the results array are euqal to or greater than 100 
def how_many_rounds(results_array, index=0, value=0):
    if index == len(results_array):
        return value

    score = results_array[index]
    if score <= 100:
        value += 1
    return how_many_rounds(results_array, index+1, value)

#This function finds the average of all the results 
def find_average(results_array):
    length = len(results_array)
    sum = results_sum(results_array)
    return sum/length


#this function calls the wheel game, having the user input values and it output the results of the game
def main():
    big_wheel_array = create_big_wheel()
    print_big_wheel_values(big_wheel_array)
    spin_threshold = int(input("\nEnter a threshhold to see if you can spin again (between 5 and 100): "))
    num_of_rounds = int(input("Enter the number of rounds you would like to play (between 1 and 100): "))
    results_array = arrays.Array(num_of_rounds)
    #print(spin_wheel(big_wheel_array))
    for index in range(num_of_rounds):
        results_array[index] = run_round(big_wheel_array, spin_threshold)
    #print(results_array)
    print("Results from",num_of_rounds, "rounds:")
    print_results(results_array)
    print("Sum:",results_sum(results_array))
    print("Rounds less than or equal to $100:",how_many_rounds(results_array))
    print("Average:", find_average(results_array))

#program runs here
if __name__ == "__main__":
    main()