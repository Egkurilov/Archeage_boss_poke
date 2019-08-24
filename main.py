from datetime import datetime
from time import sleep

# список рейдовых дней
raid_days = {
    'Monday': {'21:21': {'Летучий дельфиец'}},
    'Tuesday': {'21:07': {'Кракен'}, '21:21': {'Летучий дельфиец'}},
    'Wednesday': {'17:21': {'Летучий дельфиец'}},
    'Thursday': {'17:07': {'Кракен'}, '17:21': {'Летучий дельфиец'}},
    'Friday': {'19:21': {'Летучий дельфиец '}},
    'Saturday': {'16:56': {'Кракен'}, '19:21': {'Летучий дельфиец'}},
    'Sunday': {'19:21': {'Летучий дельфиец'}}}


# получаем день недели
def get_day_of_weak():
    now_dow = datetime.now().strftime("%A")
    return now_dow


# получаем текущее время
def get_time_now():
    now_time = datetime.now().strftime("%H:%M")
    return now_time


# удаленный ивент  todo
def ts_event(timer):
    print("время очередного события", timer)


while True:
    # проверяем день в списке рейдовых дней
    if get_day_of_weak() in raid_days:
        # принт для дебага
        print("DEBUG ", get_day_of_weak(), raid_days[get_day_of_weak()])
        # считываем список в строку для проверки
        for time in raid_days[get_day_of_weak()]:
            # сравниваем текущее время и время рейдов
            if get_time_now() == time:
                # вызов удаленного ивента todo
                ts_event(time)
                # выход из if
                break
            else:
                # для Дебага логирования
                print("Время еще не пришло, cейчас: ", get_time_now())
                # вывод сегодняшнего события
                print("Сегодня", '\n'.join(raid_days[get_day_of_weak()][time]))
    # время проверки
    sleep(60)
