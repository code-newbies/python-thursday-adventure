# item.py
"""All sorts of item related stuff belongs in this module."""

from modules.locatable import Locatable

class Item(Locatable):
    """
    Item

    This is the base class for items
    """
    def __init__(self, name=None, description=None):
        Locatable.__init__(self)
        self.name = name
        self.description = description
