Task 1: Write a simulation of the Monty Hall paradox with parameters:

* n - the total number of doors (3 and higher)
* m - the total number of cars

The simulation should help answering a question: when a player should change the the door?

monty_hall.py:
# Input: number of doors, number of cars and number of games(iterations).
# If resulting ratio of wins is not close to theoretical probability, the program outputs error message and exits.
# After all games the program prints a recommendation to choose a strategy.
# Theoretically, it is always to change the door, if the host opens a door with a goat

Run main_script.py with parameters, for example, 3 1 6.
It will rum monty_hall.py for 3 to 9 doors with cars from 1 to doors-2.


Задание 1: Парадокс Монти Холла (https://ru.wikipedia.org/wiki/Парадокс_Монти_Холла)
Написать симуляцию игры Монти Холла, где параметрами служат:

• Произвольное число дверей n

• Произвольное число машин m (от 1 до n - 2)

Программа должна помочь ответить на вопрос: в каких случаях стоит поменять свое решение и выбрать другую дверь?
Проанализируйте вероятности и возможные исходы и сделайте выводы