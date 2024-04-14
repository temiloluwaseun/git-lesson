import random
x=input("Welcome! Are you ready to roll the dice?")
if x.capitalize()=="Yes":
    print(random.randint(1,6))