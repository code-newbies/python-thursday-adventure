from os import getcwd
from os.path import join
import csv

class Room():
    def __init__(self, filename):
        self.filename = filename
		
    def enter(self, player, location):
        pass

    def location(self, location_name):
       return (0,0)

    def get_room_data(self):
        self.data = {}
        with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                        self.data[row['Room Name']] = int(row['Room Size'])
        return self.data
    
    def start_tile_create(self):
        self.startboard = []
        v = self.data['Start']
        for num in range(v):
                self.startboard.append(["[]"] * v)
                def start_tile_print(self):		
                        for row in self.startboard:
                                print(" ".join(row))
        print("\n")			
        return start_tile_print(self)
    
    def key_tile_create(self):
        self.keyboard = []
        v = self.data['Key']
        for num in range(v):
                self.keyboard.append(["[]"] * v)
                def key_tile_print(self):
                        for row in self.keyboard:
                                print (" ".join(row))
        print("\n")		
        return key_tile_print(self)
    
    def gold_tile_create(self):
        self.goldboard = []
        v = self.data['Gold']
        for num in range(v):
                self.goldboard.append(["[]"] * v)
                def gold_tile_print(self):
                        for row in self.goldboard:
                                print (" ".join(row))
        print("\n")			
        return gold_tile_print(self)
    
    def exit_tile_create(self):
        self.exitboard = []
        v = self.data['Exit']
        for num in range(v):
                self.exitboard.append(["[]"] * v)
                def exit_tile_print(self):
                        for row in self.exitboard:
                                print (" ".join(row))
        print("\n")
        return exit_tile_print(self)

    


class Engine:
    def __init__(self, base_path, prompt_func=input, print_func=print):
        self.base_path = base_path
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"

    def start(self):
        self.greet()
        self.main_loop()
    
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

