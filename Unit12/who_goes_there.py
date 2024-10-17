import csv
import list_stack
import random

class Task:
    __slots__ = ["__name", "__location"]

    def __init__(self, name, location):
        self.__name = name
        self.__location = location

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def __repr__(self):
        return self.__name + " in " + self.__location

class Crewmate:
    __slots__ = ["__color", "__tasks", "__dead"]

    def __init__(self, color):
        self.__color = color
        self.__tasks = list_stack.Stack()
        self.__dead = False

    def get_dead(self):
        return self.__dead

    def set_dead(self, value):
        self.__dead = value

    def set_location(self, value):
        self.__location = value

    def __str__(self):
        if self.__dead == True:
            return self.__color + " crewmate (" + str(self.__dead) + ")"
        return self.__color + " crewmate"

    def __repr__(self):
        return "Crewmate:\n" + \
               "color: " + self.__color + "\n" + \
               "murdered: " + str(self.__dead) + "\n" + \
               "tasks: " + str(self.__tasks)

    def assign(self, task):
        self.__tasks.push(task)

    def get_task(self):
        return self.__tasks.pop()

class Ship:
    __slots__ = ["__tasks", "__locations", "__crewmates"]

    def __init__(self, tasks):
        self.__tasks = tasks
        self.__locations = set(task.get_location() for task in tasks)
        self.__crewmates = []

    def simulate_journey(self, num_imposters):
        if not (1 <= num_imposters <= 4):
            raise ValueError("Number of imposters must be between 1 and 4 inclusive.")
        
        colors = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White", "Yellow"]
        random.shuffle(colors)
        
        self.__crewmates = [Crewmate(color) for color in colors[:10 - num_imposters]]

        for crewmate in self.__crewmates:
            tasks_assigned = random.sample(self.__tasks, random.randint(3, 6))
            
            for task in tasks_assigned:
                crewmate.assign(task)
        
        cafeteria_location = "Cafeteria"

        for person in self.__crewmates:
            person.set_location(cafeteria_location)
        
        imposters = random.sample(self.__crewmates, num_imposters)
        for imposter in imposters:
            imposter.location = random.choice(list(self.__locations - {cafeteria_location}))

        while not self.all_tasks_completed() and not self.all_crewmates_eliminated():
            for crewmate in self.__crewmates:
                if crewmate.get_dead():
                    continue

                print("\n", crewmate, "takes a turn:")
                current_task = crewmate.get_task()
                print("Task:", current_task)

                if current_task.get_location() in self.__locations:
                    print(crewmate, "moves to", current_task.get_location())

                    # Check for imposters
                    if crewmate in imposters and self.are_at_location(current_task.get_location(), imposters):
                        crewmate.set_dead(True)
                        print(crewmate, "is murdered")
                        print("Remaining tasks for", crewmate, ":", crewmate._Crewmate__tasks)
                        continue
                    else:
                        print("No imposters at the location.")

                    if current_task in crewmate.get_task():
                        crewmate._Crewmate__tasks.remove(current_task)
                        print("Task", current_task, "completed")
                    else:
                        print("Error: Task", current_task, "not assigned to", crewmate)

                    # Check if all tasks are completed for the crewmate
                    if not crewmate.get_task():
                        print("All tasks completed for", crewmate, ". They return to the cafeteria.")
                        crewmate.set_dead(True)  # Crewmate removed from rotation
                    else:
                        print("Remaining tasks for ", crewmate, ":", crewmate.get_task())
                else:
                    print("Error: Invalid location", current_task.get_location(), " for task", current_task, ".")
                    crewmate.set_dead(True)

        print("Journey completed.")

    def print_final_outcome(self):
        print("\nJourney ends\n")

        if self.all_tasks_completed():
            print("All tasks are completed.")
        elif self.all_crewmates_eliminated():
            print("The crew has been wiped out.")

        print("\nFinal Outcome:")
        print("Surviving Crewmates:")
        for crewmate in self.__crewmates:
            if not crewmate.get_dead():
                print(crewmate)

        print("\nMurdered Crewmates:")
        for crewmate in self.__crewmates:
            if crewmate.get_dead():
                print(crewmate)

    def all_crewmates_eliminated(self):
        for crewmate in self.__crewmates:
            if not crewmate.get_dead():
                return False
        return True

    def are_at_location(self, location, imposters):
        count = 0
        for imposter in imposters:
            if imposter.get_location() == location:
                count += 1
        return count > 1

    def all_tasks_completed(self):
        for crewmate in self.__crewmates:
            if crewmate.get_task():
                return False
        return True

def create_tasks(filename):
    tasks = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if exists
        for record in reader:
            if len(record) == 2:
                name, location = record
                task = Task(name, location)
                tasks.append(task)
            else:
                print("Invalid row:", record)
    return tasks

def main():
    tasks = create_tasks("tasks_01.csv")
    ship = Ship(tasks)

    while True:
        try:
            num_imposters = int(input("Enter the number of imposters (1-4): "))
            ship.simulate_journey(num_imposters)
        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
