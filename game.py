# main game loop goes here
from modules.engine import Engine
from os import getcwd
from os.path import join

"""
This script launches the game:

> python game.py
"""
library_path = join(getcwd(), "resources")
flux_capacitor = Engine(library_path)
flux_capacitor.main_loop()
