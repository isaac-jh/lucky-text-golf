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
