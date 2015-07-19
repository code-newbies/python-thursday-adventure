from uuid import uuid4
from modules.locatable import Locatable
from modules.movement import Movement

class Cockroach(Locatable):
    def __init__(self, name, description):
        Locatable.__init__(self)
        self.name = name
        self.description = description
        self.target = (0,0)
        self.move_ai = True

    def set_target(self, target):
        self.target = target

    def move(self):
        movement = Movement()
        next_tile = movement.next_tile(self.coords, self.target)
        direction = movement.what_direction(self.coords, next_tile)

        self.place(next_tile)
        return direction
