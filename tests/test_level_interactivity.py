import sys
import pytest
from modules.level_loader import LevelLoader
from tests.helpers import ui, test_room, fst, tiny_room, item_room, roach_room, locations, p1

# These tests combine Level and LevelLoader functionality and aren't true unit tests, but they 
# were at one time whent this functionality was in a single class.  Separating to allow new 
# unit tests for Level and LevelLoader to take shape uncluttered.

def test_that_level_can_return_items_at_location(test_room):
    level = test_room.get_room_data()
    items = level.contents_at_coords((5,6))
    assert items[0].name == "entrance"

    items = level.contents_at_coords((3,12))
    assert items[0].name == "exit"

    items = level.contents_at_coords((0,0))
    assert 0 == len(items)

def test_that_entrance_location_can_be_loaded_from_file(test_room):
    level = test_room.get_room_data()
    entrance = level.get_by_name("entrance")
    coords = entrance.locate()
    assert 5 == coords[0]
    assert 6 == coords[1]

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

def test_that_player_can_be_located(p1, test_room):
    level = test_room.enter(p1, "entrance")
    player = level.get_by_name("player")
    coords = player.locate()
    assert 5 == coords[0]
    assert 6 == coords[1]

def test_that_player_enters_at_location(p1, test_room):
    level = test_room.enter(p1, "exit")
    player = level.get_by_name("player")
    coords = player.locate()
    assert 3 == coords[0]
    assert 12 == coords[1]

def test_that_player_can_move_north(p1, test_room):
    level = test_room.enter(p1, "entrance")
    p1.travel("n")
    coords = p1.locate()
    assert 5 == coords[0]
    assert 7 == coords[1]

def test_that_player_can_move_south(p1, test_room):
    level = test_room.enter(p1, "entrance")
    p1.travel("s")
    coords = p1.locate()
    assert 5 == coords[0]
    assert 5 == coords[1]

def test_that_player_can_move_east(p1, test_room):
    level = test_room.enter(p1, "entrance")
    p1.travel("e")
    coords = p1.locate()
    assert 6 == coords[0]
    assert 6 == coords[1]

def test_that_player_can_move_west(p1, test_room):
    level = test_room.enter(p1, "entrance")
    p1.travel("w")
    coords = p1.locate()
    assert 4 == coords[0]
    assert 6 == coords[1]

def test_that_player_can_exit(p1, test_room):
    level = test_room.enter(p1, "exit")
    assert level.exit(p1)

def test_that_player_cannot_exit_from_entrance(p1, test_room):
    level = test_room.enter(p1, "entrance")
    assert not level.exit(p1)

def test_that_player_can_enter_room(p1, test_room):
    assert not p1.in_room()
    level = test_room.enter(p1, "entrance")
    assert p1.in_room()

def test_that_level_has_a_name(p1, tiny_room):
    level = tiny_room.enter(p1, "entrance")
    assert "tiny room" == tiny_room.name

def test_that_level_with_room_description_has_text(p1, tiny_room):
    level = tiny_room.enter(p1, "entrance")
    assert "tiniest of halls" in tiny_room.description
		
def test_that_level_with_exit_description_has_text(p1, tiny_room):
    level = tiny_room.enter(p1, "entrance")
    assert "harrowed and tiny halls of doom" in tiny_room.exit_text

def test_that_player_cannot_move_north_through_the_level_boundary(p1, tiny_room):
    level = tiny_room.enter(p1, "entrance")
    assert level.can_go_north(p1)
    p1.travel("n")
    assert not level.can_go_north(p1)

def test_that_player_cannot_move_south_through_the_level_boundary(p1, tiny_room):
    level = tiny_room.enter(p1, "exit")
    assert level.can_go_south(p1)
    p1.travel("s")
    assert not level.can_go_south(p1)

def test_that_player_cannot_move_east_through_the_level_boundary(p1, tiny_room):
    level = tiny_room.enter(p1, "entrance")
    assert level.can_go_east(p1)
    p1.travel("e")
    assert not level.can_go_east(p1)

def test_that_player_cannot_move_west_through_the_level_boundary(p1, tiny_room):
    level = tiny_room.enter(p1, "exit")
    assert level.can_go_west(p1)
    p1.travel("w")
    assert not level.can_go_west(p1)

def test_can_remove_item_from_level(p1, item_room):
    level = item_room.enter(p1, "entrance")
    key = level.get_by_name("key")
    assert key.name == "key"
    level.remove("key")
    assert level.get_by_name("key") == None

def test_player_displays_in_level_as_at(p1, item_room):
    level = item_room.enter(p1, "entrance")
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

def test_player_and_items_in_level_display(p1, item_room):
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        "@...."]
    level = item_room.enter(p1, "entrance")
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_moved_player_and_items_in_level_display(p1, item_room):
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        ">@..."]
    level = item_room.enter(p1, "entrance")
    p1.travel("e")
    actual = level.draw_map()
    assert "\n".join(expected) == actual

def test_creature_is_drawn_on_level(p1, roach_room):
    expected = [ 
        "......",
        "......",
        "@.....",
        "......",
        "......",
        "<....r"]
    level = roach_room.enter(p1, "entrance")
    actual = level.draw_map()
    assert "\n".join(expected) == actual



