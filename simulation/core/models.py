from collections import UserList
from enum import Enum
from random import randint

from config import VIRUS_INITIAL_POINTS


class Group(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


class Virus:
    def __init__(self, life: int, strengh: int, group: Group):
        self.max_life = life
        self.max_strenght = strengh
        self.group = group

        self.current_life = life
        self.current_strenght = strengh

        self.kill_count = 0
        self.damage_count = 0
        self.sore_count = 0

    @classmethod
    def create(cls, group: Group):
        points = VIRUS_INITIAL_POINTS
        life = randint(1, points)
        strenght = points - life

        return cls(life, strenght, group)


class Enviroment(UserList):
    def __init__(self, rows, columns):
        grid = [[[] for _ in range(columns)] for _ in range(rows)]

        super().__init__(grid)

        self.rows = rows
        self.columns = columns

    def __str__(self):
        s = ""
        for row in self:
            s += f"{row}\n"
        return s


e = Enviroment(5, 5)
print(e)

e[0][0].append(0)
print(e)
