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
        command = self.commands[self.command_count]
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

