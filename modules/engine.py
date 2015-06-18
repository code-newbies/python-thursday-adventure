
class Engine:
    def __init__(self, prompt_func=input, print_func=print):
        self.prompt = prompt_func
        self.display = print_func

    def start(self):
        response = self.prompt("Hello, what is your name: ")
        self.display("Welcome to text adventure, {0}!".format(response))
