# Launch with parameters, for example, 4, 1 and 5.
# The script will run monty_hall.py with 4 doors and 1, 2 cars. Then 5 doors and 1, 2, 3 cars, and so on.
# The last run is param1+param3 doors and doors - 2 cars.
import sys
import subprocess

if len(sys.argv) != 4:
    print("Usage: enter number of doors, number of cars and iterations.")
    exit(1)

# a parameter for monty_hall.py: it is used to calculate statistics of wins.
iters = 20000
# doors, initial number
d = int(sys.argv[1])
# cars, initial number
c = int(sys.argv[2])
# iteratons for a number of doors
incrs = int(sys.argv[3])

doors = d
for j in range(1, incrs):
    cars = c
    while cars < doors - 1:
        subprocess.call("python monty_hall.py {} {} {}".format(doors, cars, iters))
        cars += 1
    doors += 1

