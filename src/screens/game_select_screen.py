from engine.constants import *
from engine.screen import Screen
from engine.game_object import GameObject
from engine.font_renderer import FontRenderer
from src.behaviours.meteors_behaviour import Meteors
from src.behaviours.overlay_behaviour import Overlay

class GameSelectScreen(Screen):
    def __init__(self, size = (0, 0)):
        super().__init__(size)
        self.add_game_object(GameObject("Overlay"), BACKGROUND)
        self._back_objects["Overlay"].add_behaviour(Overlay(self._size))
        
        self.add_game_object(GameObject("Meteors"), BACKGROUND)
        self._back_objects["Meteors"].add_behaviour(Meteors(self._size))
        

        self.add_game_object(GameObject("Title"), UI)
        self._ui_objects["Title"].get_behaviour("Transform").position =\
                            (int(self._size[0]/2), int(self._size[1]/3))
        self._ui_objects["Title"].add_behaviour(\
            FontRenderer("SIMPLE GAME MEDLEY", 64))
        

    def start(self):
        self._ui_objects["Title"].get_behaviour("Transform").position =\
            (int(self._size[0]/2), int(self._size[1]/3))
        super().start()

    def update(self, delta):
        if self._size != self._back_objects["Meteors"].\
                               get_behaviour("Meteors").get_bounce_area():
            self._back_objects["Meteors"].get_behaviour("Meteors").\
                               set_bounce_area(self._size)
        super().update(delta)
        
    def render(self):
        super().render()
        
    def resize(self, new_size):
        super().resize(new_size)
        self._back_objects["Overlay"].get_behaviour("Overlay").resize(self._size)
        self._back_objects["Meteors"].get_behaviour("Meteors").set_bounce_area(self._size)
        self._ui_objects["Title"].get_behaviour("Transform").position =\
                            (int(self._size[0]/2), int(self._size[1]/3))
        
