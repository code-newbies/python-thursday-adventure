# engine.py
"""This module ties all of the disparate components together"""
from modules.world import initial_narration
from modules.command_line import CommandLine
from modules.bag import Bag
from modules.level_loader import LevelLoader
from modules.player import Player
from modules.item import Item
from modules.movement import next_tile


def tuple_values(pos, command_list):
    """returns a list of values at pos from a list of tuples"""
    return list(map(lambda x: x[pos], command_list))

class Engine:
    """This class ties it all together and might be viewed as something
    somewhat akin to a controller in an MVC framework.

    """
    def __init__(self, library_path, prompt_func=input, print_func=print):
        self.prompt_char = ">"
        self.library_path = library_path
        self.reset_game()
        self.interface = CommandLine(self, prompt_func, print_func)
        self.bag = Bag()
        self.level = None
        self.player = None
        self.player_in_room = None
        self.room = None

    def start(self):
        """Use this method to start the game"""
        player_name = self.interface.greet()
        self.player = Player(player_name)
        self.interface.display(initial_narration())
        self.init_level()
        self.interface.display(self.level.draw_map())

    def init_level(self):
        """Looks up the level information from file, loads it and inserts
        the player into the room.
        """
        self.room = LevelLoader(self.library_path, self.room_file)
        self.level = self.room.enter(self.player, "entrance")
        self.player_in_room = True
        self.interface.display(self.room.room_description())

    def reset_game(self):
        """Returns the game to its initial state"""
        self.room_file = "level_1.json"
        self.player_in_room = False

    def in_room(self):
        """Used to determine if the player is currently in a room"""
        if self.player == None:
            return False

        return self.player.in_room()

    def load_player(self, player):
        """Attribute setter for the player"""
        self.player = player

    def north(self):
        """Moves the player north if able"""
        if not self.level.can_go_north(self.player):
            self.interface.display("You cannot go north")
        else:
            for creature in self.level.get_move_ai():
                if creature.coords == (self.player.coords[0], self.player.coords[1] + 1):
                    self.attack(creature)
                    break
            else:
                self.player.travel("n")

    def south(self):
        """Moves the player south if able"""
        if not self.level.can_go_south(self.player):
            self.interface.display("You cannot go south")
        else:
            for creature in self.level.get_move_ai():
                if creature.coords == (self.player.coords[0], self.player.coords[1] - 1):
                    self.attack(creature)
                    break
            else:
                self.player.travel("s")

    def east(self):
        """Moves the player east if able"""
        if not self.level.can_go_east(self.player):
            self.interface.display("You cannot go east")
        else:
            for creature in self.level.get_move_ai():
                if creature.coords == (self.player.coords[0] + 1, self.player.coords[1]):
                    self.attack(creature)
                    break
            else:
                self.player.travel("e")

    def west(self):
        """Moves the player west if able"""
        if not self.level.can_go_west(self.player):
            self.interface.display("You cannot go west")
        else:
            for creature in self.level.get_move_ai():
                if creature.coords == (self.player.coords[0] - 1, self.player.coords[1]):
                    self.attack(creature)
                    break
            else:
                self.player.travel("w")

    def attack(self, enemy):
        dmg = self.player.weapon.damage
        self.interface.display("You attack the " + enemy.name + " for " + str(dmg) + " damage!")
        response = enemy.take_damage(dmg)
        enemy.set_target(self.player)
        if response:
            self.interface.display(response)
            for index, item in enumerate(self.level.contents):
                if item is enemy:
                    self.level.remove(enemy.name)

    def exit(self):
        """Tests for exit conditions and exits the player if they are met
        The length of this method suggests that it is ripe for splitting
        these actions into separate methods
        """
        can_exit = self.level.exit(self.player)

        if can_exit:
            self.display_exit_message()

            if not self.enter_next_level():
                self.player_in_room = False
                self.interface.display_end_of_game()
        else:
            format_string = "Sorry, you are not at an exit of {0}."
            message = format_string.format(self.room.name)
            self.interface.display(message)
        return can_exit

    def display_exit_message(self):
        """Displays the level's exit text to the user if it exists"""
        if self.room.exit_text == None:
            self.interface.display("You have exited {0}".format(self.room.name))
        else:
            self.interface.display(self.room.exit_text)

    def enter_next_level(self):
        """Transports the player to the next level or returns False if
        there is no next level
        """
        next_level, has_next_level = self.room.enter_next_level(self.player)
        if has_next_level:
            self.level = next_level
            self.interface.display(self.room.room_description())
            return True

        return False

    def item_count(self):
        """Displays the player's inventory"""
        self.interface.display(self.bag.look())

    def coordinates(self):
        """Returns the x, y coordinates of the player"""
        coords = self.player.locate()
        message = "Your co-ordinates are: ({0},{1})".format(coords[0], coords[1])
        self.interface.display(message)

    def vaccum_key_and_gold(self):
        """Automagically picks up gold and keys"""
        if self.pick_up_item("key"):
            self.interface.display("You picked up the key!")
        if self.pick_up_item("gold"):
            self.interface.display("You picked up the gold!")

    def vaccum_weapons(self):
        """Swiftly picks up Excalibur"""
        if self.pick_up_item("excalibur"):
            self.interface.display("Behold! The most power ever felt!")

    def pick_up_item(self, item):
        """Allows the player to pick up and item by removing an item from the
        room and placing it in their bag
        """
        if self.level.get_by_name(item) != None:
            player_coord = self.player.locate()
            item_coord = self.level.get_by_name(item).locate()
            if player_coord == item_coord:
                self.bag.add(Item(item))
                self.level.remove(item)
                return True

        return False

    def display_help(self):
        """Displays the help menu"""
        self.interface.display_help(self.in_room())

    def invalid_command(self):
        """Displays a message that tells the user their command was invalid"""
        self.interface.display("Sorry that command is not valid.")
        self.interface.display("Please type 'help' and press enter for a menu.")

    def main_loop(self):
        """This is the core game loop that cycles through the turns"""
        play = True

        self.start()
        while play:
            play = self.move_player()

            if self.in_room():
                self.vaccum_key_and_gold()
                self.vaccum_weapons()
                play &= self.move_creatures()
                if play:
                    self.interface.display(self.level.draw_map())
                    self.interface.display(self.player.show_health())

    def move_player(self):
        """Gets the command from the player and moves (or quits)"""
        command = self.interface.prompt(self.prompt_char).lower()
        possible_commands = self.interface.current_commands(self.in_room())

        if command == "q":
            return False
        else:
            if not self.execute_command(command, possible_commands):
                self.invalid_command()

        return True

    def execute_command(self, command, commands):
        """Executes the command if valid, returns false if invalid"""
        try:
            cmd_tuple = commands[command]
            cmd_tuple[0]()
            return True
        except KeyError:
            return False


    def move_creatures(self):
        """Moves the creatures in the room"""
        creatures = self.level.get_move_ai()

        for creature in creatures:
            target_tile = next_tile(creature.coords, creature.target)
            if target_tile == self.player.coords:
                dmg = creature.weapon.damage
                self.interface.display("You were attacked by the " + creature.name + " for " + str(dmg) + " damage!")
                response = self.player.take_damage(dmg)
                if response:
                    self.interface.display(response)
                    return False
            else:
                creature.move()
        return True
