import sys
import pytest
from os import getcwd
from os.path import join

class UserInterfaceForTests:
    def __init__(self):
        self.commands = []
        self.printed = []
        self.command_count = 0

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

    def assertPrinted(self, text, index):
        assert text in self.printed[index]

    def assertPrintedOnAnyLine(self, text):
        self.assertWasPrinted(text, True)

    def assertNotPrintedOnAnyLine(self, text):
        self.assertWasPrinted(text, False)

    def assertWasPrinted(self, text, look_for_printed):
        was_printed = False

        for output in self.printed:
            if text in output:
                was_printed = True

        assert was_printed == look_for_printed

    def assertLocation(self, room, item, expected_x, expected_y):
        x, y = room.locate(item)
        assert expected_x == x
        assert expected_y == y

class BaseTest:
    def init(self):
        self.interface = UserInterfaceForTests()
        self.base_path = getcwd()
        self.library_path = join(self.base_path, "tests", "fixtures")

    def build_path(self, file_n_path):
        return join(self.base_path, *file_n_path)

    def say(self,command):
        self.interface.say(command)
  
    def next_command(self):
        return self.interface.next_command()

    def fake_print(self, print_text):
        self.interface.fake_print(print_text)

    def fake_input(self, prompt_value):
        return self.interface.fake_input(prompt_value)

    def assertPrinted(self, text, index):
        self.interface.assertPrinted(text, index)

    def assertPrintedOnAnyLine(self, text):
        self.interface.assertWasPrinted(text, True)

    def assertNotPrintedOnAnyLine(self, text):
        self.interface.assertWasPrinted(text, False)

    def assertWasPrinted(self, text, look_for_printed):
        self.interface.assertWasPrinted(text, look_for_printed)

    def assertLocation(self, room, item, expected_x, expected_y):
        self.interface.assertLocation(room, item, expected_x, expected_y)
