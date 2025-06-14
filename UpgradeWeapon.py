import os
import sys
import time
import datetime
from BaseFunction import BaseFunction

bot = BaseFunction()

count_filed = 0 # Кол-во подвисонов после улучшения оружия
count_upgrate_weapon = 0 # Кол-во улучшений оружия
isAutoUpdate = False # Кнопка Автоулучшение изначально не была нажата

folder_screen = "screen/" # Название папки со скриншотами

# Переменные для названия скриншотов
Snaryaga = f"{folder_screen}Snaryaga.png" # Текст "Снаряжение"
NoSnaryaga = f"{folder_screen}NoSnaryaga.png"  # Текст "По этому фильтру снаряжения не найдено"
Improve = f"{folder_screen}Improve.png" # Кнопка Улучшить
AutoUpdate = f"{folder_screen}AutoUpdate.png" # Кнопка Автоулучшение (синяя)
lvl_8 = f"{folder_screen}8_lvl.png" # Кнопка 8 Уровня
lvl_12 = f"{folder_screen}12_lvl.png" # Кнопка 12 Уровня 
AutoUpdate_2 = f"{folder_screen}AutoUpdate_2.png" # Кнпока Автоулучшение (желтая)
UpdateSuccsess = f"{folder_screen}UpdateSuccsess.png" # Текст "Коснитесь, что бы продолжить"
Close = f"{folder_screen}Close.png" # Кнопка Закрыть (после зависания после улучшения оружия)
Back = f"{folder_screen}Back.png" # Кнопка Назад
Nagrudnik = f"{folder_screen}Nagrudnik.png" # Иконка нагрудника
Braslet = f"{folder_screen}Braslet.png" # Иконка браслета
Amulet = f"{folder_screen}Amulet.png" # Икнона амулете
Kolco = f"{folder_screen}Kolco.png" # Иконка кольца

upgrate_nagrudnik = False # Изначально не улучшаем нагрудник
upgrate_braslet = False # Изначально не улучшаем браслет
upgrate_amulet = False # Изначально не улучшаем амулет
upgrate_kolco = False # Изначально не улучшаем кольцо

who_update = None
# Пока верно не введем 8 или 12
while(who_update != 8 and who_update != 12) and who_update != 0:
    try:
        who_update = int(input("На какой уровень улучшить? 8 или 12?\n0 - Выход из программы\n Уровень: ")) # На какой уровень улучшать: 8 или 12
    except:
        pass

if who_update == 0:
    sys.exit() # Закрытие программы

start_time = time.time() # Старт начала выполнения скрипта
time_start_script = datetime.datetime.now().strftime("%H:%M:%S") # Время старта скрипта

# Цикл выполнения скрипта
while(1):
    # Нажать на снаряжение
    if bot.find_image(Snaryaga) and bot.find_image(NoSnaryaga) == 0:
        bot.click(105, 253) # Нажать на оружие
        
    # Нажать на Улучшить
    if bot.find_image(Improve) and bot.find_image(NoSnaryaga) == 0:
        bot.find_and_click_image(Improve)
        
    # Нажать на Автоулучшение (синяя)
    if bot.find_image(AutoUpdate):
        bot.find_and_click_image(AutoUpdate)
    
    # Улучшить на определенный уровень
    if who_update == 8:
        if bot.find_image(lvl_8):
            bot.find_and_click_image(lvl_8)
    else:
        if bot.find_image(lvl_12):
            bot.find_and_click_image(lvl_12)
        
    # Нажать на Автоулучшение (желтая)
    if bot.find_image(AutoUpdate_2) and isAutoUpdate == False:
        bot.find_and_click_image(AutoUpdate_2)
        isAutoUpdate = True
        
    # Нажать на "Коснитесь, что бы продолжить"
    if bot.find_image(UpdateSuccsess):
        bot.click(937, 1027) # Нажать для прододжения
        
    # Нажать Закрыть после подвисания (окна выбора желаемого уровня улучшения)
    if bot.find_image(Close):
        bot.find_and_click_image(Close)
        count_filed+=1
        
    # Нажать Назад
    if bot.find_image(Back) and bot.find_image(AutoUpdate) and isAutoUpdate == True:
        bot.find_and_click_image(Back)
        isAutoUpdate = False # После возврата на главный экран считаем, что оружие улучшено
        count_upgrate_weapon+=1
        print(f"Время старта скрипта: {time_start_script}")
        print(f"Кол-во зависаний после улучшения оружия: {count_filed}\nКол-во улучшений оружия: {count_upgrate_weapon}\nПрошло времени: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))}")
        time.sleep(0.5)  
    
    # Если "По этому фильтру снаряжение не найдено" - кликает на текст "Снаряжение", что бы убрать выбранное предыдущее оружие
    # И перейти к следующему виду снаряжения
    if bot.find_image(NoSnaryaga):
        bot.find_and_click_image(Snaryaga, wait=2)
        if bot.find_image(Nagrudnik) and upgrate_nagrudnik == False :
            bot.find_and_click_image(Nagrudnik)
            upgrate_nagrudnik = True # Улучшаем нагрудник
        elif bot.find_image(Braslet) and upgrate_braslet == False:
            bot.find_and_click_image(Braslet)
            upgrate_braslet = True # Улучшаем браслет
        elif bot.find_image(Amulet) and upgrate_amulet == False:
            bot.find_and_click_image(Amulet)
            upgrate_amulet = True # Улучшаем амулет
        elif bot.find_image(Kolco) and upgrate_kolco == False:
            bot.find_and_click_image(Kolco)
            upgrate_kolco = True # Улучшаем кольцо
        time.sleep(2)
    
    # Если все виды оружия улучшены - выходим из цикла и завершаем программу
    if bot.find_image(NoSnaryaga) and upgrate_nagrudnik == upgrate_braslet == upgrate_amulet == upgrate_kolco == True:
        break

print(f"\nВсе снаряжение улучшено")
print(f"Время старта скрипта: {time_start_script}")
print(f"Время окончания скрипта: {datetime.datetime.now().strftime("%H:%M:%S")}")
print(f"Прошло времени: {time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time))}")
print(f"Кол-во зависаний после улучшения оружия: {count_filed}")
print(f"Кол-во улучшений оружия: {count_upgrate_weapon}")
os.system("pause")
        




    
