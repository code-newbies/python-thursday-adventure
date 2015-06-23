import sys
import unittest
from tests.helpers import BaseTest
from modules.engine import Engine

prompt = ">"

class EngineTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.fake_input, self.fake_print)

    def test_engine_enters_main_loop(self):
        try:
            self.say("Q")
            self.engine.main_loop()
        except AttributeError:
            self.fail("Engine does not have a main_loop() method")

    def test_engine_will_prompt_and_exit_with_q(self):
        self.say("Q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)

    def test_engine_commands_are_not_case_sensitive(self):
        self.say("q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)

    def test_help_will_be_printed_when_asked_for(self):
        self.say("help")
        self.say("q")
        self.engine.main_loop()
        self.assertPrinted("help", 1)
    
    def test_begin_will_start_game(self):
        self.say("begin")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("[]")
