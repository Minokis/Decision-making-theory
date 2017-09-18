# coding: utf8
import sys
from random import seed, randint

import numpy as np

doorsTotal = int(sys.argv[1])
carsTotal = int(sys.argv[2])
iterations = int(sys.argv[3])

if len(sys.argv) != 4:
    print("Usage: enter number of doors, number of cars and number of iterations.")
    exit(1)

if carsTotal > doorsTotal - 2:
    print("Number of cars is max n-2")

print("Запуск для ", doorsTotal, " дверей, ", carsTotal, " машин, ", iterations, " повторов.")
print("Теоретические вероятности:")
print("Вероятность того, что за конкретной дверью машина: ", carsTotal/doorsTotal)
# # P(Hj| Ci, choice) = P(Hj|C1, choice)P(C1, choice) + P(Hj|C2, choice)P(C2, choice) ...+ P(Hj|Cn, choice)P(Cn, choice)=
# # = P(Ci, choice)* Sum P(Hj|Ci, choice) = 1/n * (1/(n-1) + 0 + 1/(n-2) * (n-2)) = 1/n * 1/(n-1)
print("Вероятность того, что Монти откроет дверь j: ", 1/(doorsTotal*(doorsTotal-1)))
print("Вероятность того, что за одной из оставшихся после выбора дверей ждет приз: ", (doorsTotal-1)/(doorsTotal*(doorsTotal-2)))

def showGoat(choice, doorsWithCars):
    # открыть дверь с флагом False из массива doors, которую не выбрал участник
    hostChoice = choice
    while(choice == hostChoice or doors[hostChoice]):
        hostChoice = randint(carsTotal, doorsTotal-1)
    return hostChoice

# Часть 4.1: Стратегия смены двери: возвращает True, если победа при случайном выборе двери
def changeDoor(choice, hostChoice, doors):
    # случайный выбор двери не choice и не doorOpened (проверить, что такие существуют!)
    choice2 = choice
    while(choice2 == choice or choice2 == hostChoice):
        choice2 = randint(0, doorsTotal-1)
    if doors[choice2] == True:
        return True
    else:
        return False
# Часть 4.2: Стратегия оставаться при своем выборе: возвращает True, если победа
def notToChangeDoor(choice, doorOpened, doors):
    if doors[choice] == True:
        return True
    else:
        return False

winsWithChange = 0
winsWithoutChange = 0

for i in range(0, iterations):
    # # Часть 2: создание дверей
    # doorsOpened = np.zeros((doorsTotal), dtype=np.bool_)
    doors = np.zeros((doorsTotal), dtype=np.bool_)
    # # внести m значений true в массив doors
    doors[:carsTotal] = True
    # # Часть 3: игра
    seed()
    choice = randint(0, doorsTotal - 1)
    doorOpened = showGoat(choice, doors)

    if changeDoor(choice, doorOpened, doors) == True:
        winsWithChange += 1
    if notToChangeDoor(choice, doorOpened, doors) == True:
        winsWithoutChange += 1

print("Changing doors: ", winsWithChange / iterations * 100, "% of wins.")
print("Staying with the first choice: ", winsWithoutChange * 100 / iterations, "% of wins.")