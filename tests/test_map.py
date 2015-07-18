import sys
import pytest
from modules.world import Room
from tests.helpers import ui, at_location, build_path

class TestMap:
    def setup_method(self, method):
        room_path = build_path(["tests", "fixtures"])
        room_file = "test_room.json"
        self.room = Room(room_path, room_file)
        self.level = self.room.get_room_data()

    def test_that_map_has_a_size(self):
        assert 18 == self.level.size

    def test_that_map_can_list_locations_in_it(self):
        objects = self.level.get_objects()
        assert "entrance" in objects
    
    def test_that_map_can_return_items_at_location(self):
        items = self.level.items(5,6)
        assert "entrance" in items

        items = self.level.items(3,12)
        assert "exit" in items

        items = self.level.items(1,1)
        assert 0 == len(items)

    def test_that_entrance_location_can_be_loaded_from_file(self):
        x,y = self.level.locate("entrance")
        assert 5 == x
        assert 6 == y

    def test_that_room_will_print(self):
        self.maxDiff = None

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
        
        actual = self.level.draw_map()
        assert "\n".join(expected) == actual  

class TestMapMovement:
    def setup_method(self, method):
        room_path = build_path(["tests", "fixtures"])
        room_file = "test_room.json"
        self.room = Room(room_path, room_file)

    def test_that_player_can_be_located(self):
        level = self.room.enter("entrance")
        x,y = level.locate("player")
        assert 5 == x
        assert 6 == y

    def test_that_player_enters_at_location(self):
        level = self.room.enter("exit")
        x,y = level.locate("player")
        assert 3 == x
        assert 12 == y

    def test_that_player_can_move_north(self):
        level = self.room.enter("entrance")
        level.go_north("player")
        assert at_location(level, "player", 5, 7)        

    def test_that_player_can_move_south(self):
        level = self.room.enter("entrance")
        level.go_south("player")
        assert at_location(level, "player", 5, 5)        

    def test_that_player_can_move_east(self):
        level = self.room.enter("entrance")
        level.go_east("player")
        assert at_location(level, "player", 6, 6)        

    def test_that_player_can_move_west(self):
        level = self.room.enter("entrance")
        level.go_west("player")
        assert at_location(level, "player", 4, 6)        

    def test_that_player_can_exit(self):
        level = self.room.enter("exit")
        assert level.exit()

    def test_that_player_cannot_exit_from_entrance(self):
        level = self.room.enter("entrance")
        assert not level.exit()

    def test_that_player_can_enter_room(self):
        level = self.room.enter("entrance")
        objects = level.get_objects()
        assert "player" in objects

