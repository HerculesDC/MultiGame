from pygame import Color
from engine.behaviour import Behaviour

class ButtonManager(Behaviour):
    def __init__(self):
        super().__init__("ButtonManager")
        self._out_colour = Color(200, 200, 0)
        self._released_colour = Color(0, 0, 255)
        self._hover_colour = Color(0, 255, 0)
        self._pressed_colour = Color(255, 0, 0)
        self._bb = None #Button Behaviour placeholder
        self._br = None #Box Renderer Behaviour

    def start(self):
        super().start()
        self._bb = self.game_object.get_behaviour("ButtonBehaviour")
        self._br = self.game_object.get_behaviour("BoxRenderer")

    def update(self, delta):
        super().update(delta)
        if not self._bb.is_hover:
            self._br.set_fill(self._out_colour)
        elif self._bb.is_pressed:
            self._br.set_fill(self._pressed_colour)
        elif self._bb.is_released:
            self._br.set_fill(self._released_colour)
        elif self._bb.is_hover:
            self._br.set_fill(self._hover_colour)
        

    def render(self):
        super().render()
