from .club import Driver, Wood3, Wood5, Iron4, Iron5, Iron6, Iron7, Iron8, Iron9, Pitch, Sand, Putter

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

    def __init__(
        self,
        driver: Driver,
        wood3: Wood3,
        wood5: Wood5,
        iron4: Iron4,
        iron5: Iron5,
        iron6: Iron6,
        iron7: Iron7,
        iron8: Iron8,
        iron9: Iron9,
        pitch: Pitch,
        sand: Sand,
        putter: Putter
    ):
        self.driver = driver
        self.wood3 = wood3
        self.wood5 = wood5
        self.iron4 = iron4
        self.iron5 = iron5
        self.iron6 = iron6
        self.iron7 = iron7
        self.iron8 = iron8
        self.iron9 = iron9
        self.pitch = pitch
        self.sand = sand
        self.putter = putter
