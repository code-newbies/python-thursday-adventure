# locatable.py
""" In support of the Level class, Locatable module contains code that is
location aware
"""
from uuid import uuid4

class Locatable:
    """The ancestor class for stuff in a Level that is aware of where it is"""
    def __init__(self):
        self.uid = uuid4()
        self.coords = (0, 0)
        self.display = "!"
        self.display_priority = 0
        self.move_ai = False

    def place(self, coords):
        """Sets the coordinates of the object"""
        self.coords = coords

    def set_display(self, display):
        """Returns the symbol that represented this object on the map"""
        self.display = display

    def is_at(self, coords):
        """Used to determine if this object is located as specific
        coordinates
        """
        return self.coords == coords

    def locate(self):
        """Returns the object's current location"""
        return self.coords

    def travel(self, direction):
        """Given a character representing a cardinal direction
        this method will move the object in that direction"""
        if direction == "n":
            self.coords = (self.coords[0], self.coords[1] + 1)
        elif direction == "s":
            self.coords = (self.coords[0], self.coords[1] - 1)
        elif direction == "e":
            self.coords = (self.coords[0] + 1, self.coords[1])
        elif direction == "w":
            self.coords = (self.coords[0] - 1, self.coords[1])

    def has_move_ai(self):
        """Used to indicate that this object will want to move"""
        return self.move_ai
