import pytest
from tests.helpers import *

def test_ian_inventory_can_see_all_items_on_map(ui):
    ui, engine = load_item_room(ui)
    # Ian walks into a room filled with lots of stuff and he wants to see the map
    # Ian wants to know all of the stuff in the room and definately wants to see everything
    # on the map
    # He types begin and enters the game
    ui.say("begin")
    ui.say("Ian")
    
    # The map displays all items in the room.  Ian sees the exit is one square south.
    # He moves there and exits
    ui.say("k")
    ui.say("e")

    # Having seen all there is to see, he quits the game and tells all of his friends about
    # the cool map.
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("....G")
    assert ui.output_anywhere("$...*")
    assert ui.output_anywhere("~....")
    assert ui.output_anywhere("<....")
    assert ui.output_anywhere("@....")

