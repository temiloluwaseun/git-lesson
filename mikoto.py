calc = input("enter your calculation ")

splitted = calc.split(' ')
x=int(splitted[0])
y=int(splitted[2])
def add(num1, num2):
    return num1 + num2
#    print(ola)
def subtract(num1, num2):
    return num1 - num2
#    print(x)
def multiply(num1, num2):
    return num1 * num2
#    print(xx)
def divide(num1, num2):
    return num1 / num2
#    print(xxx)
if splitted[1] == "+":
    print(add(x,y))
if splitted[1] == "-":
    print(subtract(x,y))
if splitted[1] == "*":
    print(multiply(x,y))
if splitted[1] == "/":
    print(divide(x,y))