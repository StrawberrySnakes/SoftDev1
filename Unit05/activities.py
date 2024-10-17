def numbers():
    total = 0
    while True:
        filename = input("Enter a filename:")
        if filename == "":
            break
        try:
            sum = 0
            with open(filename) as file:
                for line in file:
                    try:
                        number = int(line)
                        sum += number
                    except ValueError:
                        print("Skipping nun-numeric data:", line)

                print("Sum of numbers:",sum)
                total += sum
        except FileNotFoundError:
            print("Files does not exist:", filename)

            #this treats all error in the same way there could be a different kind of error
    print("The total sum is:", total)

def division():
    attempts = 0
    while True:

        try:
            x = int(input("Enter an integer numerator"))
            y = int(input("Enter an integer denominator"))

            if x == "" or y == "":
                break

            quotient = x/y
            print(x, "/", y, "+", quotient)
        except ValueError as ve:
            attempts += 1
            if attempts < 3:
                print("Non-numeric data entered")
            else:
                raise ve

        except ZeroDivisionError as zde:
            attempts += 1
            if attempts < 3:
                print("cannot divide by 0")
            else:
                raise zde
        except KeyboardInterrupt as ki:
            attempts += 1
            if attempts < 3:
                print("DONT INTURUPT MEEEEE :[")
            else:
                raise ki

def password():
    password = input("Enter a password: ")
    if len(password) < 10 and len(password) > 20:
        raise ValueError("Nope.. must be between 10 and 20 characters")
    pass_com = input("Confirm your password: ")
    if password != pass_com:
        raise ValueError("Passwords must match")
    return password

def exponent(base, power):
    result = 1
    for i in range(power):
        result = base * result

    return result



def main():
    password()
    #division()
    #numbers()

if __name__ == "__main__":
    main()
