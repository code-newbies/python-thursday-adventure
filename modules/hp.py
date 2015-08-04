class Health_Points():
    """This class is for health points of the player. Item bonuses
    and other bonuses are integers. """

    def __init__(self, base):
        self.base = base
	self.item_bonuses = None
	self.other_bonuses = None

    def calc_health(self):
        return self.base + self.item_bonuses + self.other_bonuses

    def take_damage(self, damage):
	self.base -= damage
	if self.calc_damage() <= 0:
	    self.dies()

    def dies(self):
	pass
	# This function is to be extended by derived classes.
	# Declaring this function here allows self.dies() to be 
	# called above, and have the derived dies function called.
