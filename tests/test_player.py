import pytest
from modules.player import Player
from modules.locatable import Locatable
from modules.hp import HealthPoints

@pytest.fixture
def bob():
    return Player("Bob the Mighty")

def test_can_initialize_bob_the_mighty(bob):
    assert bob.description == "Bob the Mighty"
    assert bob.name == "player"

def test_player_is_locatable(bob):
    assert Locatable in Player.__bases__

def test_player_can_be_placed(bob):
    assert bob.coords == (0,0)
    bob.place((0,1)) 
    assert bob.coords == (0,1)

def test_player_displays_as_at(bob):
    bob = Player("guy")
    assert bob.display == "@"

def test_player_has_display_priority_of_one(bob):
    assert bob.display_priority == 1

def test_player_tracks_if_it_is_in_a_room(bob):
    assert bob.in_room() == False
    bob.enter((3,4))
    assert bob.in_room() == True
    bob.exit()
    assert bob.in_room() == False

def test_enter_sets_player_location(bob):
    bob.enter((9,9))
    assert bob.locate() == (9,9)

def test_player_has_health_points(bob):
    assert isinstance(bob.health, HealthPoints)
