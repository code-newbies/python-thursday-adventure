import pytest
from tests.helpers import ui, init_tiny_room

def travel_to_the_next_level(ui):
    # She travels to the next level
    ui.say("i")
    ui.say("l")
    ui.say("e")

def test_power_leveling_paula_delves_deeply(ui):
    ui, engine = init_tiny_room(ui)
    # Power leveling Paula likes to get through a game as quickly as possible.
    # She will be overjoyed to travel through three levels to complete the game as quickly 
    # as possible
    ui.say("Paula")

    travel_to_the_next_level(ui)
    travel_to_the_next_level(ui)
    travel_to_the_next_level(ui)
    
    # Impressed by the game's literary acumen Leslie quits and writes a 5 star review 
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("harrowed and tiny halls of doom")
    assert ui.output_anywhere("second of three tiny rooms")
    assert ui.output_anywhere("third and final tiny room")

    assert ui.output_anywhere("completed the game")

