import sys
import pytest
from modules.world import Room, Engine, World
from tests.helpers import BaseTest


class TestTinyRoom(BaseTest):
    def setup_method(self, method):
        self.init()
        room_path = self.build_path(["tests", "fixtures"])
        room_file = "tiny_room.json"
        self.room = Room(room_path, room_file)
        self.level = self.room.get_room_data()

    def test_that_room_has_a_name(self):
        assert "tiny room" == self.room.name

    def test_that_room_with_room_description_has_text(self):
        assert "tiniest of halls" in self.room.description
		
    def test_that_room_with_exit_description_has_text(self):
        assert "harrowed and tiny halls of doom" in self.room.exit_text

class TestEnterAndExitTinyRoom(BaseTest):
    def setup_method(self, method):
        self.init()
        room_path = self.build_path(["tests", "fixtures"])
        room_file = "tiny_room.json"
        self.room = Room(room_path, room_file)

    def test_that_player_cannot_move_north_through_the_room_boundary(self):
        level = self.room.enter("entrance")
        assert level.go_north("player")
        assert not level.go_north("player")

    def test_that_player_cannot_move_south_through_the_room_boundary(self):
        level = self.room.enter("exit")
        assert level.go_south("player")
        assert not level.go_south("player")

    def test_that_player_cannot_move_east_through_the_room_boundary(self):
        level = self.room.enter("entrance")
        assert level.go_east("player")
        assert not level.go_east("player")

    def test_that_player_cannot_move_west_through_the_room_boundary(self):
        level = self.room.enter("exit")
        assert level.go_west("player")
        assert not level.go_west("player")

class TestRoomCanHaveItemsRemoved(BaseTest):
    def setup_method(self, method):
        self.init()
        room_path = self.build_path(["tests", "fixtures"])
        room_file = "item_room.json"
        self.room = Room(room_path, room_file)
        self.level = self.room.get_room_data()

    def test_can_remove_item_from_map(self):
        objects = self.level.get_objects()
        assert "key" in objects
        self.level.remove("key")
        objects = self.level.get_objects()
        assert "key" not in objects

class TestMapDrawsAllItemsInRoom(BaseTest):
    def setup_method(self, method):
        self.init()
        room_path = self.build_path(["tests", "fixtures"])
        room_file = "item_room.json"
        self.room = Room(room_path, room_file)
        self.level = self.room.get_room_data()

    def test_player_displays_in_room_as_at(self):
        level = self.room.enter("entrance")
        actual = level.draw_map()
        assert "@" in actual 

    def test_items_in_map_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            ">...."]
        actual = self.level.draw_map()
        assert "\n".join(expected) == actual  

    def test_player_and_items_in_map_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            "@...."]
        level = self.room.enter("entrance")
        actual =level.draw_map()
        assert "\n".join(expected) == actual  

    def test_moved_player_and_items_in_map_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            ">@..."]
        level = self.room.enter("entrance")
        level.go_east("player")
        actual = level.draw_map()
        assert "\n".join(expected) == actual


