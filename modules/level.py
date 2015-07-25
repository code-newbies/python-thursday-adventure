"""This module contains map and relative locations of items for a room /level"""


def highest_display_priority(contents):
    """Given a list of locatables this function will return the one with
    the highest priority"""
    max_priority = None

    for locatable in contents:
        if max_priority == None:
            max_priority = locatable
        elif max_priority.display_priority < locatable.display_priority:
            max_priority = locatable

    return max_priority

class Level:
    """Encapsulates the level and relative positions of objects within it.

    This is that class that answers the questions of where things "are".
    """
    def __init__(self, contents, size):
        self.size = size
        self.contents = contents

    def contents_at_coords(self, coords):
        """Returns a list of locatables at a specified location"""
        return list(filter(lambda x: x.is_at(coords), self.contents))

    def get_by_name(self, name):
        """Returns a locatable by name, player will be named 'player'"""
        results = list(filter(lambda x: x.name == name, self.contents))

        if len(results) > 0:
            return results[0]
        else:
            return None

    def get_location_by_name(self, name):
        """Returns the location associated with a named locatable"""
        content = self.get_by_name(name)
        if content == None:
            return None
        else:
            return content.locate()

    def add(self, locatable):
        """Adds a locatable to the level"""
        self.contents.append(locatable)

    def get_objects(self):
        """Returns the internal hash of level contents"""
        return self.contents

    def remove(self, name):
        """Removes an item from the level by name"""
        index = -1

        for i in range(0, len(self.contents)):
            if self.contents[i].name == name:
                index = i

        if index > -1:
            self.contents.pop(index)

    def draw_map(self):
        """Returns a string representation of the level"""
        lines = []

        for pos_y in range(0, self.size):
            map_row = ""

            for pos_x in range(0, self.size):
                items_in_coord = self.contents_at_coords((pos_x, pos_y))

                if len(items_in_coord) > 0:
                    char = highest_display_priority(items_in_coord).display
                else:
                    char = "."

                map_row += char

            lines.append(map_row)
        map_row = ""

        return "\n".join(reversed(lines))

    def can_go_north(self, locatable):
        """Determines if north is a valid move"""
        coords = locatable.locate()
        possible = coords[1] + 1 < self.size

        return possible

    def can_go_south(self, locatable):
        """Determines if south is a valid move"""
        coords = locatable.locate()
        possible = coords[1] > 0

        return possible

    def can_go_east(self, locatable):
        """Determines if east is a valid move"""
        coords = locatable.locate()
        possible = coords[0] + 1 < self.size

        return possible

    def can_go_west(self, locatable):
        """Determines if west is a valid move"""
        coords = locatable.locate()
        possible = coords[0] > 0

        return possible

    def exit(self, player):
        """Exits the player from the level, if that is a valid move"""
        player_x, player_y = player.locate()
        exit_location = self.get_location_by_name("exit")
        if exit_location == None:
            return False

        exit_x, exit_y = exit_location

        if player_x == exit_x and player_y == exit_y:
            player.exit()
            return True
        else:
            return False

    def get_move_ai(self):
        """Returns a list of items in the level that have an ai"""
        return list(filter(lambda x: x.has_move_ai(), self.contents))
