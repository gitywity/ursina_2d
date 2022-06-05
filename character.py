from ursina import Sprite, held_keys

class Character(Sprite):
    def __init__(self):
        super().__init__()
        self.dx = 00
        self.dy = 00
        self.friction = .05
        self.accel = 1.000000000
        self.speed = 0.000000000
        self.is_running = False
        self.running_mult = 1.25
    
    def update(self):
        going_right = held_keys["d"] or held_keys["right arrow"]
        going_left = held_keys["a"] or held_keys["left arrow"]

