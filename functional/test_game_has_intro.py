import pytest
from tests.helpers import ui, init_item_room

def test_galaxy_man_satisfies_his_need_for_literary_immersion(ui):
    # Galaxy Man tries out the text adventure abd wants to see a 
    # very interesting and immersive introduction to the game
    ui, engine = init_item_room(ui)

    # He starts it up and enters his name when prompted
    ui.say("begin")
    ui.say("Galaxy Man")
    ui.say("q")

    # Then he recieves a really spectacular introduction
    # describing the purpose of the game and includes an
    # indepth view of the game world.
    engine.main_loop()
    assert ui.output_anywhere("pork belly")
    assert ui.output_anywhere("to rescue the big pile of bacon")
    assert ui.output_anywhere("dark and moss covered room")
    assert ui.output_anywhere("with evil")
    assert ui.output_anywhere("the low-sodium cartel")
    
    # Satisfied Galaxy Man tells all his friends about how awesome 
    # the text adventure is

