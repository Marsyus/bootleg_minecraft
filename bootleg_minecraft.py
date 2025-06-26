from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

class BootlegMinecraft:
    def __init__(self):
        self.player = FirstPersonController()
        Sky()
        self.blocks = []
        self.generate_world()
        self.texture = 'images/grass.png'

    def random_grass(self):
        rand = random.randint(0, 100)
        if 0 <= rand < 86:
            return 'images/grass.png'
        if 86 <= rand < 91:
            return 'images/flower_1.png'
        if 91 <= rand < 96:
            return 'images/flower_2.png'
        if 96 <= rand <= 100:
            return 'images/flower_3.png'

    def generate_world(self):
        for rows in range(-10, 10):
            for columns in range(-10, 10):
                block = Button(color=color.white, model='cube', position=(columns,0,rows),
                            texture=self.random_grass(), parent=scene, origin_y=0.5)
                self.blocks.append(block)

    def place_block(self, block):
        new_block = Button(color=color.white, model='cube', position=block.position + mouse.normal,
                                texture=self.texture, parent=scene, origin_y=0.5)
        self.blocks.append(new_block)

    def destroy_block(self, block):
        self.blocks.remove(block)
        destroy(block)

    def key_input(self, key):
        if key == '1':
            self.texture = 'images/grass.png'
        if key == '2':
            self.texture = 'images/dirt.png'
        if key == '3':
            self.texture = 'images/cobble.png'
        if key == '4':
            self.texture = 'images/stone.png'
        if key == '5':
            self.texture = 'images/wood.png'
        
        for block in self.blocks:
            if block.hovered:
                if key == 'left mouse down':
                    self.destroy_block(block)
                elif key == 'right mouse down':
                    self.place_block(block)
