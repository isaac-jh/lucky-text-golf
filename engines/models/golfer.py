import json
from .club import Club, Driver, Wood, Iron, Wedge, Putter
from .caddy_back import CaddyBack

class Golfer:
    name: str
    exp: int
    cleared_courses: list
    caddy_back: CaddyBack

    def __init__(self, name: str) -> None:
        self.name = name
        self.exp = 0
        self.cleared_courses = []

    @staticmethod
    def fetch(json_file: object):
        golfer = Golfer(json_file["name"])
        golfer.exp = json_file["exp"]
        golfer.cleared_courses = json_file["cleared_courses"]
        return golfer
    
    def count_cleared(self):
        return len(self.cleared_courses)
    
    def save(self):
        with open(f'./golfers/{self.name}.json', 'w') as outfile:
            data = { "name": self.name, "exp": self.exp, "cleared_courses": self.cleared_courses }
            json.dump(data, outfile, sort_keys=True, indent=4)

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

    def tee_swing(self, club: Driver | Wood | Iron | Wedge):
        pass

    def fairway_swing(self, club: Driver | Wood | Iron | Wedge):
        pass

    def rough_swing(self, club: Driver | Wood | Iron | Wedge):
        pass

    def bunker_swing(self, club: Iron | Wedge):
        pass

    def approach(self, club: Wedge):
        pass

    def putting(self, club: Putter):
        pass
