def bday_message():
    name = input("What is your name?: ")
    birth_month=input("What month were you born in?: ")
    birth_day=input("What day on the month were you born?(1-31): ")
    birth_year=input("What year were you born?: ")
    print(name,", your birthday is on, ",birth_month," " ,birth_day,", " ,birth_year,"!", sep="")

bday_message()
bday_message()
bday_message()