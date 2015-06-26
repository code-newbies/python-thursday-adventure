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
    def __init__(self, filename):
        self.filename = filename
		
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
        self.data[item]['y'] += 1

    def south(self, item):
        self.data[item]['y'] -= 1

    def east(self, item):
        self.data[item]['x'] += 1

    def west(self, item):
        self.data[item]['x'] -= 1

    def get_room_data(self):
        f = open(self.filename, "r")
        data = json.load(f)
        f.close()
        self.data = data['locations']
        self.name = data['room']
        self.size = data['size']
    
    def build_map(self):
        lines = []

        for x in range(0, self.size):
            map = ""

            for y in range(0, self.size):
                items = self.items(x, y)

                if 'exit' in items:
                    char = "<"
                elif 'entrance' in items:
                    char = ">"
                else:
                    char = "."

                map += char

            lines.append(map)
        map = ""

        return "\n".join(lines)

class Engine:
    """
    Engine

    This class ties it all together and might be viewed as soemthing somewhat akin to a controller
    in an MVC framework. 

    """
    def __init__(self, base_path, prompt_func=input, print_func=print):
        self.base_path = base_path
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"
        self.map_path_n_file = self.get_rel_path(["resources", "level_1.json"])
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

        self.init_level(self.map_path_n_file)

    def set_map(self, path_n_file):
        self.map_path_n_file = path_n_file

    def init_level(self, level_file):
        self.room = Room(level_file)
        self.room.get_room_data()
        self.room.enter("entrance")
        self.player_in_room = True

    def get_rel_path(self, file_n_path):
        if type(file_n_path) is list:
            output = join(self.base_path, *file_n_path)
        else:
            output = join(self.base_path, file_n_path)

        return output

    def load_player(self, player):
        self.player = player

    def greet(self):
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))
        return response

    def north(self):
        self.room.north('player')

    def south(self):
        self.room.south('player')

    def east(self):
        self.room.east('player')

    def west(self):
        self.room.west('player')

    def exit(self):
        can_exit = self.room.exit()

        if can_exit:
            self.player_in_room = False
            self.display("You have exited {0}".format(self.room.name))
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


