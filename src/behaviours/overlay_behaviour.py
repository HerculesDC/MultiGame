from pygame import Color, Rect, Surface, Vector2
from pygame.locals import *
from engine.behaviour import Behaviour

class Overlay(Behaviour):
    def __init__(self, size = (0, 0), colour = Color(0, 0, 0, 50)):
        super().__init__("Overlay")
        self._surf = None
        self._rect = Rect((0, 0), size)
        self._colour = colour

    def start(self):
        self.prepare_surface(self._rect.size)
        super().start()

    def update(self, delta):
        super().update(delta)
        
    def render(self):
        super().render()
        from engine.game_env import Game
        Game.instance.get_screen().blit(self._surf, self._rect)

    def resize(self, size):
        if isinstance(size, (tuple, list, Vector2)):
            if len(size) == 2:
                self._rect = Rect((0, 0), size)
                self.prepare_surface(size)
            elif len(size) == 4:
                self._rect = Rect((size[0],size[1]),(size[2],size[3]))
                self.prepare_surface((size[2],size[3]))
            else:
                raise ValueError("Not enough data to resize")
        elif isinstance(size, Rect):
            self._rect = Rect(size)
            self.prepare_surface(size.size)
        else:
            raise TypeError("Incompatible type")
        
    def reposition(self, coords):
        if isinstance(size, (tuple, list, Rect, Vector2)):
            if len(size) == 2 or len(size) == 4:
                self._rect.left = size[0]
                self._rect.top = size[1]
            else:
                raise ValueError("Not enough data to reposition")
        else:
            raise TypeError("Incompatible type")

    def prepare_surface(self, size):
        self._surf = Surface(size, SRCALPHA)
        self._surf.fill(self._colour)
