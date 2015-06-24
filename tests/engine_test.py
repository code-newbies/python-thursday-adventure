import sys
import unittest
from tests.helpers import BaseTest
from modules.engine import Engine
from modules.world import Room
from os import getcwd

prompt = ">"
path = getcwd()

class EngineInitTest(BaseTest):
    def setUp(self):
        self.init()

    def test_engine_accepts_base_path(self):
        self.engine = Engine('foo', self.fake_input, self.fake_print)
        rel_path = self.engine.get_rel_path('bar.baz')
        self.assertIn('foo', rel_path)
        self.assertIn('bar.baz', rel_path)

    def test_rel_path_builds_path_from_list(self):
        path = ['a','quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
        self.engine = Engine('foo', self.fake_input, self.fake_print)
        rel_path = self.engine.get_rel_path(path)
        self.assertIn('foo', rel_path)
        for location in path:
            self.assertIn(location, rel_path)
        

    def test_engine_enters_main_loop(self):
        self.engine = Engine(path, self.fake_input, self.fake_print)
        try:
            self.say("Q")
            self.engine.main_loop()
        except AttributeError:
            self.fail("Engine does not have a main_loop() method")


class EngineTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(path, self.fake_input, self.fake_print)

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


