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
        if item.name in self.items:
            self.items[item.name]['count'] += 1
        else:
            self.items[item.name] = {'count': 1, 'name':item.name, 'item': item}
    
    def dump(self):
        return self.items

    def format_item(self, item):
        return ("{0} {1}\n".format(item['count'], item['name']))

    def look(self):
        seen = ""

        for item in self.items:
            seen = seen + self.format_item(self.items[item])

        return seen
