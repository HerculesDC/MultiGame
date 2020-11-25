from pygame import Rect, Surface
from engine.behaviour import Behaviour

class Renderer(Behaviour):
    def __init__(self, name = "Renderer"):
        super().__init__(name)
        self._size = (0, 0)
        self._surf = None
        self._rect_info = None
        
    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)
        if self._rect_info:
            self._rect_info.center = tuple(self.game_object.transform.position)

    def render(self):
        super().render()
        if self._surf and self._rect_info:
            from engine.game_env import Game
            Game.instance.get_screen().blit(self._surf, self._rect_info)
        else:
            raise TypeError("No surface and/or rect info.")
