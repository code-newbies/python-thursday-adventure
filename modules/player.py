from modules.locatable import Locatable

class Player(Locatable):
    """
    Player

    This class holds information about the player.
    """
    def __init__(self, name):
        Locatable.__init__(self)
        self.description = name
        self.name = "player"
        self.display = "@"
        self.display_priority = 1
        self.inside = False

    def in_room(self):
        return self.inside

    def enter(self, coords):
        self.place(coords)
        self.inside = True

    def exit(self):
        self.inside = False
