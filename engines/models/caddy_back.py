import random

from .club import DefaultClubDistance, Driver, Wood3, Wood5, Iron4, Iron5, Iron6, Iron7, Iron8, Iron9, Pitch, Sand, Putter


class CaddyBack:
    driver: Driver = None
    wood3: Wood3 = None
    wood5: Wood5 = None
    iron4: Iron4 = None
    iron5: Iron5 = None
    iron6: Iron6 = None
    iron7: Iron7 = None
    iron8: Iron8 = None
    iron9: Iron9 = None
    pitch: Pitch = None
    sand: Sand = None
    putter: Putter = None

    def __init__(self, golfer_level: int):
        self.driver = Driver(self._get_grade_and_distance(golfer_level, DefaultClubDistance.DRIVER))
        self.wood3 = Wood3(self._get_grade_and_distance(golfer_level, DefaultClubDistance.WOOD3))
        self.wood5 = Wood5(self._get_grade_and_distance(golfer_level, DefaultClubDistance.WOOD5))
        self.iron4 = Iron4(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON4))
        self.iron5 = Iron5(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON5))
        self.iron6 = Iron6(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON6))
        self.iron7 = Iron7(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON7))
        self.iron8 = Iron8(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON8))
        self.iron9 = Iron9(self._get_grade_and_distance(golfer_level, DefaultClubDistance.IRON9))
        self.pitch = Pitch(self._get_grade_and_distance(golfer_level, DefaultClubDistance.PITCH))
        self.sand = Sand(self._get_grade_and_distance(golfer_level, int(DefaultClubDistance.PITCH * 7 / 10 )))
        self.putter = Putter(('P', 0))

    @staticmethod
    def _get_grade_and_distance(golfer_level: int, default_distance: DefaultClubDistance | int):
        distance_standard = (golfer_level * 2) + default_distance
        max_distance = distance_standard + 30
        min_distance = distance_standard + golfer_level - 50
        today_distance = random.random(min_distance, max_distance + 1)

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
