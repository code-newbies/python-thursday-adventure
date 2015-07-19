import pytest
from os.path import join
from os import getcwd
from modules.world import Engine

def load_room(room_file, ui):
    engine = ui.get_engine()
    engine.room_file = room_file
    return ui, engine

def load_test_room(ui):
    return load_room("test_room.json", ui)

def load_roach_room(ui):
    return load_room("roach_room.json", ui)

def load_item_room(ui):
    return load_room("item_room.json", ui)

def load_tiny_room(ui):
    return load_room("tiny_room.json", ui)

def load_alexander_room(ui):
    return load_room("alexander_room.json", ui)

def build_path(file_n_path):
    base_path = getcwd()
    return join(base_path, *file_n_path)

def at_location(room, item, expected_x, expected_y):
    x, y = room.locate(item)
    return expected_x == x and expected_y == y

@pytest.fixture()
def ui():
    return UserInterfaceForTests()

class UserInterfaceForTests:
    def __init__(self):
        self.commands = []
        self.printed = []
        self.command_count = 0
    
    def get_engine(self):
        return Engine(self.library_path(), self.fake_input, self.fake_print)

    def library_path(self):
        base_path = getcwd()
        return join(base_path, "tests", "fixtures")

    def say(self,command):
        self.commands.append(command)

    def next_command(self):
        try:
            command = self.commands[self.command_count]
        except IndexError:
            details = """
            Game expected command that was not anticpated
            printed queue: {0}
            command queue: {1}
            command_count: {2}
            """.format(self.printed, self.commands, self.command_count)
            raise AssertionError(details)
        
        self.command_count += 1
        return command

    def fake_print(self, print_text):
        self.printed.append(print_text)

    def fake_input(self, prompt_value):
        self.fake_print(prompt_value)
        say = self.next_command()
        return say

    def output_on_line(self, text, index):
        return text in self.printed[index]

    def output_anywhere(self, text):
        for output in self.printed:
            if text in output:
                return True

        return False 

    def output_index(self, text):
        for i, output in enumerate(self.printed):
            if text in output:
                return i

        return None

