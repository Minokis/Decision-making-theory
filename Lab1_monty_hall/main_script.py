# запустить с параметрами, например, 3, 1 и 5.
import sys
import subprocess

if len(sys.argv) != 4:
    print("Usage: enter number of doors, number of cars and incrementations.")
    exit(1)

iters = 10000
d = int(sys.argv[1])
c = int(sys.argv[2])
incrs = int(sys.argv[3])

doors = d
for j in range(1, incrs):
    cars = c
    while cars < doors - 2:
        subprocess.call("python monty_hall.py {} {} {}".format(doors, cars, iters))
        cars += 1
    doors += 1

