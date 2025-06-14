import time
import datetime
import os
import sys
from BaseFunction import BaseFunction

bot = BaseFunction()

# Спрашиваем, проводить ли битвы бесконечно
answer = None
while(answer != 1 and answer != 0):
    try:
        answer = int(input("Проводить битвы бесконечно?\n1 - да\n0 - нет\n Выбор: "))
    except:
        pass

# Спрашиваем сколько битв проводить, если answer != 0
if answer != 1:
    count_all_fight = None
    while(type(count_all_fight) != int):
        try:
            count_all_fight = int(input("Сколько битв провести?\n0 - Выход из прогрмыы\n Кол-во битв: "))
        except:
            pass
# Иначе проводим битвы бесконечно
else:
    count_all_fight = 999999999 # Ставим бесконечное кол-во битв

if count_all_fight == 0:
    sys.exit() # Закрытие программы

# Переменные для статистики и фиксации чего-либо
count_current_fight = 0 # Текущее кол-во битв
start_time = time.time() # Старт начала выполнения скрипта
time_start_script = datetime.datetime.now().strftime("%H:%M:%S") # Время старта скрипта
time_fight = 0 # Время проведения одного боя
average_time_fight = 0 # Среднее время одного боя

# Переменные для названия скриншотов
AutoFight = "screen/AutoFight.png" # Кнопка Автобитва
Begin = "screen/Begin.png" # Кнопка Начать
Ok = "screen/Ok.png" # Кнопка Ок

# Цикл выполнения скрипта
while(count_current_fight != count_all_fight or answer == "1"):

    # Нажать на кнопку Автобитва
    bot.find_and_click_image(AutoFight)
    
    # Нажать кнопку Начать
    if bot.find_image(Begin):
        bot.find_and_click_image(Begin)
        time_fight = time.time() # Зафиксировали время начала боя
        time.sleep(5)
    
    # Нажать кнопку Ок
    if bot.find_image(Ok):
        bot.find_and_click_image(Ok)
        count_current_fight+=1
        print(f"====================================================================================")
        print(f"Время старта скрипта: {time_start_script}")
        if answer != "1":
            print(f"""Прошло битв: {count_current_fight}/{count_all_fight}\nОсталось битв: {count_all_fight - count_current_fight}\nПрошло времени: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))}""")
        else:
            print(f"""Прошло битв: {count_current_fight}/{count_all_fight}\nПрошло времени: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))}""")
        if time_fight != 0:
            print(f"Время боя: {time.strftime("%H:%M:%S", time.gmtime(time.time() - time_fight))}") # Вычисляем время одного боя
            average_time_fight += time.time() - time_fight # Вычисляем среднее время боя
            print(f"Среднее время боя: {time.strftime("%H:%M:%S",  time.gmtime(average_time_fight / count_current_fight))}")
            print(f"Примерное время проведения боев: {time.strftime("%H:%M:%S",  time.gmtime((average_time_fight / count_current_fight) * (count_all_fight - count_current_fight)))}")


print(f"Время окончания скрипта: {datetime.datetime.now().strftime("%H:%M:%S")}\n")
os.system("pause")