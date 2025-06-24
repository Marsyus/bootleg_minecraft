from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class BootlegMinecraft:
    def __init__(self):
        self.player = FirstPersonController()
        Sky()
        self.blocks = []
        self.generate_world()

    def generate_world(self):
        for rows in range(20):
            for columns in range(20):
                block = Button(color=color.white, model='cube', position=(columns,0,rows),
                            texture='grass.png', parent=scene, origin_y=0.5)
                self.blocks.append(block)

    def place_block(self, block):
        new_block = Button(color=color.white, model='cube', position=block.position + mouse.normal,
                                texture='grass.png', parent=scene, origin_y=0.5)
        self.blocks.append(new_block)

    def destroy_block(self, block):
        self.blocks.remove(block)
        destroy(block)

    def key_input(self, key):
        for block in self.blocks:
            if block.hovered:
                if key == 'left mouse down':
                    self.destroy_block(block)
                elif key == 'right mouse down':
                    self.place_block(block)
