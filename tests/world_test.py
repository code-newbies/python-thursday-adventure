import sys
import unittest
from modules.world import Room, Engine
from modules.player import Player
from tests.helpers import BaseTest

prompt = ">"

class RoomTest(BaseTest):
    def setUp(self):
        self.init()
        self.old_max_diff = self.maxDiff
        room_path = self.build_path(["tests", "fixtures", "test_room.json"])
        self.room = Room(room_path)
        self.room.get_room_data()

    def tearDown(self):
        self.maxDiff = self.old_max_diff

    def test_that_room_has_a_name(self):
        self.assertEqual("test room", self.room.name)

    def test_that_room_has_a_size(self):
        self.assertEqual(18, self.room.size)

    def test_that_room_can_list_locations_in_it(self):
        objects = self.room.get_objects()
        self.assertIn("entrance", objects)
    
    def test_that_room_can_return_items_at_location(self):
        items = self.room.items(5,6)
        self.assertIn("entrance", items)

        items = self.room.items(3,12)
        self.assertIn("exit", items)

        items = self.room.items(1,1)
        self.assertEqual(0, len(items))

    def test_that_entrance_location_can_be_loaded_from_file(self):
        x,y = self.room.locate("entrance")
        self.assertEqual(5, x)
        self.assertEqual(6, y)

    def test_that_player_can_enter_room(self):
        self.room.enter("entrance")
        objects = self.room.get_objects()
        self.assertIn("player", objects)

    def test_that_player_can_be_located(self):
        self.room.enter("entrance")
        x,y = self.room.locate("player")
        self.assertEqual(5, x)
        self.assertEqual(6, y)

    def test_that_player_enters_at_location(self):
        self.room.enter("exit")
        x,y = self.room.locate("player")
        self.assertEqual(3, x)
        self.assertEqual(12, y)

    def test_that_player_can_move_north(self):
        self.room.enter("entrance")
        self.room.north("player")
        self.assertLocation(self.room, "player", 5, 7)        

    def test_that_player_can_move_south(self):
        self.room.enter("entrance")
        self.room.south("player")
        self.assertLocation(self.room, "player", 5, 5)        

    def test_that_player_can_move_east(self):
        self.room.enter("entrance")
        self.room.east("player")
        self.assertLocation(self.room, "player", 6, 6)        

    def test_that_player_can_move_west(self):
        self.room.enter("entrance")
        self.room.west("player")
        self.assertLocation(self.room, "player", 4, 6)        

    def test_that_player_can_exit(self):
        self.room.enter("exit")
        self.assertTrue(self.room.exit())

    def test_that_player_cannot_exit_from_entrance(self):
        self.room.enter("entrance")
        self.assertFalse(self.room.exit())

    def test_that_room_will_print(self):
        self.maxDiff = None

        expected = [ 
            "..................",
            "..................",
            "..................",
            "............<.....",
            "..................",
            "......>...........",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            "..................",
            ".................."]
        
        actual = self.room.build_map()
        self.assertEqual("\n".join(expected), actual)  

class EngineInitTest(BaseTest):
    def setUp(self):
        self.init()

    def test_engine_accepts_base_path(self):
        self.engine = Engine('foo', self.fake_input, self.fake_print)
        rel_path = self.engine.get_rel_path('bar.baz')
        self.assertIn('foo', rel_path)
        self.assertIn('bar.baz', rel_path)

    def test_rel_path_builds_path_from_list(self):
        path = ['a','quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
        self.engine = Engine('foo', self.fake_input, self.fake_print)
        rel_path = self.engine.get_rel_path(path)
        self.assertIn('foo', rel_path)
        for location in path:
            self.assertIn(location, rel_path)

    def test_engine_enters_main_loop(self):
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)
        try:
            self.say("Q")
            self.engine.main_loop()
        except AttributeError:
            self.fail("Engine does not have a main_loop() method")


class EngineTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)

    def test_engine_will_prompt_and_exit_with_q(self):
        self.say("Q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)

    def test_engine_commands_are_not_case_sensitive(self):
        self.say("q")
        self.engine.main_loop()
        self.assertIn(prompt, ">")
        self.assertPrinted(prompt, 0)

    def test_help_will_be_printed_when_asked_for(self):
        self.say("help")
        self.say("q")
        self.engine.main_loop()
        self.assertPrinted("help", 1)


