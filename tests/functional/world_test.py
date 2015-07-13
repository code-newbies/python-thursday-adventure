import sys
import unittest
from tests.helpers import BaseTest
from modules.world import Room, Engine
from os import getcwd
from os.path import join

class CanReadStdOutAndMockPrompt(BaseTest):
    def setUp(self):
        self.init()

    def test_can_get_output_from_stdout_and_input_to_stdin(self):
        self.say("Hero")
        engine = Engine(self.library_path, self.fake_input, self.fake_print)
        engine.greet()
        self.assertEqual("Hello, what is your name: ", self.printed[0])
        self.assertEqual("Welcome to text adventure, Hero!", self.printed[1])
        
class CanLoopTheMainLoop(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)
    
    def test_fred_can_start_and_stop_the_loop_with_ease(self):
        # Fred is an avid gamer, some would say that he is a compulsive gamer
        # It has gotten so bad that he games in the middle of the night, when he should be sleeping
        # He games in the day at work.
        # Sometimes he games when he should be mowing the lawn.
        # Today Fred is trying a new CodeNewbie text adventure game he found, he starts it up
        # As soon as he gets the prompt of the main loop his boss walks by
        # In a panic Fred presses "Q" to quit.
        self.say("Q")
        self.engine.main_loop()
        
        # The text adventure ends 
        self.assertPrinted(">", 0)

    def test_fred_can_stop_the_loop_with_lower_case_q(self):
        # Fred when closing the game as quickly as possible doesn't have time to press shift 
        # He sends a lower case 'q' instead
        # The game closes anyway
        self.say("q")
        self.engine.main_loop()
        
        # The text adventure ends 
        self.assertPrinted(">", 0)

    def test_jaime_can_get_help(self):
        # Jamie has heard from Fred that this new Python powered CodeNewbie text adventure game
        # is not only the cause of his loss of job and sleep, but is also relitively easy for
        # beginners to enjoy because the help functionality is so easy to use.  All she needs to
        # do to check the help is start the main loop.
        # Type 'help' and press enter.
        self.say("help")
        self.say("q")
        self.engine.main_loop()

        # A list of commands will display
        # Jamie can then quit the game and tell her friends all the ease of use.
        self.assertPrinted("help", 1)

class LiteralLinusWantsLovelyMenuLists(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)
        self.engine.room_file = "test_room.json"

    def test_linus_sees_quit_begin_and_help_in_menu_but_no_other_commands_before_entering_a_room(self):
        # Linus plays the game for the first time, he has never seen a game like this
        # He wants to use the help menu heavily and try all of the commands he can.
        # He doesn't want any commands that aren't valid for teh state of the game. 
        # For instance he doesn't want to move his character when  he isn't in a room
        # He still wants to be able to start a game, quit and of course get help
        self.say("help")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("help -")
        self.assertPrintedOnAnyLine("q -")
        self.assertPrintedOnAnyLine("begin -")
        self.assertNotPrintedOnAnyLine("h -")
        self.assertNotPrintedOnAnyLine("j -")
        self.assertNotPrintedOnAnyLine("k -")
        self.assertNotPrintedOnAnyLine("l -")
        self.assertNotPrintedOnAnyLine("x -")

class PlayerCanMoveTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_alexander_can_enter_a_room_and_travel_to_the_exit(self):
        # Alexander, a great fan of text adventures, has entered a new room and seeking fame
        # and glory.
        self.engine.room_file = "alexander_room.json"
        self.say("begin")
        self.say("Alexander")

        # Alexander moves north and enters tile (5,7)
        self.say("k")

        # Alexander moves east and enters tile (6,7)
        self.say("l")

        # Alexander moves north 5 times and enters tile (6, 12)
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")
        self.say("k")

        # Alexander moves west twice and enters tile (4, 12)
        self.say("h")
        self.say("h")

        # Alexander moves south 4 times and enters tile (4, 8)
        self.say("j")
        self.say("j")
        self.say("j")
        self.say("j")

        self.say("x")
        # Alexander now shares a tile with the exit and exits the level.
        self.say("e")
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("exited alexander room")

