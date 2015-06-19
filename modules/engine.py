
class Engine:
    def __init__(self, prompt_func=input, print_func=print):
        self.prompt = prompt_func
        self.display = print_func
        self.prompt_char = ">"

    def start(self):
        self.greet()
    
    def greet(self):
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))

    def main_loop(self):
        play = True

        while play:
            command = self.prompt(self.prompt_char)

            if command == "Q":
                play = False
