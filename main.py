from datetime import datetime
from time import sleep

raid_days = {
    'Monday': '21:21',
    'Tuesday': ['21:07', '21:14', '21:21'],
    'Wednesday': '17:21',
    'Thursday': ['17:07', '17:14', '17:21'],
    'Friday': '19:21',
    'Saturday': ['19:07', '19:14', '19:21'],
    'Sunday': '19:21'}


def get_day_of_weak():
    now_dow = datetime.now().strftime("%A")
    return now_dow


def get_event_time():
    now_time = datetime.now().strftime("%H:%M")
    return now_time


while True:
    if get_day_of_weak() in raid_days:
        print(get_day_of_weak(), raid_days[get_day_of_weak()])

    sleep(60)
