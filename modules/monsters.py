# monsters.py
""" This module contains all sorts of creatures and creepies that
inhabit the game
"""

from modules.locatable import Locatable
from modules.movement import next_tile, what_direction
from modules.hp import Health_Points

class Monster(Locatable, Health_Points):
    def __init__(self, name, description, health_pts):
        Locatable.__init__(self)
        Health_Points.__init__(self, health_pts)
        self.name = name
        self.description = description
        self.target = (0, 0)
        self.move_ai = True

    def set_target(self, target):
        """Sets the feature of the level that the cockroach will attempt
        to move toawards.  i.e. the exit
        """
        self.target = target

    def move(self):
        """Move uses the Movement class to move a square towards it's target"""
        target_tile = next_tile(self.coords, self.target)
        direction = what_direction(self.coords, target_tile)

        self.place(target_tile)
        return direction

    @property
    def damage(self):
        pass

class Cockroach(Monster):
    """Being the first creature of the game, the cockroach holds a special
    place in the pantheon of the world
    """
    def __init__(self, name, description):
        Monster.__init__(self, name, description, 5)

    @property
    def damage(self):
        return 1

    Weapon = Weapon(1)
