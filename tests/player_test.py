import sys
import unittest
from modules.player import Player
from tests.helpers import BaseTest

class PlayerCanMoveTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_can_initialize_bob_the_mighty(self):
        bob = Player("Bob the Mighty")

