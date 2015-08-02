# command_line_interface.py
"""This module handles interacting with the user on the command line"""


class CommandLine:
    '''This class contains interactions with the user via command line.'''
    def __init__(self, engine, prompt_func=input, print_func=print):
        self.prompt = prompt_func
        self.display = print_func
        self.command_mapping = self.commands(engine)

    def commands(self, engine):
        """Returns a list of valid commands in tuple form
        tuple is (command, function, description, valid_outside_room)
        """
        n_response = self.prompt("Please choose a key to be your north movement: ")
        e_response = self.prompt("Please choose a key to be your east movement: ")
        s_response = self.prompt("Please choose a key to be your south movement: ")
        w_response = self.prompt("Please choose a key to be your west movement: ")
        command_list = [
            ("help", engine.display_help, "display this help menu", True),
            ("begin", engine.start, "start the game", True),
            (w_response, engine.west, "move west", False),
            (s_response, engine.south, "move south", False),
            (n_response, engine.north, "move north", False),
            (e_response, engine.east, "move east", False),
            ("x", engine.coordinates, "display current tile co-ordinates", False),
            ("e", engine.exit, "exit the map", False),
            ("a", engine.item_count, "returns item count", False),
            ("m", self.map_key, "display map key", True)
            ]

        return command_list

    def current_commands(self, in_room):
        """Returns information in tuple form on the commands that are currently
        valid; this can change based on whetheror not the player has typed
        'begin'
        """
        if in_room:
            commands = self.command_mapping
        else:
            commands = list(filter(lambda x: x[3] == True, self.command_mapping))

        return commands

    def display_help(self, in_room):
        """Creates a string containing all of the currently valid commands"""
        possible_commands = self.current_commands(in_room)

        help_text = """
You asked for help and here it is!

The commands that you can use are as follows:

q - quit the game"""

        self.display(help_text)
        for command in possible_commands:
            self.display("{0} - {1}".format(command[0], command[2]))

    def map_key(self):
        """Displays a list of symbols on the map"""
        return self.display("""
        Map Key\n
        %s: Entrance\n
        %s: Key\n
        %s: Exit\n
        %s: Player\n
        %s: Gold
        """ % (">", "~", "<", "@", "$"))

    def greet(self):
        """Welcomes the player and gets their name"""
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))
        return response

    def display_end_of_game(self):
        """Displays the end of game message to the user"""
        self.display("Congratulations! You have completed the game.")
