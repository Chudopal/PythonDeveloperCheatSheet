"""
4(EXTRA). Матрица

Город - площадка размера N на N

Агенты - перемещаются по городу(случайным образом),
    если будет на одной клетке с избранным, то избранный умрет

Избранный - просто перемещается по городу(случайным образом)

Агенты и избранный могут перемещаться: влево, вправо, вверх,
    вниз по сетке, если кто-то из них дошел до края сетки,
    то направление объекта меняется на противоположное.

Количество агентов и размер города задается через консоль.

Работает программа следующим образом:
выводится в консоль сетка N на N, где случайным образом
указано положение агентов и избранного, например:
C--
-A-
A--
потом итерация
-С-
A--
-A-
потом итерация
A--
-C-
--A
потом агент и избранный пересеклись:
-A-
--(C/A)
---
и воводится сообщение
Chosen is dead. Number of iterations - 4.
Так же можно сделать и с сеткой 5 на 5 или 10 на 10

- Каждая итерация выводится на экран.
- Время между итерациями - 0.5 сек.

Задержку между итерациями делаем через time:

import time
time.sleep(0.5) остановит работу на 0.5 сек

Случайное перемещение можно сделать через random:
import random
random.randint(1, 4) # случайное число от 1 до 4 (включая 1 и 4)
"""

import random
import time
from abc import ABC, abstractmethod


class ChosenGotCaughtException(Exception):
    """Raises when chosen got cornered"""


class City:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.borders = [self.rows, self.cols]
        self.__grid = [['-' for _ in range(self.cols)] for _ in range(self.rows)]

    def __repr__(self):
        return '\n'.join([" ".join([str(cell) for cell in row]) for row in self.__grid]) + "\n"

    @property
    def get_grid(self):
        return self.__grid

    def set_item(self, item: any, position: list[int, int]):
        self.__grid[position[0]][position[1]] = item

    def get_item(self, position: list[int, int]):
        return self.__grid[position[0]][position[1]]

    def set_empty(self, position: list[int, int]):
        self.set_item('-', position)


class MatrixCitizen(ABC):
    def __init__(self):
        self.position = [0, 0]

    @abstractmethod
    def __repr__(self):
        """String representation of object"""

    def set_position(self, position: list[int, int]):
        self.position = position


class Agent(MatrixCitizen):
    def __repr__(self):
        return "A"


class Chosen(MatrixCitizen):
    def __repr__(self):
        return "C"


class Matrix:
    def __init__(self, city_rows: int, city_cols: int, agents_num: int):
        self.city = City(city_rows, city_cols)
        self.chosen_is_dead = False
        self.citizens = [Chosen()] + [Agent() for _ in range(agents_num)]
        self._direction_movements = {
            1: (0, 1),
            2: (1, 0),
            3: (0, -1),
            4: (-1, 0)
        }
        self._init_citizens()

    def _init_citizens(self):
        for citizen in self.citizens:
            citizen.set_position(
                [
                    random.randint(0, self.city.rows - 1),
                    random.randint(0, self.city.cols - 1)
                ]
            )
            self._set_citizen(citizen)

    def _set_citizen(self, citizen: MatrixCitizen):
        cell_value = str(self.city.get_item(citizen.position))
        if (cell_value != 'C') and (cell_value != 'M'):
            self.city.set_item(citizen, citizen.position)
        else:
            self.city.set_item('M', citizen.position)
            self.chosen_is_dead = True

    def _generate_new_position(self, citizen: MatrixCitizen):
        turn_possible = False
        new_position = None
        iter_counter = 0
        while not turn_possible:
            iter_counter += 1
            if iter_counter > 16:
                raise ChosenGotCaughtException
            direction = self._direction_movements.get(random.randint(1, 4))
            raw_position = [sum(i) for i in zip(citizen.position, direction)]
            new_position = self._check_city_borders(raw_position)
            turn_possible = self._check_position(citizen, new_position)
        citizen.set_position(new_position)

    def _check_city_borders(self, position: list[int, int]):
        return [self._check_border(i[0], i[1]) for i in zip(position, self.city.borders)]

    def _check_border(self, position, border):
        if position >= border:
            new_position = position - 2
        elif position < 0:
            new_position = position + 2
        else:
            new_position = position
        return new_position

    def _check_position(self, citizen: MatrixCitizen, position: list[int, int]) -> bool:
        if type(citizen) == Chosen:
            result = type(self.city.get_item(position)) != Agent
        else:
            result = True
        return result

    def make_turn(self):
        for citizen in self.citizens:
            self.city.set_empty(citizen.position)
            self._generate_new_position(citizen)
            self._set_citizen(citizen)

    def enter_the_matrix(self):
        turn_counter = 0
        print(self.city)
        try:
            while not self.chosen_is_dead:
                self.make_turn()
                print(self.city)
                turn_counter += 1
                time.sleep(0.5)
            print(f"Chosen is dead. Number of iterations - {turn_counter}.")
        except ChosenGotCaughtException:
            print(f"Chosen got caught by agents. Number of iterations - {turn_counter}.")


mega_matrix = Matrix(4, 8, 4)
mega_matrix.enter_the_matrix()
