import pytest
from tests.helpers import ui
from modules.cockroach import Cockroach

@pytest.fixture
def roach():
    return Cockroach()

def test_roach_knows_that_it_is_a_roach(roach):
    assert roach.name == "cockroach"

def test_roach_knows_where_it_starts(roach, ui):
    pass
    
