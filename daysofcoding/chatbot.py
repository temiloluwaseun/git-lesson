import time
import datetime
import random
alarm_time = "05:00:00"
current_time = time.strftime("%H:%M:%S")
if current_time==alarm_time:
    u=["wake up", "time to wake", "time to start the day"]
    print(random.choice(u))
current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("Today is %A, %Y-%m-%d, the time is %H:%M:%S") 
print(formatted_datetime)
workout_time = "06:00:00"
current_time = time.strftime("%H:%M:%S")
if current_time==workout_time:
    v=["workout!!!", "time to workout", "time to hit the gym"]
    print(random.choice(v))
breakfast_time = "07:00:00"
current_time = time.strftime("%H:%M:%S")
if current_time==breakfast_time:
    w=["breakfast!!!", "time to eat", "time to have your breakfast"]
    print(random.choice(w))
work_time = "08:00:00"
current_time = time.strftime("%H:%M:%S")
if current_time==work_time:
    x=["go to work", "time for work", "time to to work"]
    print(random.choice(x))
al=input("Do you want to set another alarm? ")
if al=="yes":
    aln=input("What is the alarm name? ")
    alt=input("whattime do you want (format in H:M)")
    current_time = time.strftime("%H:%M")
    if current_time == alt:
        print(aln)
ework_time = "12:23"
current_time = time.strftime("%H:%M")
if current_time==ework_time:
    wd=input("Are you done for the day? ")
    if wd=="no":
        wdn=input("when will you be done?(format in H:M) ")
        current_time = time.strftime("%H:%M")
    if wd=="yes" or current_time == wdn:
        md=input("how was your day?(good or bad)")
        if md=="good":
            mdg=input("that's nice what happened? ")
            mdgl=["cool", "that's nice", "that's cool", "glad you had a great day"]
            print(random.choice(mdgl))
        if md=="bad":
            mdb=input("What happened? (1=stress,2=emotional breakdown,3=sickness,4=other)")
            if mdb=="1":
                print("Try to get some rest")
            if mdb=="2":
                mdbii=["you'll be fine","you'll get through it","you are the best","you rock"]
                print(random.choice(mdbii))
            if mdb=="3":
                mdbiii=input("Have you gone to the hospital? ")
                if mdbiii=="yes":
                    print("follow the doctors advice and ensure you take care of yourself")
                if mdbiii=="no":
                    mdbiiip=input("Have you gone to the pharmacy? ")
                    if mdbiiip=="yes":
                        print("use your medications properly and get rest")
                    if mdbiiip=="no":
                        mdbiiipi=input("are you currently receiving any form of treatment? ")
                        if mdbiiipi=="yes":
                            print("ensure you take care of yourself")
                        else:
                            print("please get treatment")
            if mdb=="4":
                input("what happened? ")
                print("sorry, you'll be fine")