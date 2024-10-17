
# a = MyClass() is a constructor creates instance of class
#for classes use camel case(capitalize begining every word MyClass)
class Student:
    #how to make sure you do not mess up and . notation 
    #slots is a filter and does not guarrentee a value for each of these names
    __slots__ = ["id", "name", "gpa", "credits"]
    def __init__(self, id, name, gpa=0.0, credits=0):
        #can do this self.id = "USY2091" hardcoded
        self.id = id
        self.name = name
        self.gpa = gpa
        self.credits = credits



def print_student(student):
    print("Student:", student.id, student.name, student.gpa, student.credits)

def main():
    student1 = Student("TOD5816", "Todd", 3.5, 18)
    print_student(student1)


    student2 = Student("LOD5816", "Loddy")
    print_student(student2)

if __name__=="__main__":
    main()