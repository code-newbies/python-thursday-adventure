# level_loader.py
"""This module handles hydrating the levels from files"""

from os.path import join
import json
from modules.item import Item
from modules.monsters import Cockroach
from modules.level import Level
from modules.weapon import Weapon

class LevelLoader:
    """This class handles the loading of level data to and from files"""
    def __init__(self, library_path, first_file):
        self.room_file = first_file
        self.library_path = library_path
        self.description = None
        self.exit_text = None
        self.name = None
        self.next_level = None
        self.reset()

    def enter(self, player, entrance_name):
        """Inserts a locatable object into a level"""
        self.reset()
        level = self.get_room_data()
        locatable = level.get_by_name(entrance_name)
        coords = locatable.locate()
        player.enter(coords)
        level.add(player)
        return level

    def enter_next_level(self, player):
        """If the current level specifies a next level, this method will
        move the player from the current level to the next"""
        has_next_level = self.next_level != None
        level = None

        if has_next_level:
            self.room_file = self.next_level
            level = self.enter(player, "entrance")

        return level, has_next_level

    def reset(self):
        """Returns the state of the object to it's initial values"""
        self.exit_text = None
        self.next_level = None
        self.name = None
        self.description = None
        self.contents = []

    def room_description(self):
        """Returns the description of the level"""
        return self.description

    def get_room_data(self):
        """finds and reads the level file and returns a level object ready
        to use"""
        path_n_file = join(self.library_path, self.room_file)

        with open(path_n_file, "r") as file_handle:
            data = json.load(file_handle)

        contents = hydrate(data['locations'])
        size = data['size']

        level = Level(contents, size)

        self.name = data['room']
        self.description = data['description']

        room_keys = data.keys()

        if 'exit_text' in room_keys:
            self.exit_text = data['exit_text']

        if 'next_level' in room_keys:
            self.next_level = data['next_level']
        else:
            self.next_level = None

        return level

def hydrate(data):
    """Populates the level with data from the file"""
    contents = []

    if data == None:
        return contents

    for key, value in data.items():
        content_type = "item"
        keys = value.keys()
        description = None
        target = None
        target_coords = None
        damage = None

        if "x" not in keys or "y" not in keys:
            pass
        else:
            if "type" in keys:
                content_type = value["type"]

            if "description" in keys:
                description = value["description"]

            if "target" in keys:
                target = value["target"]
                target_coords = (data[target]["x"], data[target]["y"])

            if "damage" in keys:
                damage = value["damage"]

            if content_type == "creature":
                locatable = Cockroach(key, description)
                if target != None:
                    locatable.set_target(target_coords)
            else:
                locatable = Item(key, description)

            if content_type == "weapon":
                locatable = Weapon(damage)
                locatable.name = key
                locatable.description = description

            locatable.place((value["x"], value["y"]))

            if "display" in keys:
                locatable.set_display(value["display"])

            contents.append(locatable)

    return contents
