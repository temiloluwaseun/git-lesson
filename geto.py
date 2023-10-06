import random
q=random.randint(1,101)
v=int(input("Guess a number from 1-100: "))
if v<q:
    print("Your entry is lower than the number")
if v>q:
    print("Your entry is higher than the number")
if v==q:
    print("you guessed right GENIUS!")


fruits=["apple","banana","orange"]
user=input("Pick a fruit(quite common fruit): ")

if user in fruits:
    print("You guessed correctly")
else:
    print("Sorry, Try again")