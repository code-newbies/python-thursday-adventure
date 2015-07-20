import pytest
from modules.movement import Movement

@pytest.fixture
def movement():
    return Movement()


def test_movement_knows_which_tile_is_north(movement):
    x,y = movement.adjacent_tile('n', 1, 1)
    assert x == 1
    assert y == 2

def test_movement_knows_which_tile_is_south(movement):
    x,y = movement.adjacent_tile('s', 1, 1)
    assert x == 1
    assert y == 0

def test_movement_knows_which_tile_is_east(movement):
    x,y = movement.adjacent_tile('e', 1, 1)
    assert x == 2
    assert y == 1

def test_movement_knows_which_tile_is_west(movement):
    x,y = movement.adjacent_tile('w', 1, 1)
    assert x == 0
    assert y == 1

def test_movement_does_not_move_with_invalid_directions(movement):
    x,y = movement.adjacent_tile('pickle', 1, 1)
    assert x == 1
    assert y == 1

