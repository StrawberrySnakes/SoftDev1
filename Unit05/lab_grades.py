"""Dessa Shapiro"""
#this code finds the average of student lab grades given a csv file 
import math
#this function asks if you wanna quit 
def terminate():
    exit = input("Are you sure you want to quit(y/n): ")
    if exit == "y" or exit == "Y":
        return True
    else:
        return False

#this function finds the student lab average given a line of data
def student_lab_average(line):
        total = 0
        count = 0
        fields = line.split(",")
        index = 0
        while index <= len(fields):
            if index >= 3 and index <= 11:
            #word = fields[index]
            #word = float(word)
                grade = fields[index]
                if grade == "":
                    grade = 0
                grade = float(grade)
                math.trunc(grade)
                total += grade
                count+=1
                index+=1
            elif index < 3 or index > 11:
                index +=1
                pass
        return total/count

#ask the user to input a file name then list names of all students and their average lab report 
def main():
    total = 0
    count = 0
    while True:
        try:
            filename = input("Enter a filename or 'quit': ")
            if filename == "quit":
                leave = terminate()
                if leave == True:
                    print("Goodbye!")
                    break
                else:
                    continue
            elif filename == "":
                print("User input ENTER")
                pass
            else:
                with open(filename) as file:
                    high_score = 0
                    low_score = 0
                    print("Lab averages from ", filename)
                    header = next(file)
                    lables = header.split(",")
                    print(lables[1], "Lab Average")
                    for line in file:
                        names = line.split(",")
                        name_last = names[0]
                        name_first = names[1]
                        labs = student_lab_average(line)
                        if labs > high_score:
                            high_score = labs
                        if labs < low_score or low_score == 0:
                            low_score = labs
                        print(name_last, name_first," ", labs)
                        total += labs
                        count += 1
                    print("Total lab average: ",total/count)
                    print("Highest Score: ", high_score)
                    print("Lowest Score: ",low_score)


        except FileNotFoundError as fnf:
           print("No such file", filename)


        


        """
        terminate()
        print(student_lab_average("Coldivar, Vikram,491 Cielito Dr, Velma OK, 73491,4,87.1,71.8,58.1,81.1,51.3,79.1,50.0,58.9,63.7,86.0,61.4,100,87.9,42.5,68.3,80.9,93.3,70.1,77.7,75.8,53.6,54.3,75.6,54.6,70.7,54.1,36.1"))
        """
if __name__ == "__main__":
    main()
