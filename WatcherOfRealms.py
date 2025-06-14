import time
import datetime
import os
import sys

choose = None
# Пока верно не введем выбор
while(choose != 1 and choose != 2 and choose != 0):
    try:
        choose = int(input(f"Выберите бота для запуска:\n1 - Автобитва\n2 - Улучшение оружия\n0 - Выход из программы\n Выбор: "))
    except:
        pass
    os.system("cls")

if choose == 0:
    sys.exit() # Закрытие программы
if choose == 1:
    print(f"Ваш выбор:  1 - Автобитва")
    print(f"ЧИТАТЬ!!! Перед использованием бота:")
    print(f"1.Перейти в рейд (продвижения/ресурсов/снаряжения/материалов и артефактов)")
    print(f"2.Выбрать желаемый этап")
    print(f"3.Нажать 'Автобитва'")
    print(f"4.ОБЯЗАТЕЛЬНО поставить галочку 'Фоновая битва'")
    print(f"5.Закрыть окно\n")
    import AutoFight
if choose == 2:
    print(f"Ваш выбор:  2 - Улучшение оружия")
    print(f"ЧИТАТЬ!!! Перед использованием бота:")
    print(f"1.Перейти в список героев")
    print(f"2.Выбрать героя ПОЛНОСТЬЮ БЕЗ снаряжения")
    print(f"3.Открыть 'Снаряжение'")
    print(f"3.Открыть 'Снаряжение'")
    print(f"4.Нажать на 'Оружие'")
    print(f"5.Выбрать фильтр 'Без улучшений'\n")
    import UpgradeWeapon
