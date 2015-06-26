# main game loop goes here
from modules.world import Engine
from os import getcwd

"""
This script launches the game:

> python game.py
"""
base_path = getcwd()
flux_capacitor = Engine(base_path)
flux_capacitor.main_loop()
