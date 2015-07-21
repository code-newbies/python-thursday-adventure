import pytest
from tests.helpers import ui, test_room
from modules.cockroach import Cockroach
from modules.world import Map, Room

@pytest.fixture
def roach():
    return Cockroach(2, 3)

def test_roach_knows_that_it_is_a_roach(roach):
    assert roach.name == "cockroach"

def test_roach_knows_where_it_starts(roach):
    assert roach.start_x == 2
    assert roach.start_y == 3

def test_roach_can_init_itself_in_level(test_room, roach):
    level = test_room.enter("entrance")
    roach.init(level)
    assert "cockroach" in level.data.keys()

def test_roach_has_unique_id(roach):
    another_roach = Cockroach(1, 1)
    third_roach = Cockroach(2, 3)
    assert roach.uid != another_roach.uid
    assert roach.uid != third_roach.uid
    assert another_roach.uid != third_roach.uid
