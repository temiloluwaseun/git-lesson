'''
x=input("what is your name?")
y=input("do you love don toliver?")
if y=="yes":
    print(x+" is a gee")
else:
    print("come on dawg")
'''                
a=int(input("input the value of a"))
b=int(input("input the value of b"))
c=int(input("input the value of c"))
q=((b*b)-(4*a*c))
import math
v=math.sqrt(q)
s=(-b+v)/(2*a)
t=(-b-v)/(2*a)
print(s)
print(t)