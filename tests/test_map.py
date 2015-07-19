import sys
import pytest
from modules.world import Room
from tests.helpers import ui, at_location, test_room

def test_that_map_can_list_locations_in_it(test_room):
    level = test_room.get_room_data()
    objects = level.get_objects()
    assert "entrance" in objects
    
def test_that_map_can_return_items_at_location(test_room):
    level = test_room.get_room_data()
    items = level.items(5,6)
    assert "entrance" in items

    items = level.items(3,12)
    assert "exit" in items

    items = level.items(1,1)
    assert 0 == len(items)

def test_that_entrance_location_can_be_loaded_from_file(test_room):
    level = test_room.get_room_data()
    x,y = level.locate("entrance")
    assert 5 == x
    assert 6 == y

def test_that_room_will_print(test_room):
    level = test_room.get_room_data()

    expected = [ 
        "..................",
        "..................",
        "..................",
        "..................",
        "..................",
        "...<..............",
        "..................",
        "..................",
        "..................",
        "..................",
        "..................",
        ".....>............",
        "..................",
        "..................",
        "..................",
        "..................",
        "..................",
        ".................."]
    
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_that_player_can_be_located(test_room):
    level = test_room.enter("entrance")
    x,y = level.locate("player")
    assert 5 == x
    assert 6 == y

def test_that_player_enters_at_location(test_room):
    level = test_room.enter("exit")
    x,y = level.locate("player")
    assert 3 == x
    assert 12 == y

def test_that_player_can_move_north(test_room):
    level = test_room.enter("entrance")
    level.go_north("player")
    assert at_location(level, "player", 5, 7)        

def test_that_player_can_move_south(test_room):
    level = test_room.enter("entrance")
    level.go_south("player")
    assert at_location(level, "player", 5, 5)        

def test_that_player_can_move_east(test_room):
    level = test_room.enter("entrance")
    level.go_east("player")
    assert at_location(level, "player", 6, 6)        

def test_that_player_can_move_west(test_room):
    level = test_room.enter("entrance")
    level.go_west("player")
    assert at_location(level, "player", 4, 6)        

def test_that_player_can_exit(test_room):
    level = test_room.enter("exit")
    assert level.exit()

def test_that_player_cannot_exit_from_entrance(test_room):
    level = test_room.enter("entrance")
    assert not level.exit()

def test_that_player_can_enter_room(test_room):
    level = test_room.enter("entrance")
    objects = level.get_objects()
    assert "player" in objects

