import pytest
from modules.movement import adjacent_tile, next_tile, next_direction


def test_knows_which_tile_is_north():
    x,y = adjacent_tile('n', 1, 1)
    assert x == 1
    assert y == 2

def test_knows_which_tile_is_south():
    x,y = adjacent_tile('s', 1, 1)
    assert x == 1
    assert y == 0

def test_knows_which_tile_is_east():
    x,y = adjacent_tile('e', 1, 1)
    assert x == 2
    assert y == 1

def test_knows_which_tile_is_west():
    x,y = adjacent_tile('w', 1, 1)
    assert x == 0
    assert y == 1

def test_does_not_move_with_invalid_directions():
    x,y = adjacent_tile('pickle', 1, 1)
    assert x == 1
    assert y == 1

def test_knows_it_does_not_need_to_move_to_get_where_it_is():
    x,y = next_tile((1,1),(1,1))
    assert x == 1
    assert y == 1

def test_knows_to_move_north_to_target_tile():
    x, y = next_tile((1,1),(1,2))
    assert x == 1
    assert y == 2

def test_knows_to_move_south_to_target_tile():
    x, y = next_tile((1,1),(1,0))
    assert x == 1
    assert y == 0

def test_knows_to_move_east_to_target_tile():
    x, y = next_tile((1,1),(2,1))
    assert x == 2
    assert y == 1

def test_knows_to_move_west_to_target_tile():
    x, y = next_tile((1,1),(0,1))
    assert x == 0
    assert y == 1

def test_knows_to_take_first_step_toward_target_two_squares_north():
    x, y = next_tile((2,2),(2,4))
    assert x == 2
    assert y == 3

def test_knows_to_take_first_step_toward_target_two_squares_south():
    x, y = next_tile((2,2),(2,0))
    assert x == 2
    assert y == 1

def test_knows_to_take_first_step_toward_target_two_squares_east():
    x, y = next_tile((2,2),(4,2))
    assert x == 3
    assert y == 2

def test_knows_to_take_first_step_toward_target_two_squares_west():
    x, y = next_tile((2,2),(0,2))
    assert x == 1
    assert y == 2

def test_can_move_northeast():
    start = (1, 1)
    target = (3, 3)

    step_one = next_tile(start, target)
    step_two = next_tile(step_one, target)
    step_three = next_tile(step_two, target)
    step_four = next_tile(step_three, target)

    assert step_one == (1, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 3)
    assert step_four == target

def test_can_move_southeast():
    start = (3, 1)
    target = (1, 3)

    step_one = next_tile(start, target)
    step_two = next_tile(step_one, target)
    step_three = next_tile(step_two, target)
    step_four = next_tile(step_three, target)

    assert step_one == (3, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 3)
    assert step_four == target

def test_can_move_southwest():
    start = (3, 3)
    target = (1, 1)

    step_one = next_tile(start, target)
    step_two = next_tile(step_one, target)
    step_three = next_tile(step_two, target)
    step_four = next_tile(step_three, target)

    assert step_one == (3, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 1)
    assert step_four == target

def test_can_move_northwest():
    start = (1, 3)
    target = (3, 1)

    step_one = next_tile(start, target)
    step_two = next_tile(step_one, target)
    step_three = next_tile(step_two, target)
    step_four = next_tile(step_three, target)

    assert step_one == (1, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 1)
    assert step_four == target

def test_knowing_location_and_target_will_determine_direction():
    assert "n" == next_direction((0,1),(0,5))
    assert "s" == next_direction((0,5),(0,1))
    assert "e" == next_direction((1,0),(5,0))
    assert "w" == next_direction((5,0),(1,0))

