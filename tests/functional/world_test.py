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
        engine = Engine(self.base_path, self.fake_input, self.fake_print)
        engine.greet()
        self.assertEqual("Hello, what is your name: ", self.printed[0])
        self.assertEqual("Welcome to text adventure, Hero!", self.printed[1])

class CanLoopTheMainLoop(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)
    
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



class PlayerCanMoveTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)

    def test_alexander_can_enter_a_room_and_travel_to_the_exit(self):
        # Alexander, a great fan of text adventures, has entered a new room and seeking fame
        # and glory.  He starts at tile (5,5)
        alexander_test_room = self.build_path(["tests","fixtures", "alexander_room.json"])
        self.engine.init_level(alexander_test_room)

        x, y = self.engine.room.locate('player')
        self.assertEqual(5, x)
        self.assertEqual(6, y)

        # Alexander moves north and enters tile (5,6)
        self.fail("Finish the test!")

        # Alexander moves east and enters tile (6,6)

        # Alexander moves north 5 times and enters tile (6, 11)

        # Alexander moves west twice and enters tile (4, 11)

        # Alexander moves south 4 times and enters time (4, 7)

        # Alexander now shares a tile with the exit and exits the level.


