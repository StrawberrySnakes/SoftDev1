"""Dessa Shapiro"""
#this code makes plots/graphs of grade data gotten from csv files
import csv
import plotter
import re

def plot_grades(filename, first_name, last_name):
#this function plots the grade of a single student given their first and last names
    with open(filename) as file:
        plotter.init(first_name+" "+last_name, "Grade Item", "Score")
        plotter.new_series("Grades")
        reader = csv.reader(file)
        next(reader)
        for record in reader:
            if re.findall(first_name, record[0]) and re.findall(last_name, record[0]):
                index = 3
                while index >= 3 and index <= 29:
                    grade = float(record[index])
                    plotter.add_data_point(grade)
                    index += 1
                plotter.plot()
            else:
                continue

def get_average(filename, column):
#This function gets the average of a column of grades from a list of students and grades in a csv
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        total = 0
        count = 0
        for record in reader:
            grade = record[column]
            try:
                grade_new = float(grade)
                total += grade_new
                count += 1
            except:
                count+=1
    
        return total/count
    
def plot_class_averages(filename):
#this function plots all the class average grades using get_avaerage function
        plotter.init("Class Averages "+filename, "Grade Item", "Score")
        plotter.new_series("Class Average")
        column = 3
        while column >=3 and column <=29:
            average = get_average(filename, column)
            plotter.add_data_point(average)
            column += 1
        plotter.plot()



def main():
#calls functions to make plots
    plot_grades("data/full_grades_100.csv", "Odyssey", "Naegeli")
    plot_grades("data/full_grades_100.csv", "Estrella", "Giulian")
    plot_class_averages("data/full_grades_999.csv")

#code runs here
if __name__ == "__main__":
    main()
