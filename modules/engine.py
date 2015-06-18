
class Engine:
    def __init__(self, prompt_func=input):
        self.prompt = prompt_func

    def start(self):
        response = self.prompt("Hello, what is your name: ")
        print("Welcome to text adventure, {0}!".format(response))
