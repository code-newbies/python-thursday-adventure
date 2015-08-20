import pytest
from tests.helpers import ui, init_roach_room

def test_roach_runs_to_the_exit(ui):
    # Jimmy steps into the room and turns on the light
    ui, engine = init_roach_room(ui)

    ui.say("Jimmy")
    # He needs to walk through this kitchen to the dark hallway beyond.  In the corner of 
    # his eye he sees a cockroach off in the far corner
    ui.say("k")

    # After making a move towards the door, he notices that the cockroach has moved toward
    # the door as well
    ui.say("k")

    # Feeling a bit preturbed he takes another step towards the exit, the cockroach 
    # trying hard to avoid the light is running full speed toward the exit as well
    ui.say("k")

    # Jimmy makes it to the doorway and exits the room.  He happily shuts off the light and
    # walks down the dark hallway.
    ui.say("e")
    ui.say("q")

    engine.main_loop()
    assert ui.output_anywhere("turn on the light")
    turn_one = ui.output_index("<....r")
    turn_two = ui.output_index("<...r.")
    turn_three = ui.output_index("<..r..")
    turn_four = ui.output_index("@.r...")
    assert turn_one < turn_two
    assert turn_two < turn_three
    assert turn_three < turn_four
