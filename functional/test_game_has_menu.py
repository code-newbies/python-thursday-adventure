import pytest
from tests.helpers import ui, load_test_room

def test_linus_sees_quit_begin_and_help_in_menu_but_no_other_commands_before_entering_a_room(ui):
    # Linus plays the game for the first time, he has never seen a game like this
    # He wants to use the help menu heavily and try all of the commands he can.
    # He doesn't want any commands that aren't valid for teh state of the game. 
    # For instance he doesn't want to move his character when  he isn't in a room
    # He still wants to be able to start a game, quit and of course get help
    ui, engine = load_test_room(ui)
    ui.say("help")
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("help -")
    assert ui.output_anywhere("q -")
    assert ui.output_anywhere("begin -")
    assert not ui.output_anywhere("h -")
    assert not ui.output_anywhere("j -")
    assert not ui.output_anywhere("k -")
    assert not ui.output_anywhere("l -")
    assert not ui.output_anywhere("x -")

