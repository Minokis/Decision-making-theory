# Input: number of doors, number of cars and number of games(iterations).
# If resulting ratio of wins is not close to theoretical probability, the program outputs error message and exits.
# After all games the program prints a recommendation to choose a strategy.
# Theoretically, it is always to change the door.

import sys
from random import seed, randint
import numpy as np

# opens the door without a car (False flag), which was not initially chosen by the player
def show_goat(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or doors_array[host_choice]:
        host_choice = randint(carsTotal, doorsTotal-1)
    return host_choice

# opens the door with a car (True flag), which was not initially chosen by the player
def show_car(players_choice, doors_array):
    host_choice = players_choice
    while players_choice == host_choice or not doors_array[host_choice]:
        host_choice = randint(0, carsTotal)
    return host_choice

# returns True if player changes the door and wins
def change_door(players_choice, host_choice, doors_array):
    # случайный выбор двери не choice и не doorOpened (проверить, что такие существуют!)
    new_choice = players_choice
    while new_choice == players_choice or new_choice == host_choice:
        new_choice = randint(0, doorsTotal-1)
    if doors_array[new_choice]:
        return True
    else:
        return False

# returns True if player sticks to the door and wins
def not_to_change_door(players_choice, doors_array):
    if doors_array[players_choice]:
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: enter number of doors, cars, and iterations.")
        exit(1)

    doorsOpened = 1  # host opens a door once
    doorsTotal = int(sys.argv[1])
    carsTotal = int(sys.argv[2])
    iterations = int(sys.argv[3])

    if doorsTotal < carsTotal + doorsOpened + 1:
        print("That way the player always wins. Try different numbers.")
        exit(1)
    if carsTotal > doorsTotal - 2:
        print("Number of cars is max n-2")
        exit(1)

    # colors in the console
    B = '\033[30m'  # black
    R = '\033[31m'  # red
    G = '\033[32m'  # green

    # conditional probabilities of victory
    pWithChange = (carsTotal * (doorsTotal - 1))/(doorsTotal * (doorsTotal - 1 - doorsOpened))
    pWithoutChange = (carsTotal/doorsTotal)

    # counters
    winsWithChange = 0
    winsWithoutChange = 0

    for i in range(0, iterations):
        # for many open doors another array can be used
        # doorsOpened = np.zeros((doorsTotal), dtype=np.bool_)
        doors = np.zeros(doorsTotal, dtype=np.bool_)
        doors[:carsTotal] = True

        # game
        seed()
        choice = randint(0, doorsTotal - 1)
        doorOpened = show_goat(choice, doors)
        # # alternative (do not use it, as it is not tested and written just for exercise)
        # doorOpened = show_car(choice, doors)

        if change_door(choice, doorOpened, doors):
            winsWithChange += 1
        if not_to_change_door(choice, doors):
            winsWithoutChange += 1

    ratioWithChange = winsWithChange / iterations
    ratioWithoutChange = winsWithoutChange / iterations

    if abs(ratioWithChange - pWithChange) > 0.01:
        print('{}Something is wrong in calculations: probability to win after changing the door is {},'
              ' result - {}. {}'.format(R, pWithChange, ratioWithChange, B))
        exit(1)

    if abs(ratioWithoutChange - pWithoutChange) > 0.01:
        print('{}Something is wrong in calculations: probability to win after sticking to the door is {},'
              ' result - {}. {}'.format(R, pWithoutChange, ratioWithoutChange, B))
        exit(1)

    if ratioWithChange > ratioWithoutChange:
        print("{}Change the door when there are {} doors and {} cars: "
              "{}% versus {}%.{}".format(G, doorsTotal, carsTotal, ratioWithChange*100, ratioWithoutChange*100, B))
    else:
        print("Stick to your choice when there are {} doors and {} cars: "
              "{}% versus {}%.".format(doorsTotal, carsTotal, ratioWithoutChange*100, ratioWithChange*100))
