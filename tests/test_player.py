import pytest
from modules.player import Player
from modules.locatable import Locatable

class TestPlayer:

    def test_can_initialize_bob_the_mighty(self):
        bob = Player("Bob the Mighty")
        assert bob.name == "Bob the Mighty"

    def test_player_is_locatable(self):
        assert Locatable in Player.__bases__

    def test_player_can_be_placed(self):
        elvis = Player("The King")
        assert elvis.coords == (0,0)
        elvis.place((0,1)) 
        assert elvis.coords == (0,1)
