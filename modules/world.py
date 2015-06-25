from os import getcwd
from os.path import join
import jsonpickle 

class Room():
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

    def get_room_data(self):
        f = open(self.filename, 'r')
        contents = f.read()
        f.close()

        data = jsonpickle.decode(contents)
        self.data = data['locations']
        self.name = data['room']
        self.size = data['size']
    
class Engine:
    def __init__(self, base_path, prompt_func=input, print_func=print):
        self.base_path = base_path
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"


    def start(self):
        player_name = self.greet()
        self.player = Player(response)

        level_file = get_rel_path("level1.json")
        init_level(level_file)
        self.main_loop()


    def init_level(self, level_file):
        self.room = Room(level_file)
        self.room.get_room_data()
        self.room.enter("entrance")

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

    def main_loop(self):
        play = True

        while play:
            command = self.prompt(self.prompt_char).lower()

            if command == "q":
                play = False
            elif command == "help":
                self.display_help()

    def display_help(self):
        help_text = """
        You asked for help and here it is!

        The commands that you can use are as follows:

        help - Display this help menu
        Q - Quit
        """
        self.display(help_text)

