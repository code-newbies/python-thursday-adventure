from uuid import uuid4
from modules.locatable import Locatable

class Cockroach(Locatable):
    def __init__(self, start_x, start_y):
        Locatable.__init__(self)
        self.name = "cockroach"
        self.place((start_x, start_y))
