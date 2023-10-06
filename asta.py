'''
import string
import random

v=string.ascii_letters + string.digits + string.punctuation

lenght=int(input("Preferred password lenght: "))

password="".join(random.choices(v,k=lenght))
print(password)


to_do_list=["wake up", "drink water", "exercise"]
print(
    "1=add task to list "
    "2=print the first task "
    "3=quit"
)
tdl=int(input("Enter a shortcut: "))
if tdl==1:
    add=input("add a task: ")
    to_do_list.append(add)
    print(to_do_list)
if tdl==2:
    print(to_do_list[0])
if tdl==3:
    print(to_do_list)


print(
    "1=Addition "
    "2=Subtraction  "
    "3=Division "
    "4=Multiplication   "
)
user=int(input("Enter a code: "))
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

if user==1:
    print(a+b)
if user==2:
    print(a-b)
if user==3:
    print(a/b)
if user==4:
    print(a*b)


print("                                          Currency Converter")
n=int(input("input the amount of money in naira: "))
curr=input("To convert to dollar press $, To convert to pounds press £:  ")
if curr=="$":
    x=n/770.51
    print("#",n," is equivalent to $ ",x)
if curr=="£":
    y=n/959.42
    print("#",n," is equivalent to £ ",y)


import time 
alarm=input("Enter the time you want to wake up: ")
ctime=time.strftime("%H:%M")
if ctime==alarm:
    print("Wake up!")
'''

'''
foods={
    "sausage roll":200
    "meat pie": 400
    "sharwama": 1500
}

s=200
m=400
sh=1500
food=input("what do you want to buy? (sausage, meatpie or sharwama and all to buy all)")
if food=="sausage":
    print("your bill is ",s)
if food=="meatpie":
    print("your bill is ",m)
if food=="sharwama":
    print("your bill is ",sh)
if food=="sausage and meatpie":
    print("your bill is ",s+m)
if food=="sausage and sharwama":
    print("your bill is ",s+sh)
if food=="meatpie and sharwama":
    print("your bill is ",m+sh)
if food=="all":
    print("your bill is ",m+s+sh)



p=int(input("enter a number: "))
q=int(input("enter a second number: "))
def add():
    return p+q
def subtract():
    return p-q
print(add())
print(subtract())


r=input("Enter your number: ")
s=r.split(" ")
g=int(r[0])
j=int(r[1])
print(g + j)
print(g * j)
'''

r=input("Enter your number: ")
s=sum(int(digit) for digit in r)
g=1
for digit in r:
    g *= int(digit)
print(s)
print(g)