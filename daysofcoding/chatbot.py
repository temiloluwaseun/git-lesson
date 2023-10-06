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
input("")