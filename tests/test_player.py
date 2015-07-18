import pytest
from modules.player import Player

class TestPlayer:

    def test_can_initialize_bob_the_mighty(self):
        bob = Player("Bob the Mighty")
        assert bob.name == "Bob the Mighty"

