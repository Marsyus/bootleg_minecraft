from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class BootlegMinecraft:
    def __init__(self):
        self.app = Ursina()
        self.player = FirstPersonController()
        Sky()
        self.blocks = []

        for rows in range(20):
            for columns in range(20):
                block = Button(color=color.white, model='cube', position=(columns,0,rows),
                            texture='grass.png', parent=scene, origin_y=0.5)
                self.blocks.append(block)

    def key_input(self, key):
        for block in self.blocks:
            if block.hovered:
                if key == 'left mouse down':
                    new_block = Button(color=color.white, model='cube', position=block.position + mouse.normal,
                                texture='grass.png', parent=scene, origin_y=0.5)
                    self.blocks.append(new_block)
                elif key == 'right mouse down':
                    self.blocks.remove(block)
                    destroy(block)

    def start(self):
        self.app.run()
