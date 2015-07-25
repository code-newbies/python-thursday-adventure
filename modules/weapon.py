# weapons.py
"""Beware! weapons inside!!!"""
from modules.item import Item

class Weapon(Item):
    """
    This is the base class for a weapon. Each weapon instance takes
    a name as a string and damage as an int.
    """
    def __init__(self, damage):
        super().__init__()
        self.damage = damage
