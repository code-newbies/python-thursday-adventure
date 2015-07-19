import pytest
from tests.helpers import ui, init_tiny_room


def test_ghastly_cannot_travel_through_room_boundaries(ui):
    ui, engine = init_tiny_room(ui)
    # Ghastly thinks that he can travel though wall and room boundaries
    # as it turns out, he cannot, but that won't stop him from trying.
    # He will try to walk through all 4 room boundaries of the 2 x 2 room.
    ui.say("begin")
    ui.say("Ghastly")
    
    # He starts in tile 0,0 and tries to go west through a wall
    ui.say("h")

    # Then he tries to go south through a wall
    ui.say("j")

    # These walls are solid and prevent me from travelling there.  So he travels north twice.
    # The second movement is prevented by a wall
    ui.say("k")
    ui.say("k")

    # Now he tries the last wall by travelling east twice.  But cannot travel through the east wall
    ui.say("l")
    ui.say("l")

    # Completely frustrated, Ghastly exits the level.
    ui.say("e")

    # Having seen all there is to see, he quits the game and tells all of his friends about
    # the cool map.
    ui.say("q")
    engine.main_loop()
    assert ui.output_anywhere("You cannot go north")
    assert ui.output_anywhere("You cannot go south")
    assert ui.output_anywhere("You cannot go east")
    assert ui.output_anywhere("You cannot go west")

