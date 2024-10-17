"""Dessa Shapiro"""

#create a superhero class with name, identity, powers and weapons
class Superhero:
    __slots__ = ["hero_name", "identity", "powers", "weapons"]
    def __init__(self, hero_name, identity, powers, weapons):
        self.hero_name = hero_name
        self.identity = identity
        self.powers = powers
        self.weapons = weapons

#creates a team with superheros and leader
class Team:
    __slots__ = ["leader", "superheroes"]
    def __init__(self, leader, superheroes):
        self.leader = leader
        self.superheroes = superheroes

#finda a specific team member 
def find_team_member(team, hero_name):
    for avenger in team.superheroes:
        if avenger.hero_name == hero_name:
            return avenger
    return None

#finds leaders
def find_team_leader(team):
    return team.leader

#prints an invividual advengers name, idtentity, powers and weapons
def print_avenger_bio(avenger):
    print(avenger.hero_name, " (",avenger.identity,") : ", end="")
    print("\nAbilities")
    for power in avenger.powers:
        print(power)
    if avenger.weapons:
        print("Weapons")
        for weapon in avenger.weapons:
            print(weapon)
    print()

#prints out the roster with names
def print_roster(team):
    print("Roster:")
    for avenger in team.superheroes:
        if avenger == team.leader:
            leader_mark = "[Leader]"
        else:
            leader_mark = ""

        print(leader_mark, avenger.hero_name)

#prints out froster with names and info
def print_full_roster_with_bios(team):
    print("Roster with Bios:")
    for avenger in team.superheroes:
        #leader_mark = "[Leader] " if avenger == team.leader else ""
        print_avenger_bio(avenger)

#defines all the superheros and adds them to a team. prints out the team info
def main():
    ironman = Superhero("Iron Man", "Tony Stark", ["Technical genius"], ["Mark VII Armor Suit"])
    captain_america = Superhero("Captain America", "Steve Rogers", ["Super strength", "Super reflexes"], ["Vibranium Shield"])
    thor = Superhero("Thor", "Thor", ["Extreme super strength", "Can control lightning"], ["Mjølnir"])
    hulk = Superhero("Hulk", "Bruce Banner", ["Extreme super strength", "Super healing", "Genius"], [])
    black_widow = Superhero("Black Widow", "Natasha Romanoff", ["Enhanced fighting techniques", "Super reflexes"], ["Widow's Bite Electroshock Bracelets"])
    hawkeye = Superhero("Hawkeye", "Clint Barton", ["Extreme aim"], ["Various Specialized Arrows", "Bow"])

    avengers_team = Team(ironman, [thor, ironman, captain_america, hulk, black_widow, hawkeye])

    print("Found Avenger Bio:")
    print_avenger_bio(thor)

    print("\nLeader Bio:")
    leader = find_team_leader(avengers_team)
    print_avenger_bio(leader)

    print_roster(avengers_team)

    specific_avenger_name = "Thor"
    specific_avenger = find_team_member(avengers_team, specific_avenger_name)
    if specific_avenger:
        print("\nFound",specific_avenger_name,"'s Bio:", end="")
        print_avenger_bio(specific_avenger)

    print_full_roster_with_bios(avengers_team)

#code runs here
if __name__ == "__main__":
    main()


