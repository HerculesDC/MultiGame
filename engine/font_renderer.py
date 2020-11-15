"""
    As a class that inherits from Behaviour, it has unreferenced
    attributes, such as: super().game_object, super().transform,
    super().is_active and super().is_started
"""
from pygame import Rect, Color, Surface
from engine.renderer import Renderer

class FontRenderer(Renderer):
    def __init__(self, txt = "Placeholder Text", size = 12, colour = Color(255, 255, 255)):
        super().__init__("FontRenderer")
        #Non-changed variables from super() include:
        #   is_active, is_started
        #   game_object and transform
        self._message = txt
        self._text_size = size
        self._text_colour = colour
        self._do_antialias = True
        
        self._font = None

    #Behaviour Functions
    def start(self):
        self.prepare_surface()
        super().start()

    def update(self, delta):
        super().update(delta)

    def render(self):
        from engine.game_env import Game
        Game.instance.get_screen().blit(self._surf, self._rect_info)
        super().render()

    #setters
    def set_size(self, size):
        self._text_size = int(size) #will raise exception if invalid
        self.prepare_surface()

    def set_text(self, txt):
        self._message = str(txt)
        self.prepare_surface()

    def set_colour(self, colour = Color(255, 255, 255)):
        if not isinstance(colour, (tuple, list, Color)):
            raise TypeError("Invalid colour type")
        elif len(colour) < 3:
            raise ValueError("Insufficient colour data")
        elif len(colour) == 3:
            self._text_colour = Color(colour[0], colour[1], colour[2])
        else:
            self._text_colour = Color(colour[0], colour[1], colour[2], colour[3])
        self.prepare_surface()
            
    #Self-management functions
    def prepare_surface(self):
        import pygame.font
        from pygame.font import Font
        self._font = Font(pygame.font.get_default_font(), self._text_size)
        self._surf = self._font.render(self._message, self._do_antialias,
                                       self._text_colour)
        self._rect_info = self._surf.get_rect()
        self._rect_info.center = tuple(self.game_object.\
                                       get_behaviour("Transform").position)
