# player.py
from modules.hp import HealthPoints
""" This is the module for all things player related"""
from modules.locatable import Locatable
from modules.hp import Health_Points
from modules.weapon import Weapon

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
        self.health = HealthPoints(10)

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

    weapon = Weapon(1)

    def dies(self):
        return "As you fall to the ground, gasping your final breath, you wish that you had only had the opportunity to taste that wonderful smelling bacon."
