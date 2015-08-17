class Health_Points():
    """This class is for health points of the player. Item bonuses
    and other bonuses are integers. """

    def __init__(self, base):
        self.base = base
        #self.item_bonuses = None
        self.item_bonuses = 0
        #self.other_bonuses = None
        self.other_bonuses = 0

    def calc_health(self):
        return self.base + self.item_bonuses + self.other_bonuses

    def take_damage(self, damage):
        self.base -= damage
        if self.calc_health() <= 0:
            return self.dies()
        else:
            return False

    def dies(self):
        pass
	    # This function is to be extended by derived classes.
        # Declaring this function here allows self.dies() to be 
        # called above, and have the derived dies function called.
