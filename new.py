'''
x=int(input("Enter an integer value  "))
if 1<= x <= 100:
    print("OK")
else:
    print("Out of range")

a=100
b=200
c=300
d=400
e=500
def add(a,b,c,d,e):
    sum=a+b+c+d+e;
    return sum;

print(add(a,b,c,d,e))


x=int(input("Enter the value of x: "))
y=(x*x*x)+(x*x)+5
print(y)

a=int(input("Number of books on shelf A: "))
b=int(input("Number of books on shelf B: "))
c=int(input("Number of books on shelf C: "))
x= a+b+c

print("The number of books on shelf A is ",a)
print("The number of books on shelf B is ",b)
print("The number of books on shelf A, B and C is ",x)
'''

acc_no=input("Enter your account number: ")
f_cr_lim=int(input("Enter your former credit limit: "))
acc_bal=int(input("Enter your credit account balance: "))

n_cr_lim=f_cr_lim/2
print("New credit limit: ",n_cr_lim)
p=acc_bal-n_cr_lim
if acc_bal>n_cr_lim:
    print("Credit amount excedeed for account ",acc_no," by",p)