import pytest
from tests.helpers import ui
from modules.cockroach import Cockroach

@pytest.fixture
def roach():
    return Cockroach(2, 3)

def test_roach_knows_that_it_is_a_roach(roach):
    assert roach.name == "cockroach"

def test_roach_knows_where_it_starts(roach):
    assert roach.start_x == 2
    assert roach.start_y == 3
