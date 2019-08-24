from datetime import datetime
from time import sleep

# список рейдовых дней
raid_days = {
    'Monday': '21:21',
    'Tuesday': ['21:07', '21:14', '21:21'],
    'Wednesday': '17:21',
    'Thursday': ['17:07', '17:14', '17:21'],
    'Friday': '19:21',
    'Saturday': ['19:07', '19:14', '19:21'],
    'Sunday': '19:21'}


# получаем день недели
def get_day_of_weak():
    now_dow = datetime.now().strftime("%A")
    return now_dow


# получаем текущее время
def get_time_now():
    now_time = datetime.now().strftime("%H:%M")
    return now_time


# удаленный ивент  todo
def ts_event(time):
    print(time)


while True:
    # проверяем день в списке рейдовых дней
    if get_day_of_weak() in raid_days:
        # принт для дебага
        print(get_day_of_weak(), raid_days[get_day_of_weak()])
        # считываем список в строку для проверки
        for time in raid_days[get_day_of_weak()]:
            # сравниваем текущее время и время рейдов
            if get_time_now == time:
                print(ts_event(get_time_now), "время очередного события")
            else:
                print("Время еще не пришло. Сейчас: ", get_time_now())
    # время проверки
    sleep(60)
