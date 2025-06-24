from ursina import *
from bootleg_minecraft import BootlegMinecraft

app = Ursina()

game = BootlegMinecraft()

def input(key):
    game.key_input(key)

app.run()