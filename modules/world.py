from os import getcwd
from os.path import join
import json 
from modules.player import Player
from modules.items import Item
from modules.items import Bag
class Room:
    """
    Room

    This class encapsulates the concepts of maps, tiles and co-ordinates.  You can load external json
    files and then add a player and move items around within the room. 
    """
    def __init__(self, library_path, first_file, print_func=print):
        self.room_file = first_file
        self.library_path = library_path
        self.exit_text = None
        self.next_level = None
        self.display = print_func
        self.bag = Bag()
    
    def enter(self, entrance_name):
        self.get_room_data()
        x, y = self.locate(entrance_name)
        self.add_item("player", x, y)

    def enter_next_level(self):
        has_next_level = self.next_level != None

        if has_next_level:
            self.room_file = self.next_level
            self.enter("entrance")    

        return has_next_level

    def add_item(self, name, x, y):
        item = {}

        item['x'] = x
        item['y'] = y

        self.data[name] = item

    def remove(self, name):
        self.data.pop(name)

    def locate(self, location_name):
        x = self.data[location_name]['x']  
        y = self.data[location_name]['y']  
        return (x,y)

    def get_objects(self):
        return self.data.keys()
    
    def items(self, x, y):
        found = []

        objects = self.get_objects()
        for item in objects:
            if self.data[item]['x'] == x and self.data[item]['y'] == y:
                found.append(item)
        return found

    def exit(self):
        player_x, player_y = self.locate("player")
        exit_x, exit_y = self.locate("exit")

        if player_x == exit_x and player_y == exit_y:
            return True
        else:
            return False
			
    def pick_up_item(self):
        if "key" in self.get_objects() and "gold" in self.get_objects():
            if self.locate("player") == self.locate("key"):
                self.bag.add(Item("key"))
                return self.display("You picked up the key!")
            elif self.locate("player") == self.locate("gold"):
                self.bag.add(Item("gold"))
                return self.display("You picked up gold!")
    
    def north(self, item):
        x,y = self.locate(item)
        possible = y + 1 < self.size

        if possible:
            self.data[item]['y'] += 1

        return possible

    def south(self, item):
        x,y = self.locate(item)
        possible = y > 0

        if possible:
            self.data[item]['y'] -= 1

        return possible

    def east(self, item):
        x,y = self.locate(item)
        possible = x + 1 < self.size

        if possible:
            self.data[item]['x'] += 1

        return possible

    def west(self, item):
        x,y = self.locate(item)
        possible = x > 0

        if possible:
            self.data[item]['x'] -= 1

        return possible

    def get_room_data(self):
        path_n_file = join(self.library_path, self.room_file)
        f = open(path_n_file, "r")
        data = json.load(f)
        f.close()
        self.data = data['locations']
        self.name = data['room']
        self.size = data['size']

        if 'exit_text' in data.keys():
            self.exit_text = data['exit_text']

        if 'next_level' in data.keys():
            self.next_level = data['next_level']
        else:
            self.next_level = None
    
    def build_map(self):
        lines = []

        for y in range(0, self.size):
            map = ""

            for x in range(0, self.size):
                items = self.items(x, y)

                if 'player' in items:
                    char = "@"
                elif len(items) > 0:
                    char = self.data[items[0]]["display"] 
                else:
                    char = "."

                map += char

            lines.append(map)
        map = ""

        return "\n".join(reversed(lines))

class Engine:
    """
    Engine

    This class ties it all together and might be viewed as something somewhat akin to a controller
    in an MVC framework. 

    """
    def __init__(self, library_path, prompt_func=input, print_func=print):
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"
        self.library_path = library_path 
        self.room_file = "level_1.json"
        self.player_in_room = False

        # tuple is (command, function, description, valid_outside_room)
        self.command_list = [
            ("help", self.display_help, "display this help menu", True),
            ("begin", self.begin, "start the game", True),
            ("h", self.west, "move west", False),
            ("j", self.south, "move south", False),
            ("k", self.north, "move north", False),
            ("l", self.east, "move east", False),
            ("x", self.coordinates, "display current tile co-ordinates", False),
            ("e", self.exit, "exit the map", False),
            ("a", self.item_count, "returns item count", False),
            ("m", self.map_key, "display map key", True)
            ]

    def current_commands(self):
        if self.in_room():
            commands = self.command_list
        else:
            commands = list(filter(lambda x: x[3] == True, self.command_list))

        return commands

    def display_help(self):
        possible_commands = self.current_commands()

        help_text = """
You asked for help and here it is!

The commands that you can use are as follows:

q - quit the game"""

        self.display(help_text)
        for command in possible_commands:
            self.display("{0} - {1}".format(command[0], command[2]))

    def in_room(self):
        return self.player_in_room

    def start(self):
        player_name = self.greet()
        self.player = Player(player_name)
        self.display(self.initial_narration())

        self.init_level()

    def init_level(self):
        self.room = Room(self.library_path, self.room_file)
        self.room.enter("entrance")
        self.player_in_room = True

    def load_player(self, player):
        self.player = player

    def greet(self):
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))
        return response

    def north(self):
        if not self.room.north('player'):
            self.display("You cannot go north")

    def south(self):
        if not self.room.south('player'):
            self.display("You cannot go south")

    def east(self):
        if not self.room.east('player'):
            self.display("You cannot go east")

    def west(self):
        if not self.room.west('player'):
            self.display("You cannot go west")

    def exit(self):
        can_exit = self.room.exit()

        if can_exit:

            if self.room.exit_text == None:
                self.display("You have exited {0}".format(self.room.name))
            else:
                self.display(self.room.exit_text)

            if not self.room.enter_next_level():
                self.player_in_room = False
                self.display("Congratulations! You have completed the game.")
        else:
            self.display("Sorry, you cannot exit {0} because you are not at an exit".format(self.room.name))
        return can_exit
    def item_count(self):
        key_amount = self.room.bag.how_many("key")
        gold_amount = self.room.bag.how_many("gold")
        self.display("You have %d key and %d gold." % (key_amount, gold_amount))

    def map_key(self):
        return self.display("""
        Map Key\n
        %s: Entrance\n
        %s: Key\n
        %s: Exit\n
        %s: Player\n
        %s: Gold
        """ % (">", "~", "<", "@", "$"))

    def coordinates(self):
        x, y = self.room.locate("player")
        self.display("Your co-ordinates are: ({0},{1})".format(x,y))

    def begin(self):
        self.start()
        

    def invalid_command(self):
        self.display("Sorry that command is not valid, please type 'help' and press enter for a menu.")

    def tuple_values(self, pos, command_list):
        return list(map(lambda x: x[pos], command_list))

    def main_loop(self):
        play = True

        while play:
            command = self.prompt(self.prompt_char).lower()
            possible_commands = self.current_commands()

            if command == "q":
                play = False
            elif command in (self.tuple_values(0, possible_commands)):
                command_tuple = list(filter(lambda x: x[0] == command, possible_commands))[0]
                command_tuple[1]()
            else:
                self.invalid_command()
            if self.in_room():
                self.display(self.room.build_map())
                self.room.pick_up_item()

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

