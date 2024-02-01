from enum import Enum

class Score(Enum):
    HOLE_IN_ONE = 'Hole In One'
    ALBATROSS = 'Albatross'
    EAGLE = 'Eagle'
    BIRDIE = 'Birdie'
    PAR = 'Par'
    BOGEY = 'Bogey'
    DOUBLE_BOGEY = 'Double Bogey'
    TRIPLE_BOGEY = 'Triple Bogey'
    QUADRUPLE_BOGEY = 'Quadruple Bogey'
    DOUBLE_PAR = 'Double Par'

class Result:
    score: Score
    exp: int

    def __init__(self, swing_count: int, par: int) -> None:
        if swing_count == 1:
            self.score = Score.HOLE_IN_ONE
            self.exp = 10
        
        if swing_count >= par * 2:
            self.score = Score.DOUBLE_PAR
            self.exp = 0

        sc = swing_count - par
        if sc == -3:
            self.score = Score.ALBATROSS
            self.exp = 12
        elif sc == -2:
            self.score = Score.EAGLE
            self.exp = 7
        elif sc == -1:
            self.score = Score.BIRDIE
            self.exp = 5
        elif sc == 0:
            self.score = Score.PAR
            self.exp = 3
        elif sc == 1:
            self.score = Score.BOGEY
            self.exp = 2
        elif sc == 2:
            self.score = Score.DOUBLE_BOGEY
            self.exp = 2
        elif sc == 3:
            self.score = Score.TRIPLE_BOGEY
            self.exp = 1
        elif sc == 4:
            self.score = Score.QUADRUPLE_BOGEY
            self.exp = 1
        else:
            self.score = Score.DOUBLE_PAR
            self.exp = 0

