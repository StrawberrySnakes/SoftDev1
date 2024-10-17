"""
This program says hi to the world and then says hi to you 
"""

def hello_world():
    #this function prints hello world... thats about it
    print("Hello, World!")

def hello_you():
    #this fuctions takes your name from an input and then prints it saying hi 
    name = input("What is your name?: ") # prompts the user
    print("Hello, ",name,"!", sep="")

#The functions are called here
hello_world()
hello_you()