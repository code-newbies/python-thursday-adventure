import sys
import pytest
from modules.engine import Engine, tuple_values
from tests.helpers import *

prompt = ">"

# use these constants for testing movement
# aliased from ui fixture in modules/helpers.py
info_ui = ui()
NORTH = info_ui.commands[0]
SOUTH = info_ui.commands[1]
EAST  = info_ui.commands[2]
WEST  = info_ui.commands[3]

def test_can_pass_map_file_to_engine(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("q")
    engine.main_loop()
    assert "test room" == engine.room.name

def test_in_room_returns_false_when_not_in_room(ui):
    ui, engine = init_test_room(ui)
    ui.say("Guido")
    ui.say("q")
    engine.main_loop()
    engine.player.inside = False
    assert not engine.in_room()

def test_in_room_returns_true_when_in_room(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("q")
    engine.main_loop()
    assert engine.in_room()

def test_in_room_returns_false_after_exiting_Room(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(WEST)
    ui.say(WEST)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)

    ui.say("e")
    ui.say("q")
    engine.main_loop()
    assert not engine.in_room()

def test_in_room_returns_false_after_exiting_Room(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("pork belly")

def test_tuple_values_will_return_first_values(ui):
    ui, engine = init_test_room(ui)
    input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
    expected_output = [1, 2, 3]
    output = list(tuple_values(0, input_list))

    for i in list(range(len(expected_output))):
      assert expected_output[i] == output[i]

def test_tuple_values_will_return_second_values(ui):
    ui, engine = init_test_room(ui)
    input_list = [(1, 'a'), (2, 'b'), (3, 'c')]
    expected_output = ['a', 'b', 'c']
    output = list(tuple_values(1, input_list))

    for i in list(range(len(expected_output))):
      assert expected_output[i] == output[i]

def test_engine_will_prompt_and_exit_with_q(ui):
    ui, engine = init_test_room(ui)
    ui.say("Guido")
    ui.say("Q")
    engine.main_loop()
    assert ">" in prompt
    assert ui.output_on_line(prompt, 9)
    # prompt is at index 9, after setting direction keys

def test_engine_commands_are_not_case_sensitive(ui):
    ui, engine = init_test_room(ui)
    ui.say("Guido")
    ui.say("q")
    engine.main_loop()
    assert ">" in prompt
    assert ui.output_on_line(prompt, 9)

def test_invalid_engine_commands_receive_error_message(ui):
    ui, engine = init_test_room(ui)
    ui.say("Guido")
    ui.say("G")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("not valid")
    assert ui.output_anywhere("Please type 'help' and press enter for a menu.")

def test_help_will_be_printed_when_asked_for(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("help")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("quit")
    assert ui.output_anywhere("begin")
    assert ui.output_anywhere("help")
    assert ui.output_anywhere("north")
    assert ui.output_anywhere("south")
    assert ui.output_anywhere("east")
    assert ui.output_anywhere("west")
    assert ui.output_anywhere("exit")
    assert ui.output_anywhere("co-ordinates")

def test_h_moves_player_west(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(WEST)
    ui.say("x")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("(4,6)")

def test_j_moves_player_south(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(SOUTH)
    ui.say("x")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("(5,5)")

def test_k_moves_player_north(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(NORTH)
    ui.say("x")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("(5,7)")

def test_l_moves_player_east(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(EAST)
    ui.say("x")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("(6,6)")

def test_begin_will_start_game(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere(".................")

def test_exit_will_exit_level_at_exit(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(WEST)
    ui.say(WEST)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)
    ui.say(NORTH)

    ui.say("e")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("exited test room")

def test_exit_will_not_exit_level_when_not_at_exit(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say(WEST)
    ui.say("e")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("not at an exit")

def test_that_health_points_display(ui):
    ui, engine = init_test_room(ui)
    ui.say("begin")
    ui.say("test bot")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("Current Health")

def test_alexander_can_enter_a_room_and_travel_to_the_exit(ui):
    ui, engine = init_alexander_room(ui)
    # Alexander, a great fan of text adventures, has entered a new room and seeking fame
    # and glory.  He starts at tile (5,6)
    engine.room_file = "alexander_room.json"
    engine.init_level()
    assert engine.player.locate() == (5,6)

    # Alexander moves north and enters tile (5,7)
    engine.north()
    assert engine.player.locate() == (5,7)

    # Alexander moves east and enters tile (6,7)
    engine.east()
    assert engine.player.locate() == (6,7)

    # Alexander moves north 5 times and enters tile (6, 12)
    engine.north()
    engine.north()
    engine.north()
    engine.north()
    engine.north()
    assert engine.player.locate() == (6,12)

    # Alexander moves west twice and enters tile (4, 12)
    engine.west()
    engine.west()
    assert engine.player.locate() == (4, 12)

    # Alexander moves south 4 times and enters time (4, 8)
    engine.south()
    engine.south()
    engine.south()
    engine.south()
    assert engine.player.locate() == (4, 8)

    # Alexander now shares a tile with the exit and exits the level.
    exit_x, exit_y = engine.level.get_location_by_name("exit")
    player_x, player_y = engine.level.get_location_by_name("player")

    assert exit_x == player_x
    assert exit_y == player_y
    result = engine.exit()
    assert result

# Test moving to the next level
def test_that_room_with_next_level_populates(ui):
    ui, engine = init_tiny_room(ui)
    engine.init_level()
    assert "tiny_room_too.json" in engine.room.next_level

def test_room_will_move_to_next_level_when_enter_next_level_called(p1, ui):
    ui, engine = init_tiny_room(ui)
    engine.init_level()
    engine.room.enter_next_level(p1)
    assert "tiny room too" == engine.room.name

def test_engine_will_move_to_next_level_when_exited(ui):
    ui, engine = init_tiny_room(ui)
    engine.init_level()
    engine.north()
    engine.east()
    engine.exit()
    assert "tiny room too" ==  engine.room.name
    assert engine.in_room()

def test_having_moved_to_the_next_level_the_player_can_move_and_exit_the_following_exit(ui):
    ui, engine = init_tiny_room(ui)
    engine.init_level()
    engine.north()
    engine.east()
    engine.exit()
    engine.north()
    engine.east()
    engine.exit()
    assert "tiny room three" == engine.room.name
    assert engine.in_room()

def test_having_exited_the_final_level_the_player_exits_and_recieved_a_completion_message(ui):
    ui, engine = init_tiny_room(ui)
    engine.init_level()
    engine.north()
    engine.east()
    engine.exit()
    engine.north()
    engine.east()
    engine.exit()
    engine.north()
    engine.east()
    engine.exit()
    assert not engine.room.next_level
    assert not engine.in_room()
    assert ui.output_anywhere("have completed the game")



