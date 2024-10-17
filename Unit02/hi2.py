#This code is a mad lib which uses lists and inputs to creates a self-made story.. kinda
import random
import os

#This is where all the list and word values are stored
adj_list = []
noun_list=[]
verb_list=[]
animal_list=[]
name_list=[]
number = [56,10,30,6,0.453,571,760,0,]

#this function asks for user inputs 
def ask_for_words():
    for i in range(1):
        name_input=input("Type a name: ")
        name_list.append(name_input)
    for i in range(3):
        adj_input =input("Type an adjective: ")
        adj_list.append(adj_input)
    for i in range(3):
        noun_input=input("Type a noun: ")
        noun_list.append(noun_input)
    for i in range(2):
        verb_input=input("Type a verb: ")
        verb_list.append(verb_input)
    for i in range(3):
        animal_input=input("Type an animal: ")
        animal_list.append(animal_input)

#This is the story 
def story_time():
    print("You are on a trip to the ",random.choice(number)," year old local zoo with your best friend, ",name_list[0], sep="", end="",)
    print(". You and ",name_list[0]," decide to ",verb_list[0]," to see the ",animal_list[0],"s, you are shocked to see a that the ",animal_list[0],"s have ",adj_list[0]," ",noun_list[0],"s on their heads.",sep="", end="",)
    print("You are so startled that you trip over a ",noun_list[1], sep="", end="",)
    print(".You are on the ground as you notice a big shadow hovering over you, its in the shape of a ",animal_list[1],". It must have escaped it's cage!",sep="",)
    print(" ")
    print("You look around and all the ",adj_list[1]," animals are free as they ",verb_list[1]," around the zoo. You notice your friend has fallen into the ",adj_list[2]," ",animal_list[2],"s cage.",sep="")
    print("You grab your friend and run away as fast a you can. The last thing you see before it all goes dark is a big ",noun_list[2]," coming straight at you." ,sep="", )

#Allows the user to choose to play again 
def play_again():
    play_game = input("Do you want to play mad libs again?(y/n): ")
    if play_game == "y" or "Y":
        adj_list.clear()
        noun_list.clear()
        verb_list.clear()
        animal_list.clear()
        name_list.clear()
        ask_for_words()
        story_time()
    elif play_game == "n" or "N":
        os.system("clear")
        print("Thank you for playing!")

#everything runs here
ask_for_words()
story_time()
play_again()