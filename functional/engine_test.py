import sys
import unittest
from modules.engine import Engine

class CanReadStdOutAndMockPrompt(unittest.TestCase):
    def setUp(self):
        self.say = ""
        self.printed = []

    def fake_print(self, print_text):
        self.printed.append(print_text)

    def fake_input(self, prompt_value):
        self.fake_print(prompt_value)
        return self.say

    def test_can_get_output_from_stdout_and_input_to_stdin(self):

        self.say = "Hero"
        engine = Engine(self.fake_input, self.fake_print)
        engine.start()
        self.assertEqual("Hello, what is your name: ", self.printed[0])
        self.assertEqual("Welcome to text adventure, Hero!", self.printed[1])
