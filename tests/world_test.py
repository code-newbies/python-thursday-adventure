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
        
        actual = self.room.build_map()
        self.assertEqual("\n".join(expected), actual)  

class RoomDrawsAllItemsInRoomTest(BaseTest):
    def setUp(self):
        self.init()
        self.old_max_diff = self.maxDiff
        self.maxDiff = None
        room_path = self.build_path(["tests", "fixtures", "item_room.json"])
        self.room = Room(room_path)
        self.room.get_room_data()

    def tearDown(self):
        self.maxDiff = self.old_max_diff

    def test_player_displays_in_room_as_at(self):
        self.room.enter("entrance")
        actual = self.room.build_map()
        self.assertIn("@", actual)  

    def test_items_in_room_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            ">...."]
        actual = self.room.build_map()
        self.assertEqual("\n".join(expected), actual)  

    def test_player_and_items_in_room_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            "@...."]
        self.room.enter("entrance")
        actual = self.room.build_map()
        self.assertEqual("\n".join(expected), actual)  

    def test_moved_player_and_items_in_room_display(self):
        expected = [ 
            "....G",
            "$...*",
            "~....",
            "<....",
            ">@..."]
        self.room.enter("entrance")
        self.room.east("player")
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

    def load_test_room(self):
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)
        map_path = self.engine.get_rel_path(["tests", "fixtures", "test_room.json"])
        self.engine.set_map(map_path)

    def test_can_pass_map_file_to_engine(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        self.assertEqual("test room", self.engine.room.name)

    def test_in_room_returns_false_when_not_in_room(self):
        self.load_test_room()
        self.say("q")
        self.engine.main_loop()
        self.assertFalse(self.engine.in_room())

    def test_in_room_returns_true_when_in_room(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        self.assertTrue(self.engine.in_room())

    def test_in_room_returns_false_after_exiting_Room(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("h")
        self.say("h")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")

        self.say("e")
        self.say("q")
        self.engine.main_loop()
        self.assertFalse(self.engine.in_room())

    def test_engine_enters_main_loop(self):
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)
        try:
            self.say("Q")
            self.engine.main_loop()
        except AttributeError:
            self.fail("Engine does not have a main_loop() method")

class EngineHelperTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)

    def test_tuple_values_will_return_first_values(self):
        input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = [1, 2, 3]
        output = list(self.engine.tuple_values(0, input_list))

        for i in list(range(len(expected_output))):
           self.assertEqual(expected_output[i], output[i])

    def test_tuple_values_will_return_second_values(self):
        input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = ['a', 'b', 'c']
        output = list(self.engine.tuple_values(1, input_list))

        for i in list(range(len(expected_output))):
           self.assertEqual(expected_output[i], output[i])

class EngineMenuAndCommandTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)
        map_path = self.engine.get_rel_path(["tests", "fixtures", "test_room.json"])
        self.engine.set_map(map_path)

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

    def test_invalid_engine_commands_receive_error_message(self):
        self.say("&")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("not valid, please type 'help' and press enter for a menu.")

    def test_help_will_be_printed_when_asked_for(self):
        self.say("begin")
        self.say("test bot")
        self.say("help")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("quit")
        self.assertPrintedOnAnyLine("begin")
        self.assertPrintedOnAnyLine("help")
        self.assertPrintedOnAnyLine("north")
        self.assertPrintedOnAnyLine("south")
        self.assertPrintedOnAnyLine("east")
        self.assertPrintedOnAnyLine("west")
        self.assertPrintedOnAnyLine("exit")
        self.assertPrintedOnAnyLine("co-ordinates")

    def test_h_moves_player_west(self):
        self.say("begin")
        self.say("test bot")
        self.say("h")
        self.say("x")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("(4,6)")

    def test_j_moves_player_south(self):
        self.say("begin")
        self.say("test bot")
        self.say("j")
        self.say("x")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("(5,5)")

    def test_k_moves_player_north(self):
        self.say("begin")
        self.say("test bot")
        self.say("k")
        self.say("x")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("(5,7)")

    def test_l_moves_player_east(self):
        self.say("begin")
        self.say("test bot")
        self.say("l")
        self.say("x")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("(6,6)")

    def test_begin_will_start_game(self):
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine(".................")

    def test_exit_will_exit_level_at_exit(self):
        self.say("begin")
        self.say("test bot")
        self.say("h")
        self.say("h")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")

        self.say("e")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("exited test room")

    def test_exit_will_not_exit_level_when_not_at_exit(self):
        self.say("begin")
        self.say("test bot")
        self.say("h")
        self.say("e")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("cannot exit test room because you are not at an exit")

class PlayerCanMoveTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)

    def test_alexander_can_enter_a_room_and_travel_to_the_exit(self):
        # Alexander, a great fan of text adventures, has entered a new room and seeking fame
        # and glory.  He starts at tile (5,6)
        alexander_test_room = self.build_path(["tests","fixtures", "alexander_room.json"])
        self.engine.init_level(alexander_test_room)
        self.assertLocation(self.engine.room, 'player', 5,6)

        # Alexander moves north and enters tile (5,7)
        self.engine.north()
        self.assertLocation(self.engine.room, 'player', 5,7)

        # Alexander moves east and enters tile (6,7)
        self.engine.east()
        self.assertLocation(self.engine.room, 'player', 6,7)

        # Alexander moves north 5 times and enters tile (6, 12)
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.assertLocation(self.engine.room, 'player', 6,12)

        # Alexander moves west twice and enters tile (4, 12)
        self.engine.west()
        self.engine.west()
        self.assertLocation(self.engine.room, 'player', 4, 12)

        # Alexander moves south 4 times and enters time (4, 8)
        self.engine.south()
        self.engine.south()
        self.engine.south()
        self.engine.south()
        self.assertLocation(self.engine.room, 'player', 4, 8)

        # Alexander now shares a tile with the exit and exits the level.
        exit_x, exit_y = self.engine.room.locate("exit")
        player_x, player_y = self.engine.room.locate("player")

        self.assertEqual(exit_x, player_x)
        self.assertEqual(exit_y, player_y)
        result = self.engine.exit()
        self.assertTrue(result)
