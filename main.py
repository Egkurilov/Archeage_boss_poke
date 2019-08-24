from datetime import datetime
from time import sleep

import config
import tsping


# получаем день недели
def get_day_of_weak():
    return datetime.now().strftime("%A")


# получаем текущее время
def get_time_now():
    return datetime.now().strftime("%H:%M")


# удаленный ивент  todo
def ts_event(timer):
    print("время очередного события", timer)
    tsping.client_with_group_list('"Сегодня"\n'.join(config.raid_days[get_day_of_weak()][time]))


while True:
    # проверяем день в списке рейдовых дней
    if get_day_of_weak() in config.raid_days:
        # принт для дебага
        print("DEBUG ", get_day_of_weak(), config.raid_days[get_day_of_weak()])
        # считываем список в строку для проверки
        for time in config.raid_days[get_day_of_weak()]:
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
                # print("Сегодня", '\n'.join(raid_days[get_day_of_weak()][time]))
    # время проверки
    sleep(config.sleep_time)
