from os import getcwd
from os.path import join
import json 
from modules.player import Player

class Room:
    """
    Room

    This class encapsulates the concepts of maps, tiles and co-ordinates.  You can load external json
    files and then add a player and move items around within the room. 
    """
    def __init__(self, library_path, first_file):
        self.room_file = first_file
        self.library_path = library_path
        self.exit_text = None
        self.next_level = None
		
    def enter(self, entrance_name):
        x, y = self.locate(entrance_name)
        self.add_item("player", x, y)

    def add_item(self, name, x, y):
        item = {}

        item['x'] = x
        item['y'] = y

        self.data[name] = item

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

    This class ties it all together and might be viewed as soemthing somewhat akin to a controller
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
            ("e", self.exit, "exit the map", False)
            ]

    def display_help(self):
        if self.in_room():
            current_commands = self.command_list
        else:
            current_commands = list(filter(lambda x: x[3] == True, self.command_list))

        help_text = """
You asked for help and here it is!

The commands that you can use are as follows:

q - quit the game"""

        self.display(help_text)
        for command in current_commands:
            self.display("{0} - {1}".format(command[0], command[2]))

    def in_room(self):
        return self.player_in_room

    def start(self):
        player_name = self.greet()
        self.player = Player(player_name)

        self.init_level()

    def init_level(self):
        self.room = Room(self.library_path, self.room_file)
        self.room.get_room_data()
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
            self.player_in_room = False

            if self.room.exit_text == None:
                self.display("You have exited {0}".format(self.room.name))
            else:
                self.display(self.room.exit_text)
        else:
            self.display("Sorry, you cannot exit {0} because you are not at an exit".format(self.room.name))
        return can_exit

    def coordinates(self):
        x, y = self.room.locate("player")
        self.display("Your co-ordinates are: ({0},{1})".format(x,y))

    def begin(self):
        self.start()
        map_ = self.room.build_map()
        self.display(map_)

    def invalid_command(self):
        self.display("Sorry that command is not valid, please type 'help' and press enter for a menu.")

    def tuple_values(self, pos, command_list):
        return list(map(lambda x: x[pos], command_list))

    def main_loop(self):
        play = True

        while play:
            command = self.prompt(self.prompt_char).lower()

            if command == "q":
                play = False
            elif command in (self.tuple_values(0, self.command_list)):
                command_tuple = list(filter(lambda x: x[0] == command, self.command_list))[0]
                command_tuple[1]()
            else:
                self.invalid_command()


