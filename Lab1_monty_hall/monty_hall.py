# Программа принимает на вход число дверей, число машин и количество итераций.
# На каждой итерации учитывается выигрыш при стратегии смены двери и выборе первоначальной двери, чтобы потом посчитать
# отношение удачных исходов при выборе той или иной стратегии.
# Если результат не приближен к теоретической вероятности, программа выводит сообщение об ошибке в расчетах и завершает работу.
# После всех итераций выводится сообщение о том, какую стратегию выбрать.
# Теоретически всегда нужно сменить дверь.

import sys
from random import seed, randint
import numpy as np

# открыть дверь с флагом False (т.е. без машины) из массива doors, которую не выбрал участник
def show_goat(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or doors_array[host_choice]:
        host_choice = randint(carsTotal, doorsTotal-1)
    return host_choice

# открыть дверь с флагом True (т.е. с машииной) из массива doors, которую не выбрал участник
def show_car(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or not doors_array[host_choice]:
        host_choice = randint(0, carsTotal)
    return host_choice

# Стратегия смены двери: возвращает True, если победа при случайном выборе двери
def change_door(players_choice, host_choice, doors_array):
    # случайный выбор двери не choice и не doorOpened (проверить, что такие существуют!)
    new_choice = players_choice
    while new_choice == players_choice or new_choice == host_choice:
        new_choice = randint(0, doorsTotal-1)
    if doors_array[new_choice]:
        return True
    else:
        return False

# Стратегия оставаться при своем выборе: возвращает True, если победа
def not_to_change_door(players_choice, doors_array):
    if doors_array[players_choice]:
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: enter number of doors, cars, and iterations.")
        exit(1)

    doorsOpened = 1  # по условию задачи ведущий открывает дверь 1 раз
    doorsTotal = int(sys.argv[1])
    carsTotal = int(sys.argv[2])
    iterations = int(sys.argv[3])

    if doorsTotal < carsTotal + doorsOpened + 1:
        print("That way the player always wins. Try different numbers.")
        exit(1)
    if carsTotal > doorsTotal - 2:
        print("Number of cars is max n-2")
        exit(1)

    # цвета в консоли для удобства
    B = '\033[30m'  # black
    R = '\033[31m'  # red
    G = '\033[32m'  # green

    # условные вероятности выигрыша при смене двери и при изначальном выборе
    pWithChange = (carsTotal * (doorsTotal - 1))/(doorsTotal * (doorsTotal - 1 - doorsOpened))
    pWithoutChange = (carsTotal/doorsTotal)

    # счетчики для выигрышей игрока
    winsWithChange = 0
    winsWithoutChange = 0

    for i in range(0, iterations):
        # для нескольких открытых дверей можно записывать флаги в массив
        # doorsOpened = np.zeros((doorsTotal), dtype=np.bool_)
        doors = np.zeros(doorsTotal, dtype=np.bool_)
        doors[:carsTotal] = True

        # игра
        seed()
        choice = randint(0, doorsTotal - 1)
        doorOpened = show_goat(choice, doors)
        # # alternative
        # doorOpened = show_car(choice, doors)

        if change_door(choice, doorOpened, doors):
            winsWithChange += 1
        if not_to_change_door(choice, doors):
            winsWithoutChange += 1

    ratioWithChange = winsWithChange / iterations
    ratioWithoutChange = winsWithoutChange / iterations

    if abs(ratioWithChange - pWithChange) > 0.01:
        print('{}Расхождение в расчетах: вероятность выигрыша при смене двери = {},'
              ' на практике - {}. {}'.format(R, pWithChange, ratioWithChange, B))
        exit(1)

    if abs(ratioWithoutChange - pWithoutChange) > 0.01:
        print('{}Расхождение в расчетах: вероятность выигрыша, если оставить первую дверь = {},'
              ' на практике - {}. {}'.format(R, pWithoutChange, ratioWithoutChange, B))
        exit(1)

    if ratioWithChange > ratioWithoutChange:
        print("{} Сменить дверь при {} дверей и {} машин: "
              "{}% против {}%.{}".format(G, doorsTotal, carsTotal, ratioWithChange*100, ratioWithoutChange*100, B))
    else:
        print("Оставить первоначальную дверь при {} дверей и {} машин: "
              "{}% против {}%.".format(doorsTotal, carsTotal, ratioWithoutChange*100, ratioWithChange*100))
