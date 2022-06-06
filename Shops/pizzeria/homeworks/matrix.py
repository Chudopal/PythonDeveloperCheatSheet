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
import time, random
from abc import ABC, abstractmethod


class MatrixCitizen(ABC):
    def __init__(self, name: str):
        self.name = name
        self.position = [0, 0]

    @abstractmethod
    def __repr__(self):
        pass

    def make_move(self):
        direction = random.randint(1, 4)
        if direction == 1:
            pass
        elif direction == 2:
            pass
        elif direction == 3:
            pass
        else:
            pass


class Agent(MatrixCitizen):
    def __init__(self, name: str = 'Smith'):
        super().__init__(name)
        self.role = 'Agent'

    def __repr__(self):
        return "A"


class Chosen(MatrixCitizen):
    def __init__(self, name: str = 'Neo'):
        super().__init__(name)
        self.role = 'Chosen'

    def __repr__(self):
        return "C"


class City:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.grid = [['-' for i in range(self.columns)] for j in range(self.rows)]

    def __repr__(self):
        return '\n'.join([" ".join([str(cell) for cell in row]) for row in self.grid]) + "\n"


class Matrix:
    def __init__(self, city_rows: int, city_cols: int, agents_num: int):
        self.city = City(city_rows, city_cols)
        self.chosen = Chosen()
        self.agents = [Agent() for _ in range(agents_num)]
        self.citizens = [self.chosen] + self.agents
        self._arrange_citizens()

    def _arrange_citizens(self):
        for citizen in self.citizens:
            citizen.position = [
                random.randint(0, self.city.rows - 1),
                random.randint(0, self.city.columns - 1)
            ]
            self._set_citizen(citizen)

    def _set_citizen(self, citizen: MatrixCitizen):
        self.city.grid[citizen.position[0]][citizen.position[1]] = citizen


mega_matrix = Matrix(4, 4, 4)
print(mega_matrix.citizens)
print(mega_matrix.city)
