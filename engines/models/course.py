from random import randint, choice, shuffle
from typing import List

from .hole import Hole
from .field import Field


class Course:
    data: List[Hole]

    def __init__(self) -> None:
        self.data = []

        par_pair = randint(1,5)
        pars = []
        pars.extend([3] * par_pair)
        pars.extend([5] * par_pair)
        pars.extend([4] * (18 - par_pair * 2))
        shuffle(pars)

        par_3_range = (80, 180)
        par_4_range = (240, 350)
        par_5_range = (400, 600)

        field = (Field.PENALTYAREA, Field.OB)

        rough_range = (50, 90)
        fairway_range = (10,50)
        
        for i in range(18):
            num = i + 1
            par = pars[i]

            if par == 3:
                total_distance = randint(par_3_range[0], par_3_range[1])
            elif par == 5:
                total_distance = randint(par_5_range[0], par_5_range[1])
            else:
                total_distance = randint(par_4_range[0], par_4_range[1])

            miss_shot_rule = choice(field)
            rough_ratio = randint(rough_range[0], rough_range[1])
            fairway_ratio = randint(fairway_range[0], fairway_range[1])
            bunker_ratio = 100 - rough_ratio - fairway_ratio
            green_distance = randint(10, 40)

            self.data.append(Hole(num, par, total_distance, miss_shot_rule, fairway_ratio, rough_ratio, bunker_ratio, green_distance))
