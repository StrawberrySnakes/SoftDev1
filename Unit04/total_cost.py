#This code asks for user input to claculate the cost of entities 

#uses if statements to caluclate total cost values 
def calculate_total_cost(quantity):
    if quantity >= 1 and quantity <= 9:
        return 50 * quantity
    elif quantity >= 10 and quantity <= 19:
        return 45 * quantity
    elif quantity >= 20 and quantity <= 29:
        return 38 * quantity
    elif quantity>=30:
        return 32 * quantity

#calls caluclate_total_cost while value input is greater than 0
def main():
    while True:
        input_quantity = int(input("Enter a quantity to be purchased: "))
        if input_quantity <= 0:
            print("Goodbye!")
            break
        else:
            print("Total cost:",calculate_total_cost(input_quantity))

#calls the code here
if __name__ == "__main__":
    main()