class Bicycle:
    __slots__ = ["__color", "__gears"]
    def __init__(self, color, gears):
        self.__color = color
        self.__gears = gears
    def ride(self, name):
        print(name, "rides the", self.__color, "bike with", self.__gears, "gears!")

    def get_color(self): #accessors, "getters"
        return self.__color
    
    def get_gears(self):
        return self.__gears
    
    def set_color(self, color): #Mutators, "setters"
        self.__color = color


def main():
    bike = Bicycle("Red", 21)
    bike.ride("Todd")
    print(bike.get_color(), bike.get_gears())
    bike.set_color("Blue")
    bike.ride("TODDDD")

    other = Bicycle("Multi-Colored", 14)
    other.ride("Toddd")

if __name__ == "__main__":
    main()
