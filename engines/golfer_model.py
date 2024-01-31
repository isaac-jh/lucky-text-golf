from .club_model import Club, Driver, Wood, Iron, Wedge, Putter

class Golfer:
    name: str
    exp: int = 0
    cleared_courses: int = 0

    def __init__(self, name) -> None:
        self.name = name

    def get_level(self):
        if self.exp < 100:
            return self.exp // 10
        elif self.exp < 300:
            return (self.exp - 100) // 20 + 10
        elif self.exp < 600:
            return (self.exp - 300) // 30 + 20
        elif self.exp < 1000:
            return (self.exp - 600) // 40 + 30
        elif self.exp < 1500:
            return (self.exp - 1000) // 50 + 40
        else:
            return 50
    
    def todays_distance_condition(self, club: Club):
        pass

    def tee_shot(self, club: Driver | Wood | Iron):
        pass

    def fairway_shot(self, club: Club):
        pass

    def rough_shot(self, club: Iron | Wedge):
        # wood 계열 고를 경우 비거리 감소
        pass

    def bunker_shot(self, club: Iron | Wedge):
        # green bunker 일 경우에는 approach로 고려
        pass

    def approach(self, wedge: Wedge):
        pass

    def putting(self, putter: Putter):
        pass
