from pygame import Color
from engine.constants import *
from engine.screen import Screen
from engine.game_object import GameObject
from engine.font_renderer import FontRenderer

class StartScreen(Screen):
    def __init__(self, size = (0, 0)):
        super().__init__(size, (0, 0, 0, 255))
        
        self._txt_col = Color(25, 75, 255)
        self._hsva_buf = self._txt_col.hsva
        self._start = 0
        self._speed = 1

        self._should_advance = False

        title = GameObject("Title")
        title.add_behaviour(FontRenderer("HErC presents", 100, self._txt_col))
        self.add_game_object(title, UI)
        
    def start(self):
        self._ui_objects["Title"].get_behaviour("Transform").position=\
            (self._size[0]>>1, int(self._size[1]/2.5))
        super().start()

    def update(self, delta):
        if self._should_advance:
            from src.screens.game_select_screen import GameSelectScreen
            self.advance_screen(GameSelectScreen(self._size))
        else:
            self._start += self._speed
            #HSVA's S and V values cannot exceed 100
            if self._start + self._speed > 100:
                self._speed *= -3
            elif self._start + self._speed < 0:
                self._should_advance = True
                self.start = 0
                
            self._hsva_buf = (self._hsva_buf[0],
                              self._start,
                              self._start,
                              self._hsva_buf[3])
            self._txt_col.hsva = self._hsva_buf
            self._ui_objects["Title"].\
                        get_behaviour("FontRenderer").set_colour(self._txt_col)
        super().update(delta)    
