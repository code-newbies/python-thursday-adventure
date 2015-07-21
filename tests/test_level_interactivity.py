import sys
import pytest
from modules.world import LevelLoader
from tests.helpers import ui, at_location, test_room, fst, tiny_room, item_room, roach_room, locations

# These tests combine Level and LevelLoader functionality and aren't true unit tests, but they 
# were at one time whent this functionality was in a single class.  Separating to allow new 
# unit tests for Level and LevelLoader to take shape uncluttered.

def test_that_level_can_list_locations_in_it(test_room):
    level = test_room.get_room_data()
    objects = level.get_objects()
    assert "entrance" in objects
    
def test_that_level_can_return_items_at_location(test_room):
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

def test_that_level_will_print(test_room):
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

def test_that_level_has_a_name(tiny_room):
    level = tiny_room.enter("entrance")
    assert "tiny room" == tiny_room.name

def test_that_level_with_room_description_has_text(tiny_room):
    level = tiny_room.enter("entrance")
    assert "tiniest of halls" in tiny_room.description
		
def test_that_level_with_exit_description_has_text(tiny_room):
    level = tiny_room.enter("entrance")
    assert "harrowed and tiny halls of doom" in tiny_room.exit_text

def test_that_player_cannot_move_north_through_the_level_boundary(tiny_room):
    level = tiny_room.enter("entrance")
    assert level.go_north("player")
    assert not level.go_north("player")

def test_that_player_cannot_move_south_through_the_level_boundary(tiny_room):
    level = tiny_room.enter("exit")
    assert level.go_south("player")
    assert not level.go_south("player")

def test_that_player_cannot_move_east_through_the_level_boundary(tiny_room):
    level = tiny_room.enter("entrance")
    assert level.go_east("player")
    assert not level.go_east("player")

def test_that_player_cannot_move_west_through_the_level_boundary(tiny_room):
    level = tiny_room.enter("exit")
    assert level.go_west("player")
    assert not level.go_west("player")

def test_can_remove_item_from_level(item_room):
    level = item_room.get_room_data()
    objects = level.get_objects()
    assert "key" in objects
    level.remove("key")
    objects = level.get_objects()
    assert "key" not in objects

def test_player_displays_in_level_as_at(item_room):
    level = item_room.enter("entrance")
    actual = level.draw_map()
    assert "@" in actual 

def test_items_in_level_display(item_room):
    level = item_room.get_room_data()
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        ">...."]
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_player_and_items_in_level_display(item_room):
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        "@...."]
    level = item_room.enter("entrance")
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_moved_player_and_items_in_level_display(item_room):
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        ">@..."]
    level = item_room.enter("entrance")
    level.go_east("player")
    actual = level.draw_map()
    assert "\n".join(expected) == actual

def test_creature_is_drawn_on_level(roach_room):
    expected = [ 
        "......",
        "......",
        "@.....",
        "......",
        "......",
        "<....r"]
    level = roach_room.enter("entrance")
    actual = level.draw_map()
    assert "\n".join(expected) == actual



