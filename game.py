# main game loop goes here
from modules.engine import Engine
from os import getcwd

base_path = getcwd
flux_capacitor = Engine(base_path)
flux_capacitor.start()