class PlayerCannotTravelThroughEdgesOfRoom(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_ghastly_cannot_travel_through_room_boundaries(self):
        self.engine.room_file = "tiny_room.json"
        # Ghastly thinks that he can travel though wall and room boundaries
        # as it turns out, he cannot, but that won't stop him from trying.
        # He will try to walk through all 4 room boundaries of the 2 x 2 room.
        self.say("begin")
        self.say("Ghastly")
        
        # He starts in tile 0,0 and tries to go west through a wall
        self.say("h")

        # Then he tries to go south through a wall
        self.say("j")

        # These walls are solid and prevent me from travelling there.  So he travels north twice.
        # The second movement is prevented by a wall
        self.say("k")
        self.say("k")

        # Now he tries the last wall by travelling east twice.  But cannot travel through the east wall
        self.say("l")
        self.say("l")

        # Completely frustrated, Ghastly exits the level.
        self.say("e")

        # Having seen all there is to see, he quits the game and tells all of his friends about
        # the cool map.
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("You cannot go north")
        self.assertPrintedOnAnyLine("You cannot go south")
        self.assertPrintedOnAnyLine("You cannot go east")
        self.assertPrintedOnAnyLine("You cannot go west")

class GameHasBeautifulAndConfigurableDescriptions(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_literary_leslie_loves_lots_of_lively_loquaciousness(self):
        self.engine.room_file = "tiny_room.json"
        # Literary Leslie likes her games to have nice descriptions of things
        # She would like to see life breathed into this text adventure with wonderous words
        self.say("begin")
        
        self.say("Literary")
        self.assertNotPrintedOnAnyLine("dark and cramped")
        # She travels to the exit searching for words 
        self.say("k")
        self.say("l")
        self.say("e")

        # Impressed by the game's literary acumen Leslie quits and writes a 5 star review 
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("harrowed and tiny halls of doom")
        self.engine.init_level()
        
class GameHasMultipleLevels(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def travel_to_the_next_level(self):
        # She travels to the next level
        self.say("k")
        self.say("l")
        self.say("e")

    def test_power_leveling_paula_delves_deeply(self):
        self.engine.room_file = "tiny_room.json"
        # Power leveling Paula likes to get through a game as quickly as possible.
        # She will be overjoyed to travel through three levels to complete the game as quickly 
        # as possible
        self.say("begin")
        self.say("Paula")

        self.travel_to_the_next_level()
        self.travel_to_the_next_level()
        self.travel_to_the_next_level()
        
        # Impressed by the game's literary acumen Leslie quits and writes a 5 star review 
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("harrowed and tiny halls of doom")
        self.assertPrintedOnAnyLine("second of three tiny rooms")
        self.assertPrintedOnAnyLine("third and final tiny room")

        self.assertPrintedOnAnyLine("completed the game")

class CanDrawAMapTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_ian_inventory_can_see_all_items_on_map(self):
        # Ian walks into a room filled with lots of stuff and he wants to see the map
        self.engine.room_file = "item_room.json"
        # Ian wants to know all of the stuff in the room and definately wants to see everything
        # on the map
        # He types begin and enters the game
        self.say("begin")
        self.say("Ian")
        
        # The map displays all items in the room.  Ian sees the exit is one square south.
        # He moves there and exits
        self.say("k")
        self.say("e")

        # Having seen all there is to see, he quits the game and tells all of his friends about
        # the cool map.
        self.say("q")
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("....G")
        self.assertPrintedOnAnyLine("$...*")
        self.assertPrintedOnAnyLine("~....")
        self.assertPrintedOnAnyLine("<....")
        self.assertPrintedOnAnyLine("@....")

class SeesAIntriguingIntroToTheGameTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.library_path, self.fake_input, self.fake_print)

    def test_galaxy_man_satisfies_his_need_for_literary_immersion(self):
        # Galaxy Man tries out the text adventure abd wants to see a 
        # very interesting and immersive introduction to the game
        self.engine.room_file = "item_room.json"

        # He starts it up and enters his name when prompted
        self.say("begin")
        self.say("Galaxy Man")
        self.say("q")

        # Then he recieves a really spectacular introduction
        # describing the purpose of the game and includes an
        # indepth view of the game world.
        self.engine.main_loop()
        self.assertPrintedOnAnyLine("pork belly")
        self.assertPrintedOnAnyLine("to rescue the big pile of bacon")
        self.assertPrintedOnAnyLine("dark and moss covered room")
        self.assertPrintedOnAnyLine("with evil")
        self.assertPrintedOnAnyLine("the low-sodium cartel")
        
        # Satisfied Galaxy Man tells all his friends about how awesome 
        # the text adventure is

