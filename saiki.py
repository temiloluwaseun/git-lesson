time = int(input("What is the time:   "))
if time <= 12 :
    print(f"{time} am")
else:
    timer = time % 12
    print(f"{timer} pm")