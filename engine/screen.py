from pygame import Color
from engine.constants import *
from engine.game_object import GameObject

class Screen():
    def __init__(self, size = (0, 0), colour = None):
        self._screen_colour = colour
        self._size = size
        self._back_objects = {}
        self._game_objects = {}
        self._ui_objects = {}

        self.is_started = False

    def start(self):
        for back_key in self._back_objects.keys():
            if not self._back_objects[back_key].is_started:
                self._back_objects[back_key].start()
                
        for game_key in self._game_objects.keys():
            if not self._game_objects[game_key].is_started:
                self._game_objects[game_key].start()
                
        for ui_key in self._ui_objects.keys():
            if not self._ui_objects[ui_key].is_started:
                self._ui_objects[ui_key].start()
        if not self.is_started:
            self.is_started = True
    
    def update(self, delta):
        for back_key in self._back_objects.keys():
            if self._back_objects[back_key].is_active:
                self._back_objects[back_key].update(delta)
                
        for game_key in self._game_objects.keys():
            if self._game_objects[game_key].is_active:
                self._game_objects[game_key].update(delta)
                
        for ui_key in self._ui_objects.keys():
            if self._ui_objects[ui_key].is_active:
                self._ui_objects[ui_key].update(delta)

    def get_size(self):
        return self._size
    
    def resize(self, new_size):
        self._size = new_size

    def render(self):
        #Convenience only
        if self._screen_colour:
            from engine.game_env import Game
            Game.instance.get_screen().fill(self._screen_colour)
                
        for back_key in self._back_objects.keys():
            if self._back_objects[back_key].is_active:
                self._back_objects[back_key].render()
                
        for game_key in self._game_objects.keys():
            if self._game_objects[game_key].is_active:
                self._game_objects[game_key].render()
                
        for ui_key in self._ui_objects.keys():
            if self._ui_objects[ui_key].is_active:
                self._ui_objects[ui_key].render()
        
    #Internal management functions
    def check_name(self, name, layer = GAMELAYER):
        if not isinstance(name, str):
            raise TypeError("Invalid name")
        if not isinstance(layer, int):
            raise TypeError("Invalid layer")
        if layer != BACKGROUND and\
           layer != GAMELAYER and\
           layer != UI:
            raise ValueError("non-existent layer")
        if layer == BACKGROUND:
            return name in self._back_objects.keys()
        if layer == GAMELAYER:
            return name in self._game_objects.keys()
        if layer == UI:
            return name in self._ui_objects.keys()
        
    def add_game_object(self, new_go, layer = GAMELAYER):
        if not isinstance(new_go, GameObject):
            raise TypeError(str(type(new_go))+" is not a GameObject.")
        else:
            if not isinstance(new_go.name, str):
                raise TypeError("GameObject name must be str.")
            if new_go.name == "":
                raise ValueError("Cannot add empty-named GameObject")
            if self.check_name(new_go.name, layer):
                raise ValueError(new_go.name+" already exists in layer.")
            else:
                new_go.set_layer(layer)
                if layer == BACKGROUND:
                    self._back_objects[new_go.name] = new_go
                    if not self._back_objects[new_go.name].is_started:
                        self._back_objects[new_go.name].start()
                    return
                if layer == GAMELAYER:
                    self._game_objects[new_go.name] = new_go
                    if not self._game_objects[new_go.name].is_started:
                        self._game_objects[new_go.name].start()
                    return
                if layer == UI:
                    self._ui_objects[new_go.name] = new_go
                    if not self._ui_objects[new_go.name].is_started:
                        self._ui_objects[new_go.name].start()
                    return
                
    def remove_game_object(self, rem_go, layer = GAMELAYER):
        name = ""
        if isinstance(rem_go, GameObject):
            name = rem_go.name
        elif isinstance(rem_go, str):
            name = rem_go
        else:
            raise TypeError("Not a valid GameObject or string argument")
        if self.checkname(name, layer):
            if layer == BACKGROUND:
                return self._back_objects.pop(name)
            if layer == GAMELAYER:
                return self._game_objects.pop(name)
            if layer == UI:
                return self._ui_objects.pop(name)
        else:
            raise ValueError("Not found...")
            return

    def get_game_object(self, go, layer = GAMELAYER):
        name = ""
        if isinstance(go, GameObject):
            name = go.name
        elif isinstance(go, str):
            name = go
        else:
            raise TypeError("Not a valid GameObject or str argument")
        if self.checkname(name, layer):
            if layer == BACKGROUND:
                return self._back_objects[name]
            if layer == GAMELAYER:
                return self._game_objects[name]            
            if layer == UI:
                return self._ui_objects[name]
        else:
            raise ValueError("Not found...")
            return
    
    def has_game_object(self, go):
        name = ""
        if isinstance(go, GameObject):
            name = go.name
        elif isinstance(go, str):
            name = go
        else:
            raise TypeError("Not a valid GameObject or str argument")
        return (self.check_name(name, UI),
                self.check_name(name, GAMELAYER),
                self.check_name(name, BACKGROUND))
            
    #Cross-screen management functionality
    #Obs.: errors are managed by the Game
    def advance_screen(self, new_screen):
        from engine.game_env import Game
        Game.instance.set_level(new_screen)
