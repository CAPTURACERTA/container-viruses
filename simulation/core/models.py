from __future__ import annotations

import uuid
from collections import UserList
from enum import Enum
from random import randint, randrange, sample

from core.config import (
    ENV_COLS,
    ENV_MAX_VIRUSES,
    ENV_ROWS,
    VIRUS_INIT_POINTS,
    VIRUS_REGEN_BASE,
)


class Group(Enum):
    RED = "🔴"
    GREEN = "🟢"
    BLUE = "🔵"


class Virus:
    def __init__(self, life: int, strengh: int, group: Group):
        self.id = uuid.uuid4()
        self.max_life = life
        self.current_life = life
        self.strenght = strengh
        self.group = group

    def __repr__(self):
        return self.group.value

    @classmethod
    def viruses_interaction(cls, viruses: list[Virus]):

        for virus in viruses:
            sore = 0
            bonus_team_regen = 0

            lookup_viruses = viruses.copy()
            for lookup_virus in lookup_viruses:
                if lookup_virus.id != virus.id:
                    if virus.group != lookup_virus.group:
                        sore += lookup_virus.strenght
                    else:
                        bonus_team_regen += 1

            virus.current_life -= sore
            if virus.current_life < virus.max_life:
                virus.current_life += randint(1, VIRUS_REGEN_BASE + bonus_team_regen)
            if virus.current_life > virus.max_life:
                virus.current_life = virus.max_life

    @classmethod
    def create(cls, group: Group):
        points = VIRUS_INIT_POINTS
        life = randrange(1, points)
        strenght = points - life

        return cls(life, strenght, group)


class Enviroment(UserList):
    def __init__(self, rows: int, columns: int):
        grid = [[[] for _ in range(columns)] for _ in range(rows)]

        super().__init__(grid)

        self.rows = rows
        self.columns = columns
        self.total_squares = self.rows * self.columns

        if self.total_squares < len(Group):
            raise ValueError(
                f"Environment can't be smaler than total groups: {self.total_squares} < {len(Group)}"
            )

    def __str__(self):
        s = ""
        for row in self:
            s += f"{row}\n"
        return s


class Orchestror:
    def __init__(self, enviroment: Enviroment = Enviroment(ENV_ROWS, ENV_COLS)):
        self.enviroment = enviroment

        self.start()

    def start(self):
        viruses_per_group = round(ENV_MAX_VIRUSES / len(Group))
        total_viruses = viruses_per_group * len(Group)
        random_positions = sample(range(self.enviroment.total_squares), total_viruses)
        viruses = []

        for group in Group:
            viruses.extend([Virus.create(group) for _ in range(viruses_per_group)])

        for position in random_positions:
            row = position // self.enviroment.columns
            col = position % self.enviroment.columns
            virus = viruses.pop()
            self.enviroment[row][col].append(virus)
