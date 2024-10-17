import random
def secret_number():
    return random.randint(1, 100)

def check_guess(secret, guess):
    if secret < guess:
        return "Too High"
    if secret > guess:
        return "Too Low"
    if secret == guess:
        return "Correct"
    
def prompt_for_guess(secret):
    guess = input("Enter guess:")
    guess = int(guess)
    return check_guess(secret, guess)