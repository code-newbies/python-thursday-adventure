
class Engine:
<<<<<<< HEAD
<<<<<<< HEAD
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

    def main_loop(self):
        play = True

        while play:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
            command = self.prompt(self.prompt_char).upper()
=======
            command = self.prompt(self.prompt_char).lower()
>>>>>>> 4647ec3... Adds help menu


            if command == "q":
                play = False
<<<<<<< HEAD
=======
    def __init__(self, prompt_func=input):
=======
    def __init__(self, prompt_func=input, print_func=print):
>>>>>>> 579a2d6... Updated to use passed in output function rather than print. This will make for cleaner tests.
        self.prompt = prompt_func
        self.display = print_func

    def start(self):
        response = self.prompt("Hello, what is your name: ")
<<<<<<< HEAD
        print("Welcome to text adventure, {0}!".format(response))
>>>>>>> 4a69152... created fucntional test that allows stdout to be read and allows input to be passed to the program
=======
        self.display("Welcome to text adventure, {0}!".format(response))
>>>>>>> 579a2d6... Updated to use passed in output function rather than print. This will make for cleaner tests.
=======
            command = self.prompt(self.prompt_char)
=======
            command = self.prompt(self.prompt_char).upper()
>>>>>>> e0a63b3... Adds main game loop and test helpers
=======
            command = self.prompt(self.prompt_char).lower()
>>>>>>> 5f1f848... Adds help menu


            if command == "q":
                play = False
<<<<<<< HEAD
>>>>>>> 376ef97... Creates main loop and allows 'Q' to exit the main loop
=======
=======
>>>>>>> 5f1f848... Adds help menu
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

<<<<<<< HEAD
>>>>>>> 4647ec3... Adds help menu
=======
>>>>>>> 5f1f848... Adds help menu
