from functools import reduce

class Item():
    def __init__(self, name):
        self.name = name

class Bag():
    def __init__(self):
        self.items = {}

    def is_empty(self):
        return self.item_count() == 0 

    def item_count(self):
        total = 0

        for item in self.items.values():
            total += item['count']

        return total

    def how_many(self, name):
        if name in self.items:
            return self.items[name]['count']
        else:
            return 0

    def add(self, item):
        self.add_many(item, 1)

    def add_many(self, item, quantity):
        if item.name in self.items:
            self.items[item.name]['count'] += quantity
        else:
            self.items[item.name] = {'count': quantity, 'name':item.name, 'item': item}
    
    def remove(self, item_name):
        if item_name in self.items:
            item_dict = self.items[item_name]

            item = item_dict['item']
            item_count = item_dict['count']
            new_item_count = item_count -1
            item_dict['count'] += new_item_count

            if new_item_count == 0:
                self.items.pop(item_name)

            return (1, item)
        else:
            return (0, None)

    def remove_many(self, item_name, quantity):
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
        return self.items

    def format_item(self, item):
        return ("{0} {1}\n".format(item['count'], item['name']))

    def look(self):
        seen = ""

        for item in self.items:
            seen = seen + self.format_item(self.items[item])

        return seen
