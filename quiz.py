
user1=input("What is your name user 1: ")
user2=input("What is your name user 2: ")
score1=0
score2=0
a=input(f"What is the largest ocean in the world {user1}: ")
b=["pacific", "pacific ocean"]
if a in b:
    score1 += 5
    print(f"{user1} is correct")
else:
    score1 +=0
    print("incorrect")

d=input(f"What is the largest continent in the world {user2}: ")
e="asia"
if d==e:
    score2 += 5
    print(f"{user2} is correct")
else:
    score2 +=0

d=input(f"What is the capital of Nigeria {user1}: ")
e="abuja"
if d==e:
    score1 += 5
    print(f"{user2} is correct")
else:
    score1 +=0

d=input(f"What is the capital of France {user2}: ")
e="paris"
if d==e:
    score2 += 5
    print(f"{user2} is correct")
else:
    score2 +=0

print(f"{user1} has {score1} points")
print(f"{user2} has {score2} points")

'''
x=input("write a word: ")
w=x[::-1]
if x==w:
    print("The word is a palindrome")




ab=input("enter your numbers (seperate by comma)")
xyz={
"1":"a",
"2":"b",
"3":"c",
"4":"d",
"5":"e",
"6":"f",
"7":"g",
"8":"h",
"9":"i",
"10":"j",
"11":"k",
"12":"l",
"13":"m",
"14":"n",
"15":"o",
"16":"p",
"17":"q",
"18":"r",
"19":"s",
"20":"t",
"21":"u",
"22":"v",
"23":"w",
"24":"x",
"25":"y",
"26":"z",
}





wxy=""
for i in ab:
    if i in xyz:
        wxy += xyz[i]
print(wxy)
#print(literal[26])
'''


while True:
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == '1':
            result = (temperature * 9/5) + 32
            print(f"{temperature} Celsius is equal to {result} Fahrenheit.")
        elif choice == '2':
            result = (temperature - 32) * 5/9
            print(f"{temperature} Fahrenheit is equal to {result} Celsius.")
        elif choice == '3':
            result = temperature + 273.15
            print(f"{temperature} Celsius is equal to {result} Kelvin.")
        elif choice == '4':
            result = temperature - 273.15
            print(f"{temperature} Kelvin is equal to {result} Celsius.")
        elif choice == '5':
            result = (temperature - 32) * 5/9 + 273.15
            print(f"{temperature} Fahrenheit is equal to {result} Kelvin.")
        elif choice == '6':
            result = (temperature + 459.67) * 5/9
            print(f"{temperature} Kelvin is equal to {result} Fahrenheit.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7).")

