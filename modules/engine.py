from modules.world import Room
from os import path
class Engine:
    def __init__(self, prompt_func=input, print_func=print):
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"

    def start(self):
        self.greet()
        self.main_loop()
    
    def greet(self):
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))
        self.display("Let us begin!")
    def main_loop(self):
        play = True

        while play:
            command = self.prompt(self.prompt_char).lower()

            if command == "q":
                play = False
            elif command == "help":
                self.display_help()
            elif command == "begin":
                self.room = Room(path.join("resources", "Game_Setup.csv"))
                self.room.get_room_data()
                self.room.start_tile_create()
                """
                Code here to initiate player movement on the start tile.
                """

    def display_help(self):
        help_text = """
        You asked for help and here it is!

        The commands that you can use are as follows:

        begin - Starts the game.
        help - Display this help menu
        Q - Quit
        """
        self.display(help_text)

