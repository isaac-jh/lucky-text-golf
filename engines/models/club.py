from .field import Field
from enum import Enum
from typing import Tuple

class DefaultClubDistance(Enum):
    DRIVER = 150
    WOOD3 = 130
    WOOD5 = 110
    IRON4 = 100
    IRON5 = 90
    IRON6 = 80
    IRON7 = 70
    IRON8 = 60
    IRON9 = 50
    PITCH = 40
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

    def _get_shot_range(self, golfer_level: int):
        pass


class Driver(Club):
    pass


class Wood(Club):
    pass


class Wood3(Wood):
    pass


class Wood5(Wood):
    pass


class Iron(Club):
    pass


class Iron4(Iron):
    pass


class Iron5(Iron):
    pass


class Iron6(Iron):
    pass


class Iron7(Iron):
    pass


class Iron8(Iron):
    pass


class Iron9(Iron):
    pass


class Wedge(Club):
    pass


class Pitch(Wedge):
    pass


class Sand(Wedge):
    pass


class Putter(Club):
    pass
