import sys
import unittest
from os import getcwd
from os.path import join

class BaseTest(unittest.TestCase):
    def init(self):
        self.commands = []
        self.command_count = 0
        self.printed = []
        self.base_path = getcwd()
        self.library_path = join(self.base_path, "tests", "fixtures")
  
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
        try:
            self.assertIn(text, self.printed[index])
        except IndexError:
            details = """
            Expected '{0}' to be printed at position {1}, but nothing was printed; 
            {2}
            """.format(text, index, self.printed)
            raise AssertionError(details)

    def assertPrintedOnAnyLine(self, text):
        self.assertWasPrinted(text, True)

    def assertNotPrintedOnAnyLine(self, text):
        self.assertWasPrinted(text, False)

    def assertWasPrinted(self, text, look_for_printed):
        was_printed = False

        for output in self.printed:
            if text in output:
                was_printed = True

        if was_printed ^ look_for_printed:
            if look_for_printed:
                details = "Expected '{0}' to be printed on any line. Below is what was printed\n {1}"
            else:           
                details = "'{0}' should not be printed on any line. It was printed\n {1}"
            
            raise AssertionError(details.format(text, self.printed))

    def build_path(self, file_n_path):
        return join(self.base_path, *file_n_path)

    def assertLocation(self, room, item, expected_x, expected_y):
        x, y = room.locate(item)
        self.assertEqual(expected_x, x)
        self.assertEqual(expected_y, y)
