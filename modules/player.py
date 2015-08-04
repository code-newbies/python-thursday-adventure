# player.py
""" This is the module for all things player related"""
from modules.locatable import Locatable
from modules.hp import Health_Points

class Player(Locatable, Health_Points):
    """This class holds information about the player."""
    def __init__(self, name):
        Locatable.__init__(self)
	Health_Points.__init__(self, 100)
        self.description = name
        self.name = "player"
        self.display = "@"
        self.display_priority = 1
        self.inside = False

    def in_room(self):
        """Called to determine if the player is inside or outside a level"""
        return self.inside

    def enter(self, coords):
        """Places the player in a level at a particular location"""
        self.place(coords)
        self.inside = True

    def exit(self):
        """Removes the player from a level"""
        self.inside = False
