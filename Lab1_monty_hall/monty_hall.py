import sys
from random import seed, randint
import numpy as np
from colorconsole import terminal

# открыть дверь с флагом False из массива doors, которую не выбрал участник
def show_goat(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or doors_array[host_choice]:
        host_choice = randint(carsTotal, doorsTotal-1)
    return host_choice

# открыть дверь с флагом True из массива doors, которую не выбрал участник
def show_car(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or not doors_array[host_choice]:
        host_choice = randint(0, carsTotal)
    return host_choice

# Стратегия смены двери: возвращает True, если победа при случайном выборе двери
def change_door(players_choice, host_choice, doors_array):
    # случайный выбор двери не choice и не doorOpened (проверить, что такие существуют!)
    new_choice = players_choice
    while(new_choice == players_choice or new_choice == host_choice):
        new_choice = randint(0, doorsTotal-1)
    if doors_array[new_choice] == True:
        return True
    else:
        return False

# Стратегия оставаться при своем выборе: возвращает True, если победа
def not_to_change_door(players_choice, doors_array):
    if doors_array[players_choice] == True:
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: enter number of doors, cars, and iterations.")
        exit(1)

    doorsTotal = int(sys.argv[1])
    carsTotal = int(sys.argv[2])
    doorsOpened = 1
    iterations = int(sys.argv[3])

    if doorsTotal < carsTotal + doorsOpened + 1:
        print("That way the player always wins. Try different numbers.")
        exit(1)
    if carsTotal > doorsTotal - 2:
        print("Number of cars is max n-2")
        exit(1)

    cond_prob = (carsTotal - carsTotal/doorsTotal)/(doorsTotal-1-doorsOpened)

    B = '\033[30m'  # black
    R = '\033[31m'  # red
    G = '\033[32m'  # green

    winsWithChange = 0
    winsWithoutChange = 0

    for i in range(0, iterations):
        # для нескольких открытых дверей можно записывать флаги в массив
        # doorsOpened = np.zeros((doorsTotal), dtype=np.bool_)
        doors = np.zeros((doorsTotal), dtype=np.bool_)
        doors[:carsTotal] = True

        # игра
        seed()
        choice = randint(0, doorsTotal - 1)
        doorOpened = show_goat(choice, doors)
        # # alternative
        # doorOpened = show_car(choice, doors)
        if change_door(choice, doorOpened, doors) == True:
            winsWithChange += 1
        if not_to_change_door(choice, doors) == True:
            winsWithoutChange += 1

    winsRatio = winsWithChange / iterations
    if abs(winsRatio - cond_prob) > 0.01:
        print("{}Расхождение в расчетах: теор - {}, прак - {}. {}".format(R, cond_prob, winsRatio, B))
    else:
        if winsRatio >= 0.5:
            print("{}{} дверей, {} машин, {} открываний: {}%{}".format(G, doorsTotal, carsTotal, doorsOpened, winsRatio*100, B))
        else:
            print("{}{} дверей, {} машин, {} открываний: {}%{}".format(R, doorsTotal, carsTotal, doorsOpened, winsRatio*100, B))
