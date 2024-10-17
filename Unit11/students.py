"""
A Student class.

@author GCCIS Faculty
"""

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa", "__courses"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0
        self.__courses = []

    def get_id(self):
        return self.__id 
    
    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits

    def get_gpa(self):
        return self.__gpa
    
    def set_name(self, name):
        self.__name = name

    def add_course(self, course):
        self.__courses.append(course)

class Course:
    __slots__ = ["__name", "__credits", "__grade"]
    def __init__(self, name, credits, grade):
        self.__name = name
        self.__credits = credits
        self.__grade = grade

    def get_name(self):
        return self.__name
    
    def get_credits(self):
        return self.__credits
    
    def get_grade(self):
        return self.__grade

    def compute_points(self):
        quality = QUALITY_POINTS[self.__grade]
        return self.__credits * quality
    
    def get_gpa(self):
        total_points = 0
        total_cedits = 0
        for courses in self.__corses:
            total_points += courses.compute_points()
            total_cedits += courses.get_credits()
        if total_cedits != 0:
            return total_points / total_cedits
        return

def print_student(student):
    """
    Prints a student's info to standard output.
    """
    print("Student: ID=", student.id, ", name=", student.name, 
        ", credits=", student.credits, ", GPA=", student.gpa, sep="")
    
def main():
    dessa = Student("DJS9826", "Dessa", "17", "3.7")
    print(dessa.get_id(), dessa.get_name(), dessa.get_credits(), dessa.get_gpa())

    course = Course("GCIS-123", 4, "C+")
    print(course.get_name(), course.get_credits())

    dessa.add_course(course)
    dessa.add_course(Course("IST-140", 3, "A"))
    dessa.add_course(Course("MAT-190", 3, "B"))

    print(dessa.get_gpa())
