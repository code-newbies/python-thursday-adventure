import sys
import pytest
from modules.world import Room, Engine, World
from tests.helpers import fst, tiny_room, item_room

def test_that_room_has_a_name(tiny_room):
    level = tiny_room.enter("entrance")
    assert "tiny room" == tiny_room.name

def test_that_room_with_room_description_has_text(tiny_room):
    level = tiny_room.enter("entrance")
    assert "tiniest of halls" in tiny_room.description
		
def test_that_room_with_exit_description_has_text(tiny_room):
    level = tiny_room.enter("entrance")
    assert "harrowed and tiny halls of doom" in tiny_room.exit_text

def test_that_player_cannot_move_north_through_the_room_boundary(tiny_room):
    level = tiny_room.enter("entrance")
    assert level.go_north("player")
    assert not level.go_north("player")

def test_that_player_cannot_move_south_through_the_room_boundary(tiny_room):
    level = tiny_room.enter("exit")
    assert level.go_south("player")
    assert not level.go_south("player")

def test_that_player_cannot_move_east_through_the_room_boundary(tiny_room):
    level = tiny_room.enter("entrance")
    assert level.go_east("player")
    assert not level.go_east("player")

def test_that_player_cannot_move_west_through_the_room_boundary(tiny_room):
    level = tiny_room.enter("exit")
    assert level.go_west("player")
    assert not level.go_west("player")

def test_can_remove_item_from_map(item_room):
    level = item_room.get_room_data()
    objects = level.get_objects()
    assert "key" in objects
    level.remove("key")
    objects = level.get_objects()
    assert "key" not in objects

def test_player_displays_in_room_as_at(item_room):
    level = item_room.enter("entrance")
    actual = level.draw_map()
    assert "@" in actual 

def test_items_in_map_display(item_room):
    level = item_room.get_room_data()
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        ">...."]
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_player_and_items_in_map_display(item_room):
    expected = [ 
        "....G",
        "$...*",
        "~....",
        "<....",
        "@...."]
    level = item_room.enter("entrance")
    actual = level.draw_map()
    assert "\n".join(expected) == actual  

def test_moved_player_and_items_in_map_display(item_room):
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


