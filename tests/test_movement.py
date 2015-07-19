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

def test_movement_knows_it_does_not_need_to_move_to_get_where_it_is(movement):
    x,y = movement.next_tile((1,1),(1,1))
    assert x == 1
    assert y == 1

def test_movement_knows_to_move_north_to_target_tile(movement):
    x, y = movement.next_tile((1,1),(1,2))
    assert x == 1
    assert y == 2 

def test_movement_knows_to_move_south_to_target_tile(movement):
    x, y = movement.next_tile((1,1),(1,0))
    assert x == 1
    assert y == 0

def test_movement_knows_to_move_east_to_target_tile(movement):
    x, y = movement.next_tile((1,1),(2,1))
    assert x == 2
    assert y == 1

def test_movement_knows_to_move_west_to_target_tile(movement):
    x, y = movement.next_tile((1,1),(0,1))
    assert x == 0
    assert y == 1

def test_movement_knows_to_take_first_step_toward_target_two_squares_north(movement):
    x, y = movement.next_tile((2,2),(2,4))
    assert x == 2
    assert y == 3

def test_movement_knows_to_take_first_step_toward_target_two_squares_south(movement):
    x, y = movement.next_tile((2,2),(2,0))
    assert x == 2
    assert y == 1

def test_movement_knows_to_take_first_step_toward_target_two_squares_east(movement):
    x, y = movement.next_tile((2,2),(4,2))
    assert x == 3
    assert y == 2

def test_movement_knows_to_take_first_step_toward_target_two_squares_west(movement):
    x, y = movement.next_tile((2,2),(0,2))
    assert x == 1
    assert y == 2

def test_movement_can_move_northeast(movement):
    start = (1, 1)
    target = (3, 3)

    step_one = movement.next_tile(start, target)
    step_two = movement.next_tile(step_one, target)
    step_three = movement.next_tile(step_two, target)
    step_four = movement.next_tile(step_three, target)

    assert step_one == (1, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 3)
    assert step_four == target
    
def test_movement_can_move_southeast(movement):
    start = (3, 1)
    target = (1, 3)

    step_one = movement.next_tile(start, target)
    step_two = movement.next_tile(step_one, target)
    step_three = movement.next_tile(step_two, target)
    step_four = movement.next_tile(step_three, target)

    assert step_one == (3, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 3)
    assert step_four == target
    
def test_movement_can_move_southwest(movement):
    start = (3, 3)
    target = (1, 1)

    step_one = movement.next_tile(start, target)
    step_two = movement.next_tile(step_one, target)
    step_three = movement.next_tile(step_two, target)
    step_four = movement.next_tile(step_three, target)

    assert step_one == (3, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 1)
    assert step_four == target
    
def test_movement_can_move_northwest(movement):
    start = (1, 3)
    target = (3, 1)

    step_one = movement.next_tile(start, target)
    step_two = movement.next_tile(step_one, target)
    step_three = movement.next_tile(step_two, target)
    step_four = movement.next_tile(step_three, target)

    assert step_one == (1, 2)
    assert step_two == (2, 2)
    assert step_three == (2, 1)
    assert step_four == target
    
def test_knowing_location_and_target_movement_will_determine_direction(movement):
    assert "n" == movement.next_direction((0,1),(0,5))
    assert "s" == movement.next_direction((0,5),(0,1))
    assert "e" == movement.next_direction((1,0),(5,0))
    assert "w" == movement.next_direction((5,0),(1,0))

