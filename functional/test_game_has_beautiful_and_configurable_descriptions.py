import pytest
from tests.helpers import ui, init_tiny_room

def test_literary_leslie_loves_lots_of_lively_loquaciousness(ui):
    ui, engine = init_tiny_room(ui)
    engine.room_file = "tiny_room.json"
    # Literary Leslie likes her games to have nice descriptions of things
    # She would like to see life breathed into this text adventure with wonderous words
    
    ui.say("h")
    ui.say("j")
    ui.say("k")
    ui.say("l")

    ui.say("Literary")
    assert not ui.output_anywhere("dark and moss covered")
    # She travels to the exit searching for words 
    ui.say("k")
    ui.say("l")
    ui.say("e")

    # Impressed by the game's literary acumen Leslie quits and writes a 5 star review 
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("dark and moss covered")
