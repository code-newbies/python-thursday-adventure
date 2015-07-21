from os import getcwd
from os.path import join
import json 
from modules.player import Player
from modules.items import Item
from modules.items import Bag
from modules.cockroach import Cockroach

class Room:
    """
    Room

    This class handles the loading of level data to and from files
    """
    def __init__(self, library_path, first_file):
        self.room_file = first_file
        self.library_path = library_path
        self.exit_text = None
        self.next_level = None
        self.name = None
        self.description = None

    def enter(self, entrance_name):
        level = self.get_room_data()
        x, y = level.locate(entrance_name)
        level.add_item("player", x, y)
        return level
        
    def enter_next_level(self):
        has_next_level = self.next_level != None
        level = None

        if has_next_level:
            self.room_file = self.next_level
            level = self.enter("entrance")    

        return level, has_next_level
		
    def room_description(self):
        return self.description

    def hydrate(selfi, data):
        return data

    def get_room_data(self):
        path_n_file = join(self.library_path, self.room_file)
        f = open(path_n_file, "r")
        data = json.load(f)
        f.close()

        locations = self.hydrate(data['locations'])
        size = data['size']
        level = Map(locations, size)

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

class Map:
    """
    Map

    This class handles the concept of relative locations and where things "are"
    """
    def __init__(self, data, size):
        self.data = data
        self.size = size

    def locate(self, location_name):
        x = self.data[location_name]['x']  
        y = self.data[location_name]['y']  
        return (x,y)

    def add_item(self, name, x, y):
        item = {}

        item['x'] = x
        item['y'] = y

        self.data[name] = item

    def get_objects(self):
        return self.data.keys()
    
    def remove(self, name):
        self.data.pop(name)

    def draw_map(self):
        lines = []

        for y in range(0, self.size):
            map = ""

            for x in range(0, self.size):
                items_in_coord = self.items(x, y)

                if 'player' in items_in_coord:
                    char = "@"
                elif len(items_in_coord) > 0:
                    char = self.data[items_in_coord[0]]["display"] 
                else:
                    char = "."

                map += char

            lines.append(map)
        map = ""

        return "\n".join(reversed(lines))

    def items(self, x, y):
        found = []

        objects = self.get_objects()
        for item in objects:
            if self.data[item]['x'] == x and self.data[item]['y'] == y:
                found.append(item)
        return found

    def go_north(self, item):
        x,y = self.locate(item)
        possible = y + 1 < self.size

        if possible:
            self.data[item]['y'] += 1

        return possible

    def go_south(self, item):
        x,y = self.locate(item)
        possible = y > 0

        if possible:
            self.data[item]['y'] -= 1

        return possible

    def go_east(self, item):
        x,y = self.locate(item)
        possible = x + 1 < self.size

        if possible:
            self.data[item]['x'] += 1

        return possible

    def go_west(self, item):
        x,y = self.locate(item)
        possible = x > 0

        if possible:
            self.data[item]['x'] -= 1

        return possible

    def exit(self):
        player_x, player_y = self.locate("player")
        exit_x, exit_y = self.locate("exit")

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
        self.room = Room(self.library_path, self.room_file)
        self.level = self.room.enter("entrance")
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
        if not self.level.go_north('player'):
            self.ui.display("You cannot go north")

    def south(self):
        if not self.level.go_south('player'):
            self.ui.display("You cannot go south")

    def east(self):
        if not self.level.go_east('player'):
            self.ui.display("You cannot go east")

    def west(self):
        if not self.level.go_west('player'):
            self.ui.display("You cannot go west")

    def exit(self):
        can_exit = self.level.exit()

        if can_exit:

            if self.room.exit_text == None:
               
                self.ui.display("You have exited {0}".format(self.room.name))
            else:
                self.ui.display(self.room.exit_text)

            next_level, has_next_level = self.room.enter_next_level()
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
