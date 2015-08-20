import pytest
from tests.helpers import ui, init_test_room

def test_fred_can_start_and_stop_the_loop_with_ease(ui):
    ui, engine = init_test_room(ui)
    # Fred is an avid gamer, some would say that he is a compulsive gamer
    # It has gotten so bad that he games in the middle of the night, when he should be sleeping
    # He games in the day at work.
    # Sometimes he games when he should be mowing the lawn.
    # Today Fred is trying a new CodeNewbie text adventure game he found, he starts it up
    # As soon as he gets the prompt of the main loop his boss walks by
    # In a panic Fred presses "Q" to quit.
    ui.say("Fred")
    ui.say("Q")
    engine.main_loop()

    # The text adventure ends 
    assert ui.output_anywhere(">")

def test_fred_can_stop_the_loop_with_lower_case_q(ui):
    ui, engine = init_test_room(ui)
    # Fred when closing the game as quickly as possible doesn't have time to press shift 
    # He sends a lower case 'q' instead
    # The game closes anyway
    ui.say("Fred")
    ui.say("q")
    engine.main_loop()

    # The text adventure ends 
    assert ui.output_anywhere(">")

def test_jaime_can_get_help(ui):
    ui, engine = init_test_room(ui)
    # Jamie has heard from Fred that this new Python powered CodeNewbie text adventure game
    # is not only the cause of his loss of job and sleep, but is also relitively easy for
    # beginners to enjoy because the help functionality is so easy to use.  All she needs to
    # do to check the help is start the main loop.
    # Type 'help' and press enter.
    ui.say("Jaime")
    ui.say("help")
    ui.say("q")
    engine.main_loop()

    # A list of commands will display
    # Jamie can then quit the game and tell her friends all the ease of use.
    print(ui.printed)
    assert ui.output_anywhere("help")
