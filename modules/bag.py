# bag.py
"""This module is a mystical magical storage device and all of the bells and
whistles"""
from modules.item import Item


def format_item(item):
    """formats an item in the bag for printing on screen
    This should be moved into the Item class"""
    return "{0} {1}\n".format(item['count'], item['name'])


class Bag(Item):
    """This class is the incredible inventory bag.
    Like the one from Mary Poppins, only cooler.
    """

    def __init__(self):
        super().__init__(name="Bag of Holding",
                         description="This bag is infinitely large.")
        self.items = {}

    def is_empty(self):
        """Tells you if the bag has any items in it"""
        return self.item_count() == 0

    def item_count(self):
        """Returns the number of items in the bag
        Note: this is the total number of items in the bag not just the count
        of types of items int he bag.  A bag with three flutes and a dog in
        it will have and item_count() or 4"""
        total = 0

        for item in self.items.values():
            total += item['count']

        return total

    def how_many(self, name):
        """Returns the count of a certain type of item in the bag"""
        if name in self.items:
            return self.items[name]['count']
        else:
            return 0

    def add(self, item):
        """Adds an item to the bag"""
        self.add_many(item, 1)

    def add_many(self, item, quantity):
        """Adds more than one of an item to the bag"""
        if item.name in self.items:
            self.items[item.name]['count'] += quantity
        else:
            self.items[item.name] = {'count': quantity,
                                     'name': item.name,
                                     'item': item}

    def remove(self, item_name):
        """Removes an item with the given name from the bag,
        returns (was the item removed, instance of what was removed)"""
        return self.remove_many(item_name, 1)

    def remove_many(self, item_name, quantity):
        """Removes multipe items with the given name from the bag,
        returns (was the item removed, instance of what was removed)"""
        if item_name in self.items:
            item_dict = self.items[item_name]

            item = item_dict['item']
            item_count = item_dict['count']
            new_item_count = item_count - quantity

            if item_count >= quantity:
                item_dict['count'] -= quantity
                taken = quantity
            else:
                taken = item_count

            if new_item_count <= 0:
                self.items.pop(item_name)

            return (taken, item)
        else:
            return (0, None)

    def dump(self):
        """Returns a hash with all the contents of the bag"""
        return self.items

    def look(self):
        """Returns a string listing the contents of the bag"""
        seen = ""

        for item in self.items:
            seen = seen + format_item(self.items[item])

        return seen

