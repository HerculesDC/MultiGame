from pygame.math import Vector2
from engine.behaviour import Behaviour

class Transform(Behaviour):
    def __init__(self):
        super().__init__("Transform")

        self.position = Vector2(0,0)
        self.rotation = 0
        self.scale = Vector2(1,1)

    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)

    def render(self):
        super().render()

    def translate(self, offset):
        if isinstance(offset, (tuple, list, Vector2)):
            self.position[0] += offset[0]
            self.position[1] += offset[1]
        else:
            raise TypeError("Unknown format")

    def set_position(self, new_pos):
        if isinstance(new_pos, (tuple, list, Vector2)):
            self.position[0] = new_pos[0]
            self.position[1] = new_pos[1]
        else:
            raise TypeError("Unknown format")

    def rotate(self, rot):
        self.rotation += rot

    def rescale(self, scale_):
        if isinstance(scale_, (tuple, list, Vector2)):
            self.scale[0] *= scale_[0]
            self.scale[1] *= scale_[1]
        elif isinstance(scale_, (int, float)):
            self.scale *= scale_
        else:
            raise TypeError("Unknown format")
