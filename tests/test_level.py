import pytest
from modules.level import Level, highest_display_priority
from modules.monsters import Cockroach
from modules.item import Item

@pytest.fixture
def level():
    contents = []
    item = Item("exit", "The real exit")
    item.place((1,2))

    roach = Cockroach("roach", "a big green roach")
    roach.place((2,3))

    contents.append(item)
    contents.append(roach)
    return Level(contents, 4)

def test_level_accepts_a_list_of_contents_and_a_size(level):
    assert len(level.contents) == 2
    assert level.size == 4

def test_contents_at_coords_finds_no_contents_at_empty_coords(level):
    assert len(level.contents_at_coords((0,0))) == 0

def test_contents_at_coords_finds_contents_at_its_coords(level):
    results = level.contents_at_coords((2,3))
    assert len(results) == 1
    assert type(results[0]) is Cockroach

def test_get_by_name_returns_content_with_name(level):
    result = level.get_by_name("roach")
    assert result.name == "roach"

def test_get_by_name_returns_none_for_invalid_name(level):
    result = level.get_by_name("jabberwonky")
    assert result == None

def test_get_location_by_name_returns_just_coords(level):
    result = level.get_location_by_name("roach")
    assert result == (2,3)

def test_can_get_highest_display_priority(level):
    items = []

    high = Item("high", "highest display priority")
    high.display_priority = 100
    items.append(high)

    med = Item("med", "medium display priority")
    med.displau_priority = 10
    items.append(med)

    low = Item("low", "low low low")
    low.display_priority = 0
    items.append(low)

    result = highest_display_priority(items)
    assert result.display_priority == 100

def test_can_return_contents_with_move_ai(level):
    creatures = level.get_move_ai()

    assert len(creatures) == 1
