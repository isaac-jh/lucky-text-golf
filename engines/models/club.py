import random

from .field import Field
from enum import Enum
from typing import Tuple


class DefaultClubDistance(Enum):
    DRIVER = 180
    WOOD3 = 160
    WOOD5 = 140
    IRON4 = 130
    IRON5 = 120
    IRON6 = 110
    IRON7 = 100
    IRON8 = 90
    IRON9 = 80
    PITCH = 70
    # SAND always calculate by PITCH's 70%

class Club:
    grade: str
    distance: int

    def __init__(self, grade_and_distance: Tuple[str, int]) -> None:
        grade, distance = grade_and_distance
        self.grade = grade
        self.distance = distance

    def shot(self, golfer_level: int, field: Field):
        pass

    def _calculate_miss_shot(self, golfer_level: int, club: str):
        value = random.random()
        if club == "D" or club == "W":
            if golfer_level // 10 < 1:
                if value < 0.3:
                    return True
            elif golfer_level // 10 < 3:
                if value < 0.1:
                    return True
        if club == "I":
            if golfer_level // 10 < 1:
                if value < 0.2:
                    return True
            elif golfer_level // 10 < 3:
                if value < 0.05:
                    return True


class Driver(Club):
    def shot(self, golfer_level: int, field: Field):
        if self._calculate_miss_shot(golfer_level, 'D'):
            return 0
        min_distance = self.distance - int((50 - golfer_level) // 2)
        return random.randrange(min_distance, self.distance + 1)


class Wood(Club):
    def shot(self, golfer_level: int, field: Field):
        if self._calculate_miss_shot(golfer_level, 'W'):
            return 0
        min_distance = self.distance - int(((50 - golfer_level) // 2) * 7 / 10)
        if field == Field.ROUGH:
            penalty = 0.9
        return int(random.randrange(min_distance, self.distance + 1) * penalty)


class Iron(Club):
    def shot(self, golfer_level: int, field: Field):
        if self._calculate_miss_shot(golfer_level, 'I'):
            return 0
        min_distance = self.distance - int(((50 - golfer_level) // 2) * 5 / 10)
        if field == Field.ROUGH:
            penalty = 0.9
        if field == Field.BUNKER:
            penalty = 0.6
        return int(random.randrange(min_distance, self.distance + 1) * penalty)


class Wedge(Club):
    # Wedge use shot method only in tee shot
    def shot(self, golfer_level: int, field: Field):
        min_distance = self.distance - int(((50 - golfer_level) // 2) * 3 / 10)
        return random.randrange(min_distance, self.distance + 1)
    
    def approach(self, golfer_level: int, field: Field, goal_distance: int):
        penalty = int(goal_distance * (5 - golfer_level // 10) / 10)
        if field == Field.ROUGH:
            penalty += penalty * 0.1
        if field == Field.BUNKER:
            penalty += penalty * 0.2
        min_distance = self.distance - penalty
        max_distance = self.distance + penalty

        return random.randrange(min_distance, max_distance + 1)


class Putter(Club):
    def putting(self, golfer_level: int, goal_distance: int):
        penalty = int(goal_distance * (5 - golfer_level // 10) / 10)
        min_distance = self.distance - penalty
        max_distance = self.distance + penalty

        return random.randrange(min_distance, max_distance + 1)
