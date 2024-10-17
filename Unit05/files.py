import plotter

def word_search(filename):
    word = input("Enter a word: ")
    word = word.lower()
    file = open(filename)
    for line in file:
        line = line.strip()
        line = line.lower()
        if line == word:
            print("Found the word:",word)
            return
    
    print("Did not find the word")
    file.close()

def longest_word(filename):
    file = open(filename)
    for line in file:
        words = line.split()
        if len(words) == 0:
            continue
        longest_word = words[0]
        longest_length = len(longest_word)

        for index in range(1, len(words)):
            word = words[index]
            length = len(word)
            if length > longest_length:
                longest_length = length
                longest_word = word
            print("longest word:", longest_word)
        

    file.close()

def print_names(filename):
    file = open(filename)
    next(file) #how to skip a line
    for line in file:
        feilds = line.split(",")
        first = feilds[1]
        last = feilds[0]
        print(first, last)


def class_average(filename, column):
    with open(filename) as file:
        total = 0
        count = 0
        header = next(file)
        lables = header.split(",")
        lable= lables[column]
        for line in file:
            feilds = line.split(",")
            lab = feilds[column]
            lab = float(lab)

            total += lab
            count += lab

        print("Class average:", (total/count))

def polt_grades(csv_file, column):
    with open(csv_file) as file:
        plotter.init("Grades", "Numbers", "Score")
        header = next(file)
        lables = header.split(",")
        name = lables[column]
        plotter.new_series(name)

        for record in file:
            fields = record.split(",")
            grade = float(fields[column])
            plotter.add_data_point(grade)



        
def main():
    polt_grades("data/grades_363.csv", 8)
    """
    print(word_search("data/words.txt"))
    longest_word("data/alice.txt")
    print_names("data/grades_010.csv")
    class_average("data/grades_010.csv", 8)
    """

main()

# with-as 
#with open("a_file.txt") as a_file: will make sure the file is closed 
