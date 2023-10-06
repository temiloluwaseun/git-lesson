time=int(input("What is the time?"))
if time<=12:
    print(time,"am")
else:
    print(time%12,"pm")