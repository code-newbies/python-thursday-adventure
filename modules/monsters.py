# monsters.py
""" This module contains all sorts of creatures and creepies that
inhabit the game
"""

from modules.locatable import Locatable
from modules.movement import next_tile, what_direction

class Cockroach(Locatable):
    """Being the first creature of the game, the cockroach holds a special
    place in the pantheon of the world
    """
    def __init__(self, name, description):
        Locatable.__init__(self)
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
