COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RESET = "\u001b[0m"
WHITE = "\u001b[38;5;7m"
LIGHT_GREEN = "\u001b[38;5;10m"
BLUE = "\u001b[38;5;26m"
ORANGE = "\u001b[38;5;130m"
GREEN = "\u001b[38;5;28m"
RED = "\u001b[38;5;9m"
YELLOW = "\u001b[38;5;11m"

RARITY_STRINGS = {
    COMMON : WHITE + "C", 
    UNCOMMON : LIGHT_GREEN + "U", 
    RARE : BLUE + "R", 
    LEGENDARY : ORANGE + "L"}

class Card:
    __slots__ = ["__name", "__resourse_cost", "__rarity", "__faction", "__attack_power", "__health"]
    def __init__(self, name, resourse_cost, rarity, faction, attack_power, health):
        self.__name = name
        self.__resourse_cost = resourse_cost
        self.__rarity = rarity
        self.__faction = faction
        self.__attack_power = attack_power
        self.__health = health

    def get_name(self):
        return self.__name
    
    def get_resourse_cost(self):
        return self.__resourse_cost
    
    def get_rarity(self):
        return self.__rarity
    
    def get_faction(self):
        return self.__faction
    
    def get_attack_power(self):
        return self.__attack_power
    
    def get_health(self):
        return self.__health
    
    def __repr__(self):
        return  "\nName" + self.__name\
                + "\nResourse Cost" + str(self.__resourse_cost)\
                + "\nRarity" + str(self.__rarity)\
                + "\nFaction" + str(self.__faction)\
                + "\nAttack Power" + str(self.__attack_power)\
                + "\nHealth" + str(self.__health)
    
    def __str__(self):
        return "[" + "c" + self.__name[0] \
        + " " + "{:02d}".format(self.__resourse_cost)\
        + " " + "{:02d}".format(self.__attack_power)\
        + " " + "{:02d}".format(self.__health)\
        + "]"
    
    def damage(self, amount):
        if amount > self.__health:
            excess = amount = self.__health
            self.__health = 0
            return excess
        else:
            self.__health -= amount
            return 0
    
    def is_conscious(self):
        if self.__health > 0:
            return True
        return False
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__resourse_cost == other.__resourse_cost \
                and self.__faction == other.__faction \
                and self.__rarity == other.__rarity \
                and self.__attack_power == other.__attack_power
        else: 
            return False
        
    def __lt__(self, other):
        if type(self) == type(other):
            if self.__resourse_cost != other.__resourse_cost:
                return self.__resourse_cost < other.__resourse_cost
            else:
                self.__name < other.__name
        else:
            return False


        
    

def main():
    card1 = Card("Trollzord", 2, "Trolls", UNCOMMON, 3, 5)
    card1 = Card("Troll Peasent", 3, "Trolls", COMMON, 2, 3)
    # print(card1.get_health())
    # print(card1.get_rarity())
    # print(card1)
    # s = repr(card1)
    # print(s)
    print(card1)
    card1.damage(3)
    print(card1, card1.is_conscious())


if __name__ == "__main__":
    main()

    