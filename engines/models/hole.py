from .field import Field
from random import choice

class Hole:
    num: int
    total_distance: int
    miss_shot_rule: Field.PENALTYAREA | Field.OB
    field_ratio: list
    green_distance: int

    def __init__(
            self,
            num: int,
            total_distance: int,
            miss_shot_rule: Field.PENALTYAREA | Field.OB = Field.PENALTYAREA,
            fairway_ratio: int = 60,
            rough_ratio: int = 30,
            bunker_ratio: int = 10,
            green_distance: int = 25
        ) -> None:
        self.num = num
        self.total_distance = total_distance
        self.miss_shot_rule = miss_shot_rule
        self.green_distance = green_distance

        ratio = []
        ratio.extend([Field.FAIRWAY] * fairway_ratio)
        ratio.extend([Field.ROUGH] * rough_ratio)
        ratio.extend([Field.BUNKER] * bunker_ratio)
        self.field_ratio = ratio

    def where_is_my_ball(self):
        return choice(self.field_ratio)
