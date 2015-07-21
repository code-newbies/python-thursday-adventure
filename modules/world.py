from os import getcwd
from os.path import join
import json 
from modules.player import Player
from modules.items import Item
from modules.items import Bag
from modules.cockroach import Cockroach

class LevelLoader:
    """
    LevelLoader

    This class handles the loading of level data to and from files
    """
    def __init__(self, library_path, first_file):
        self.room_file = first_file
        self.library_path = library_path
        self.reset()

    def enter(self, player, entrance_name):
        self.reset()
        level = self.get_room_data()
        locatable = level.get_by_name(entrance_name)
        x,y = locatable.locate()
        level.add(player)
        return level
        
    def enter_next_level(self, player):
        has_next_level = self.next_level != None
        level = None

        if has_next_level:
            self.room_file = self.next_level
            level = self.enter(player, "entrance")    

        return level, has_next_level

    def reset(self):
        self.exit_text = None
        self.next_level = None
        self.name = None
        self.description = None
        self.contents = []
		
    def room_description(self):
        return self.description

    def hydrate(self, data):
        contents = []

        if data == None:
            return contents

        for key, value in data.items():
            content_type = "item"
            keys = value.keys()
            description = None

            if "x" not in keys or "y" not in keys:
                pass
            else:
                if "type" in keys:
                    content_type = value["type"]

                if "description" in keys:
                    description = value["description"]

                if content_type == "creature":
                    locatable = Cockroach(key, description)
                else:
                    locatable = Item(key, description)

                locatable.place((value["x"], value["y"]))

                if "display" in keys:
                    locatable.set_display(value["display"])

                contents.append(locatable)

        return contents

    def get_room_data(self):
        path_n_file = join(self.library_path, self.room_file)
        f = open(path_n_file, "r")
        data = json.load(f)
        f.close()

        contents = self.hydrate(data['locations'])
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

class Level:
    """
    Level

    This class handles the concept of relative locations and where things "are"
    """
    def __init__(self, contents, size):
        self.size = size
        self.contents = contents
    
    def contents_at_coords(self, coords):
        return list(filter(lambda x: x.is_at(coords), self.contents))

    def get_by_name(self, name):
        results = list(filter(lambda x: x.name == name, self.contents))

        if len(results) > 0:
            return results[0]
        else:
            return None

    def get_location_by_name(self, name):
        content = self.get_by_name(name)
        if content == None:
            return None
        else:
            return content.locate()

    def add(self, locatable):
        self.contents.append(locatable)

    def get_objects(self):
        return self.contents
    
    def remove(self, name):
        self.data.pop(name)

    def draw_map(self):
        lines = []

        for y in range(0, self.size):
            map = ""

            for x in range(0, self.size):
                items_in_coord = self.contents_at_coords((x, y))

                if len(items_in_coord) > 0:
                    char = items_in_coord[0].display
                else:
                    char = "."

                map += char

            lines.append(map)
        map = ""

        return "\n".join(reversed(lines))

    def can_go_north(self, locatable):
        x,y = locatable.locate()
        possible = y + 1 < self.size

        return possible

    def can_go_south(self, locatable):
        x,y = locatable.locate()
        possible = y > 0

        return possible

    def can_go_east(self, locatable):
        x,y = locatable.locate()
        possible = x + 1 < self.size

        return possible

    def can_go_west(self, locatable):
        x,y = locatable.locate()
        possible = x > 0

        return possible

    def exit(self, player):
        exit = self.get_by_name("exit")

        player_x, player_y = player.locate()
        exit_x, exit_y = player.locate()

        if player_x == exit_x and player_y == exit_y:
            return True 
        else:
            return False
			

