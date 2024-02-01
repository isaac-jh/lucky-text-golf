from .field import Field

class Club:
    grade: str
    distance: int

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
