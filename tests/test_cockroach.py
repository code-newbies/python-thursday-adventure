import pytest
from tests.helpers import ui, test_room
from modules.monsters import Cockroach

@pytest.fixture
def roach():
    roach = Cockroach("cockroach", "A big fat hairy cockroach")
    roach.place((2, 3))
    return roach

def test_roach_knows_that_it_is_a_roach(roach):
    assert roach.name == "cockroach"

def test_roach_knows_its_description(roach):
    assert roach.description == "A big fat hairy cockroach"

def test_roach_knows_where_it_starts(roach):
    assert roach.coords[0] == 2
    assert roach.coords[1] == 3

def test_cockroach_has_a_target(roach):
    roach.set_target((0,3))
    assert roach.target == (0,3)

def test_default_target_is_zero_zero(roach):
    assert roach.target == (0,0)

def test_roach_can_update_its_location(roach):
    assert (2,3) == roach.locate()
    roach.place((1,1))
    assert (1,1) == roach.locate()

def test_roach_will_move_towards_target(roach):
    roach.set_target((0,3))
    assert "w" == roach.move()

def test_move_will_update_the_roach_location(roach):
    roach.set_target((0,3))
    roach.move()
    assert (1,3) == roach.locate()

def test_has_move_ai(roach):
    assert roach.has_move_ai()