class Engine:
    """
    Engine

    This class ties it all together and might be viewed as something somewhat akin to a controller
    in an MVC framework. 

    """
    def __init__(self, library_path, prompt_func=input, print_func=print):
        self.prompt_char = ">"
        self.library_path = library_path 
        self.reset_game()
        self.world = World()
        self.ui = CommandLineInterface(self, prompt_func, print_func)
        self.bag = Bag() 
        self.level = None

    def start(self):
        player_name = self.greet()
        self.player = Player(player_name)
        self.ui.display(self.world.initial_narration())
        self.init_level()

    def init_level(self):
        self.room = LevelLoader(self.library_path, self.room_file)
        self.level = self.room.enter(self.player, "entrance")
        self.player_in_room = True
        self.ui.display(self.room.room_description())

    def reset_game(self):
        self.room_file = "level_1.json"
        self.player_in_room = False

    def in_room(self):
        return self.player_in_room

    def load_player(self, player):
        self.player = player

    def greet(self):
        response = self.ui.prompt("Hello, what is your name: ")
        self.ui.display("Welcome to text adventure, {0}!".format(response))
        return response

    def north(self):
        if not self.level.can_go_north(self.player):
            self.ui.display("You cannot go north")
        else:
            self.player.go("n")

    def south(self):
        if not self.level.can_go_south(self.player):
            self.ui.display("You cannot go south")
        else:
            self.player.go("s")

    def east(self):
        if not self.level.can_go_east(self.player):
            self.ui.display("You cannot go east")
        else:
            self.player.go("e")

    def west(self):
        if not self.level.can_go_west(self.player):
            self.ui.display("You cannot go west")
        else:
            self.player.go("w")

    def exit(self):
        can_exit = self.level.exit(self.player)

        if can_exit:

            if self.room.exit_text == None:
               
                self.ui.display("You have exited {0}".format(self.room.name))
            else:
                self.ui.display(self.room.exit_text)

            next_level, has_next_level = self.room.enter_next_level(self.player)
            if has_next_level:
                self.level = next_level
                self.ui.display(self.room.room_description())
            else:    
                self.player_in_room = False
                self.ui.display("Congratulations! You have completed the game.")
        else:
            self.ui.display("Sorry, you cannot exit {0} because you are not at an exit".format(self.room.name))
        return can_exit

    def item_count(self):
        key_amount = self.room.bag.how_many("key")
        gold_amount = self.room.bag.how_many("gold")
        self.ui.display("You have %d key and %d gold." % (key_amount, gold_amount))

    def coordinates(self):
        x, y = self.level.locate("player")
        self.ui.display("Your co-ordinates are: ({0},{1})".format(x,y))

    def vaccum_key_and_gold(self):
        if self.pick_up_item("key"):
            self.ui.display("You picked up the key!")
        if self.pick_up_item("gold"):
            self.ui.display("You picked up the gold!")
        
    def pick_up_item(self, item):
        if item in self.level.get_objects():
            if self.level.locate("player") == self.level.locate(item):
                self.bag.add(Item(item))
                self.level.remove(item)
                return True

        return False

    def display_help(self):
        self.ui.display_help(self.in_room())

    def invalid_command(self):
        self.ui.display("Sorry that command is not valid, please type 'help' and press enter for a menu.")

    def tuple_values(self, pos, command_list):
        return list(map(lambda x: x[pos], command_list))

    def main_loop(self):
        play = True
        
        while play:
            
            command = self.ui.prompt(self.prompt_char).lower()
            possible_commands = self.ui.current_commands(self.in_room())

            if command == "q":
                play = False
            elif command in (self.tuple_values(0, possible_commands)):
                command_tuple = list(filter(lambda x: x[0] == command, possible_commands))[0]
                command_tuple[1]()
            else:
                self.invalid_command()

            if self.in_room():
                self.ui.display(self.level.draw_map())
                self.vaccum_key_and_gold()



class World:
    """
    World 

    Contains game content in the greater world and not in the levels.   Such as intro and outro.

    """

    def initial_narration(self):

        text = """
Once a very very long time ago an intrepid hero dared to stand up
against the low-sodium cartel.  Our hero knew that the shortage of
pork belly could only have been caused by their brand of devious
evil. 

The low-sodium cartel had reportedly been hoarding pork belly in 
their underground lair.  There could only be one reason for this, 
they wanted to cause a bacon shortage.

Now you must go and enter the dark and moss covered room filled
with evil in order to rescue the big pile of bacon. 

It is dark and you light a torch...
        """
        return text 

class CommandLineInterface:
    '''
    Command Line Interface

    This class contains interactions with the user via command line.

    '''
    def __init__(self, engine, prompt_func=input, print_func=print):
        self.command_mapping = self.commands(engine)
        self.prompt = prompt_func
        self.display = print_func

    def commands(self, engine):
        # tuple is (command, function, description, valid_outside_room)
        command_list = [
            ("help", engine.display_help, "display this help menu", True),
            ("begin", engine.start, "start the game", True),
            ("h", engine.west, "move west", False),
            ("j", engine.south, "move south", False),
            ("k", engine.north, "move north", False),
            ("l", engine.east, "move east", False),
            ("x", engine.coordinates, "display current tile co-ordinates", False),
            ("e", engine.exit, "exit the map", False),
            ("a", engine.item_count, "returns item count", False),
            ("m", self.map_key, "display map key", True)
            ]

        return command_list

    def current_commands(self, in_room):
        if in_room:
            commands = self.command_mapping
        else:
            commands = list(filter(lambda x: x[3] == True, self.command_mapping))

        return commands

    def display_help(self, in_room):
        possible_commands = self.current_commands(in_room)

        help_text = """
You asked for help and here it is!

The commands that you can use are as follows:

q - quit the game"""

        self.display(help_text)
        for command in possible_commands:
            self.display("{0} - {1}".format(command[0], command[2]))

    def map_key(self):
        return self.display("""
        Map Key\n
        %s: Entrance\n
        %s: Key\n
        %s: Exit\n
        %s: Player\n
        %s: Gold
        """ % (">", "~", "<", "@", "$"))
