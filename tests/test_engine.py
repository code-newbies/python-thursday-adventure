import sys
import pytest
from modules.world import Engine
from tests.helpers import BaseTest

prompt = ">"

class TestEngineInit(BaseTest):
    def setUp(self):
        self.init()

    def load_test_room(self):
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)
        self.engine.room_file = "test_room.json"

    def test_can_pass_map_file_to_engine(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        assert "test room" = self.engine.room.name

    def test_in_room_returns_false_when_not_in_room(self):
        self.load_test_room()
        self.say("q")
        self.engine.main_loop()
        assert not self.engine.in_room()

    def test_in_room_returns_true_when_in_room(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        assert self.engine.in_room()

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
        assert not self.engine.in_room()

    def test_in_room_returns_false_after_exiting_Room(self):
        self.load_test_room()
        self.say("begin")
        self.say("test bot")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("pork belly")

class TestEngineHelper(BaseTest):
    def setup_method(self, method):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_tuple_values_will_return_first_values(self):
        input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = [1, 2, 3]
        output = list(self.engine.tuple_values(0, input_list))

        for i in list(range(len(expected_output))):
           assert expected_output[i] == output[i]

    def test_tuple_values_will_return_second_values(self):
        input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
        expected_output = ['a', 'b', 'c']
        output = list(self.engine.tuple_values(1, input_list))

        for i in list(range(len(expected_output))):
           assert expected_output[i] == output[i]

class TestEngineMenuAndCommand(BaseTest):
    def setup_method(self, method):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)
        self.engine.room_file = "test_room.json"

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

class TestPlayerCanMove(BaseTest):
    def setup_method(self, method):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_alexander_can_enter_a_room_and_travel_to_the_exit(self):
        # Alexander, a great fan of text adventures, has entered a new room and seeking fame
        # and glory.  He starts at tile (5,6)
        self.engine.room_file = "alexander_room.json"
        self.engine.init_level()
        self.assertLocation(self.engine.level, 'player', 5,6)

        # Alexander moves north and enters tile (5,7)
        self.engine.north()
        self.assertLocation(self.engine.level, 'player', 5,7)

        # Alexander moves east and enters tile (6,7)
        self.engine.east()
        self.assertLocation(self.engine.level, 'player', 6,7)

        # Alexander moves north 5 times and enters tile (6, 12)
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.engine.north()
        self.assertLocation(self.engine.level, 'player', 6,12)

        # Alexander moves west twice and enters tile (4, 12)
        self.engine.west()
        self.engine.west()
        self.assertLocation(self.engine.level, 'player', 4, 12)

        # Alexander moves south 4 times and enters time (4, 8)
        self.engine.south()
        self.engine.south()
        self.engine.south()
        self.engine.south()
        self.assertLocation(self.engine.level, 'player', 4, 8)

        # Alexander now shares a tile with the exit and exits the level.
        exit_x, exit_y = self.engine.level.locate("exit")
        player_x, player_y = self.engine.level.locate("player")

        self.assertEqual(exit_x, player_x)
        self.assertEqual(exit_y, player_y)
        result = self.engine.exit()
        assert result

class TestEngineLeveling(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)
        self.engine.room_file = "tiny_room.json"
        self.engine.init_level()

    def test_that_room_with_next_level_populates(self):
        assert "tiny_room_too.json" in self.engine.room.next_level

    def test_room_will_move_to_next_level_when_enter_next_level_called(self):
        self.engine.room.enter_next_level()
        assert "tiny room too" == self.engine.room.name

    def test_engine_will_move_to_next_level_when_exited(self):
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        assert "tiny room too" ==  self.engine.room.name
        assert self.engine.in_room()

    def test_having_moved_to_the_next_level_the_player_can_move_and_exit_the_following_exit(self):
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        assert tiny room three == self.engine.room.name
        assert self.engine.in_room()

    def test_having_exited_the_final_level_the_player_exits_and_recieved_a_completion_message(self):
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        self.engine.north()
        self.engine.east()
        self.engine.exit()
        assert self.engine.room.next_level
        assert not self.engine.in_room()
        self.assertPrintedOnAnyLine("have completed the game")



