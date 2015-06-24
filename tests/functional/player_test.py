import sys
import unittest
from modules.world import Room, Engine
from modules.player import Player
from tests.helpers import BaseTest
from os import getcwd
from os.path import join

class PlayerCanMoveTest(BaseTest):
    def setUp(self):
        self.init()
        self.engine = Engine(self.base_path, self.fake_input, self.fake_print)

    def test_alexander_can_enter_a_room_and_travel_to_the_exit(self):
        # Alexander, a great fan of text adventures, has entered a new room and seeking fame
        # and glory.  He starts at tile (5,5)
        alexander_test_room = self.build_path(["tests","fixtures", "alexander_room.csv"])
        self.engine.room = Room(alexander_test_room)
        alexander = Player("Alexander")
        self.engine.load_player(alexander)
        self.engine.room.enter(self.engine.player, "entrance")

        x, y = self.engine.room.locate(player)
        self.assertEqual(5, x)
        self.assertEqual(5, y)

        # Alexander moves north and enters tile (5,6)
        self.fail("Finish the test!")

        # Alexander moves east and enters tile (6,6)

        # Alexander moves north 5 times and enters tile (6, 11)

        # Alexander moves west twice and enters tile (4, 11)

        # Alexander moves south 4 times and enters time (4, 7)

        # Alexander now shares a tile with the exit and exits the level.


