import sys
import unittest

class BaseTest(unittest.TestCase):
    def init(self):
        self.commands = []
        self.command_count = 0
        self.printed = []
  
    def say(self,command):
        self.commands.append(command)

    def next_command(self):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> e0a63b3... Adds main game loop and test helpers
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
<<<<<<< HEAD
=======
        command = self.commands[self.command_count]
>>>>>>> 376ef97... Creates main loop and allows 'Q' to exit the main loop
=======
>>>>>>> e0a63b3... Adds main game loop and test helpers
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

