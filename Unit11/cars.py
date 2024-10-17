class Car:
    __slots__ = ["__vin", "__make", "__model", "__year", "__mileage", "__fuel"]
    def __init__(self, vin, make, model, year, mileage=0, fuel=0):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel = fuel

    def get_vin(self):
        return self.__vin
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_mileage(self):
        return self.__mileage
    
    def get_fuel(self):
        return self.__fuel
    
    def filler_up(self, gallons):
        self.__fuel += gallons
        if self.__fuel > 15:
            self.__fuel = 15
            
    
    def drive(self, distance):
        max = self.__fuel * 30
        if max <= distance:
            self.__mileage += distance
            self.__fuel -= distance/30
        else:
            self.__mileage += max
            self.__fuel = 0
    
    def __repr__(self):
        return "Car: "\
        + "\n VIN: " + self.__vin\
        + "\n Make: " + self.__make\
        + "\n Model: " + self.__model\
        + "\n Year: " + self.__year\
        + "\n Mileage: " + str(self.__mileage)\
        + "\n Fuel: " + str(self.__fuel)\
    
    def __str__(self):
        return self.__vin + " " + self.__make + " " + self.__model
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__vin == other.__vin
        else: 
            return False

    def __lt__(self, other):
        if type(self) == type(other):
            return self.__vin < other.__vin
        else: 
            return False
    
    def __hash__(self):
        return hash(self.__vin)
        
    
        

def print_car(car):
    #print(car.get_vin(), car.get_make(), car.get_model(), car.get_year(), car.get_mileage(), car.get_fuel())
    print(car)


def main():
    car1 = Car("ABCDE12345","Suberu", "Forester", "2017", 90200)
    car2 = Car("ABCDE12345","Suberu", "Forester", "2017", 90200)
    car3 = Car("JFHIWJ1263","chevy", "Malabu", "2010", 20400)

    print(car1, "==", car2, (car1 == car2))
    print(car1, "is", car2, (car1 is car2))
    print(car1, "is", car3, (car1 is car3))

    lst = [car1, car2, car3]
    lst = sorted(lst)
    print(lst)

    s = set(lst)
    print(s)

    
    #car2 = Car()
    # print_car(car1)
    # car1.filler_up(20)
    # print_car(car1)
    # car1.drive(50)
    # print_car(repr(car1))


if __name__ == "__main__":
    main()