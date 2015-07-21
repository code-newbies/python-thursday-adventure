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
