import pytest
from os.path import join
from os import getcwd
from modules.engine import Engine
from modules.level_loader import LevelLoader
from modules.player import Player

def init_room(room_file, ui):
    engine = ui.get_engine()
    engine.player = Player("Test Player")
    engine.room_file = room_file
    return ui, engine

def init_test_room(ui):
    return init_room("test_room.json", ui)

def init_roach_room(ui):
    return init_room("roach_room.json", ui)

def init_item_room(ui):
    return init_room("item_room.json", ui)

def init_tiny_room(ui):
    return init_room("tiny_room.json", ui)

def init_alexander_room(ui):
    return init_room("alexander_room.json", ui)

@pytest.fixture
def tiny_room():
    fst = FileTools()
    return load_room("tiny_room.json", fst)

@pytest.fixture
def test_room():
    fst = FileTools()
    return load_room("test_room.json", fst)

@pytest.fixture
def roach_room():
    fst = FileTools()
    return load_room("roach_room.json", fst)

@pytest.fixture
def item_room():
    fst = FileTools()
    return load_room("item_room.json", fst)

@pytest.fixture
def alexander_room():
    fst = FileTools()
    return load_room("alexander_room.json", fst)


def load_room(room_file, fst):
    room_path = fst.build_path(["tests", "fixtures"])
    room_file = room_file
    return LevelLoader(room_path, room_file)

@pytest.fixture()
def fst():
    return FileTools()

@pytest.fixture()
def locations():
    fst = FileTools()
    return fst.load_json_fixture("locations")

class FileTools:
    def build_path(self, file_n_path):
        base_path = getcwd()
        return join(base_path, *file_n_path)

    def load_json_fixture(self, filename):
        import json
        file_n_path = self.build_path(["tests", "fixtures", "{0}.json".format(filename)])
        f = open(file_n_path, "r")
        data = json.load(f)
        f.close
        return data

#def at_location(room, item, expected_x, expected_y):
#    x, y = room.locate(item)
#    return expected_x == x and expected_y == y

@pytest.fixture()
def ui():
    return UserInterfaceForTests()

class UserInterfaceForTests:
    def __init__(self):
        self.commands = ["i", "l", "k", "j"] #dummy game input keys for setup
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
        print("self.command_count = {0}".format(self.command_count))
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

@pytest.fixture
def roach_data():
    return { "cockroach": { "x": 4, "y": 5, "display": "r", "type": "creature" } }

@pytest.fixture
def p1():
    return Player("Arthur, King of the Brittans")

