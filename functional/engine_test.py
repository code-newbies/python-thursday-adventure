import sys
import unittest
from modules.engine import Engine

class CanReadStdOutAndMockPrompt(unittest.TestCase):
    def setUp(self):
        self.say = ""

    def fake_input(self, prompt_value):
        print(prompt_value)
        return self.say

    def test_can_get_output_from_stdout_and_input_to_stdin(self):

        self.say = "Hero"
        engine = Engine(self.fake_input)
        engine.start()
        output = sys.stdout.getvalue()
        self.assertIn("Hello, what is your name:", output)
        self.assertIn("Welcome to text adventure, Hero!", output)
