from modules.locatable import Locatable

class Player(Locatable):
    """
    Player

    This class holds information about the player.
    """
    def __init__(self, name):
        Locatable.__init__(self)
        self.name = name
