"""Dessa Shapiro"""
class Pet:
    __slots__ = ["__species", "__name", "__weight", "__age", "__fur_color"]
    def __init__(self, species, name, weight, fur_color, age=0):
        self.__species = species
        self.__name = name
        self.__weight = weight
        self.__fur_color = fur_color
        self.__age = age

    def get_species(self):
        return self.__species
    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_fur_color(self):
        return self.__fur_color
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name
    

    def feed(self, calories):
        pounds = calories / 3000
        self.__weight += pounds

    def walk(self, distance):
        pounds = distance * 100 / 3000
        self.__weight -= pounds

def main():
    cat = Pet("Cat", "Fluffy", 6, "Black", 2)
    print(cat.get_name(), cat.get_weight())

    cat.feed(1800)
    print(cat.get_name(), cat.get_weight())

    cat.set_name("kmflkfmlenfle")

    cat.walk(1.2)
    print(cat.get_name(), cat.get_weight())

    


if __name__ == "__main__":
    main()

