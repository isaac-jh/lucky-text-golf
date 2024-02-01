import random

from .club import DefaultClubDistance, Driver, Wood, Iron, Wedge, Putter


class CaddyBack:
    driver: Driver = None
    wood3: Wood = None
    wood5: Wood = None
    iron4: Iron = None
    iron5: Iron = None
    iron6: Iron = None
    iron7: Iron = None
    iron8: Iron = None
    iron9: Iron = None
    pitch: Wedge = None
    sand: Wedge = None
    putter: Putter = None

    def __init__(self, golfer_level: int):
        self.driver = Driver(self._get_grade_and_distance(golfer_level, DefaultClubDistance.DRIVER))
        self.wood3 = Wood(self._get_grade_and_distance(golfer_level, DefaultClubDistance.WOOD3))
        self.wood5 = Wood(self._get_grade_and_distance(golfer_level, DefaultClubDistance.WOOD5))
        self.iron4 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON4))
        self.iron5 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON5))
        self.iron6 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON6))
        self.iron7 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON7))
        self.iron8 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON8))
        self.iron9 = Iron(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON9))
        self.pitch = Wedge(self._get_grade_and_distance(golfer_level, DefaultClubDistance.PITCH))
        self.sand = Wedge(self._get_grade_and_distance(golfer_level, int(DefaultClubDistance.PITCH * 7 / 10 )))
        self.putter = Putter(('P', 0))

    @staticmethod
    def _get_grade_and_distance(golfer_level: int, default_distance: DefaultClubDistance | int):
        distance_standard = (golfer_level * 2) + default_distance
        max_distance = distance_standard + 30
        min_distance = distance_standard + golfer_level - 50
        today_distance = random.randrange(min_distance, max_distance + 1)

        grade_value = today_distance - distance_standard

        if grade_value > 20:
            grade = 'SSS'
        elif grade_value > 10:
            grade = 'SS'
        elif grade_value > 0:
            grade = 'S'
        elif grade_value > -10:
            grade = 'A'
        elif grade_value > -20:
            grade = 'B'
        elif grade_value > -30:
            grade = 'C'
        elif grade_value > -40:
            grade = 'D'
        else:
            grade = 'F'
        
        return (grade, today_distance)
