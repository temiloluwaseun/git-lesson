number1= int(input("Enter a number"))
number2= int(input("Enter another number"))

def add():
    return number1+number2

def divide():
    return number1/number2

def multiply(num1, num2):
    return num1 * num2

print(add())
print(divide())

x= add()
y= divide()

print(multiply(x, y))