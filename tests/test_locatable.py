import pytest
from tests.helpers import ui, test_room
from modules.locatable import Locatable

@pytest.fixture
def locatable():
    return Locatable()

def test_locatable_has_a_location(locatable):
    locatable.place((2,3))
    assert locatable.coords[0] == 2
    assert locatable.coords[1] == 3

def test_locatable_has_unique_id(locatable):
    another = Locatable()
    third = Locatable()
    assert locatable.uid != another.uid
    assert locatable.uid != third.uid
    assert another.uid != third.uid

def test_locatable_knows_how_to_display_itself(locatable):
    assert locatable.display == "!"

def test_can_set_display(locatable):
    locatable.set_display("@")
    assert locatable.display == "@"

def test_can_test_location(locatable):
    locatable.place((5,6))
    assert not locatable.is_at((3,4))
    assert locatable.is_at((5,6))

def test_locatable_can_be_located(locatable):
    locatable.place((3,3))
    assert locatable.locate() == (3,3)

def test_locatable_can_go_north(locatable):
    locatable.place((1,1))
    locatable.travel("n")
    assert locatable.locate() == (1,2)

def test_locatable_can_go_south(locatable):
    locatable.place((1,1))
    locatable.travel("s")
    assert locatable.locate() == (1,0)

def test_locatable_can_go_east(locatable):
    locatable.place((1,1))
    locatable.travel("e")
    assert locatable.locate() == (2,1)

def test_locatable_can_go_west(locatable):
    locatable.place((1,1))
    locatable.travel("w")
    assert locatable.locate() == (0,1)

def test_locatable_has_display_priority(locatable):
    assert locatable.display_priority == 0

def test_has_no_move_ai_by_defailt(locatable):
    assert locatable.has_move_ai() == False
