"""Dessa Shapiro"""
PI = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    index = 0
    score = 0
    for index in range(len(PI)):
        pi_digits = input("Enter the next decimal digit of pi: ")
        if pi_digits == PI[index]:
            score+=1
        else:
            print("Incorrect digit! correct digit =", PI[index])
            break
    return score

def display_score(score):
    if score >= 0 and score <= 4:
        title= "PI Neophyte"
    elif score >= 5 and score <= 9:
        title= "PI Novice"
    elif score >= 10 and score <= 24:
        title= "PI Journeyman"
    elif score >= 25 and score <= 49:
        title= "PI Enthusiast"
    elif score >= 50 and score <= 96:
        title= "PI Connoisseur"
    elif score >= 97 and score <= 100:
        return "PI Expert"
    elif score >= 100:
        title= "PI Imposter"

    print("Your score was", score,"digits. You have the title of:",title)
    
    
def main():
    x = int(pi_tester())
    display_score(x)

main()
    






