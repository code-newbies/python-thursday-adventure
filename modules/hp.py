class Health_Points():
    """This class is for health points of the player. Item bonuses
    and other bonuses are integers. """

    def __init__(self, base):
        self.base = base
	self.item_bonuses = None
	self.other_bonuses = None

    def calc_health(self):
        return self.base + self.item_bonuses + self.other_bonuses
