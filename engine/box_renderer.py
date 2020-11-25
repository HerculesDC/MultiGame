from pygame import Color, Surface
from engine.renderer import Renderer

class BoxRenderer(Renderer):
    def __init__(self, extent = (0, 0), fill = Color(0, 0, 0)):
        super().__init__("BoxRenderer")
        self._size = extent
        self._surf = Surface(self._size)
        self._rect_info = self._surf.get_rect()
        self._fill = fill
        self._outline = None
        self._line_width = None
        self._radius = 0
        self._tl_radius = -1
        self._tr_radius = -1
        self._bl_radius = -1
        self._br_radius = -1

    def start(self):
        super().start()
        #EXPAND

    def update(self, delta):
        super().update(delta)

    def render(self):
        super().render()

    def set_fill(self, fill):
        self._fill = fill
        self._surf.fill(self._fill)
