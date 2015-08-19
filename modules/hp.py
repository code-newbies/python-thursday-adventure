class HealthPoints():
    """This class is for health points of the player. Item bonuses
    and other bonuses are integers. """

    def __init__(self, base):
        self.base = base
        self.item_bonuses = 0
        self.other_bonuses = 0
        self.max_total = self.calc_health()

    def calc_health(self):
        return self.base + self.item_bonuses + self.other_bonuses

    def show_health(self):
        return "Current Health: {} hp".format(self.calc_health())
