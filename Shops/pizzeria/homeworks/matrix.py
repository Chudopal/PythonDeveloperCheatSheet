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
import time, random, os
from abc import ABC, abstractmethod


class MatrixCitizen(ABC):
    def __init__(self):
        self.position = [0, 0]
        self.row = self.position[0]
        self.col = self.position[1]
        self.direction_movements = {
            1: (0, 1),
            2: (1, 0),
            3: (0, -1),
            4: (-1, 0)
        }

    @abstractmethod
    def __repr__(self):
        """String representation of object"""

    def set_position(self, position: list[int, int]):
        self.position = position
        self.row = position[0]
        self.col = position[1]

    def turn(self, city_borders: list[int, int]):
        direction = self.direction_movements.get(random.randint(1, 4))
        new_position = [sum(i) for i in zip(self.position, direction)]
        self.position = self._check_city_borders(new_position, city_borders)

    def _check_city_borders(self, position: list[int, int], borders: list[int, int]):
        return [self._check_position(i[0], i[1]) for i in zip(position, borders)]

    def _check_position(self, position, border):
        new_position = None
        if position >= border:
            new_position = position - 2
        elif position < 0:
            new_position = position + 2
        else:
            new_position = position
        return new_position


class Agent(MatrixCitizen):
    def __repr__(self):
        return "A"


class Chosen(MatrixCitizen):
    def __repr__(self):
        return "C"


class City:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [['-' for i in range(self.cols)] for j in range(self.rows)]

    def __repr__(self):
        return '\n'.join([" ".join([str(cell) for cell in row]) for row in self.grid]) + "\n"


class Matrix:
    def __init__(self, city_rows: int, city_cols: int, agents_num: int):
        self.city = City(city_rows, city_cols)
        self.chosen = Chosen()
        self.chosen_dead = False
        self.agents = [Agent() for _ in range(agents_num)]
        self.citizens = [self.chosen] + self.agents
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
        cell_value = str(self.city.grid[citizen.row][citizen.col])
        if (cell_value != 'C') and (cell_value != 'M'):
            self.city.grid[citizen.row][citizen.col] = citizen
        else:
            self.city.grid[citizen.row][citizen.col] = "M"
            self.chosen_dead = True

    def _set_empty(self, cell_coords: list[int, int]):
        self.city.grid[cell_coords[0]][cell_coords[1]] = '-'

    def _make_turn(self):
        for citizen in self.citizens:
            self._set_empty(citizen.position)
            citizen.turn([self.city.rows, self.city.cols])
            self._set_citizen(citizen)

    def run_matrix(self):
        turn_counter = 0
        while not self.chosen_dead:
            self._make_turn()
            print(self.city)
            turn_counter += 1
            time.sleep(0.5)
        print(f"Chosen is dead. Number of iterations - {turn_counter}.")


mega_matrix = Matrix(6, 6, 2)
mega_matrix.run_matrix()
