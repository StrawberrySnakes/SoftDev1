
def make_student(id, name):
    lst = [id, name, 0.0, 0]
    return lst

def add_student(population, id, name):
    student = make_student(id, name)
    population[id] = student
    # for index in range(len(population)):
    #     student = population[index]
    #     if student[0] == id:
    #         population.pop(index)
    #         break
        
    # student = make_student(id, name)
    # population.append(student)
        
def get_student(population, id):
#     for student in population:
#         if student[0] == id:
#             return student
#     return None
    if id in population:
        student = population[id]
        return student
    else:
        return None

def add_credits(population, id, credits):
    student = get_student(population, id)
    if student is not None:
        student[3] += credits

def get_credits(population, id):
    student = get_student(population, id)
    if student is not None:
        return student[3]
    else:
        return None
    
def main():
    population = {}
    add_student(population, "RJS0991", "Todd")
    add_student(population, "GHD8912", "Jeff")
    add_student(population, "DJK4077", "Mary")
    add_student(population, "ALI1299", "Lanna")
    add_student(population, "GHD8912", "LALA")
    #print(stu1, stu2, stu3, stu4)
    print(population)
    print(get_student(population, "GHD8912"))
    print(get_student(population, "KDT0398"))

    # add_credits(population, "ALI1299", 4)
    # print(get_credits(population, "RJS0991"))
    # print(population)
    
if __name__ == "__main__":
    main()
