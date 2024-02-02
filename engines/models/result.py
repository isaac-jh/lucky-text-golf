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
    score_num: int
    exp: int

    def __init__(self, swing_count: int, par: int) -> None:
        sc = swing_count - par
        self.score_num = sc

        if swing_count == 1:
            self.score = Score.HOLE_IN_ONE.value
            self.exp = 10
            return
        
        if swing_count >= (par * 2):
            self.score = Score.DOUBLE_PAR.value
            self.exp = 0
            return

        if sc == -3:
            self.score = Score.ALBATROSS.value
            self.exp = 12
        elif sc == -2:
            self.score = Score.EAGLE.value
            self.exp = 7
        elif sc == -1:
            self.score = Score.BIRDIE.value
            self.exp = 5
        elif sc == 0:
            self.score = Score.PAR.value
            self.exp = 3
        elif sc == 1:
            self.score = Score.BOGEY.value
            self.exp = 2
        elif sc == 2:
            self.score = Score.DOUBLE_BOGEY.value
            self.exp = 2
        elif sc == 3:
            self.score = Score.TRIPLE_BOGEY.value
            self.exp = 1
        elif sc == 4:
            self.score = Score.QUADRUPLE_BOGEY.value
            self.exp = 1
        else:
            self.score = Score.DOUBLE_PAR.value
            self.exp = 0

