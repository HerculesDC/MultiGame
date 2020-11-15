import random
import json
import pygame
from pygame.time import Clock

from engine.input_system import InputSystem
from engine.screen import Screen
from src.screens.start_screen import StartScreen
from src.screens.game_select_screen import GameSelectScreen
from src.screens.test_screen import TestScreen

class Game:
    class __Game:
        _FPS = 45
        screen = None
        level = None
        def __init__(self):
            random.seed()
            self.is_started = False
            self.is_running = False

            #This will become JSON later
            self.screen_size = (800, 600)
            self.title = "HErC\'s Simple Game Library"

            self.clock = Clock()
            self.delta = 0
            
            pygame.init()
            self.time_since_started = pygame.time.get_ticks()
            Game.__Game.screen = pygame.display.set_mode(self.screen_size,
                                                  pygame.RESIZABLE)
            
            pygame.display.set_caption(self.title)
            #Game.__Game.set_level(StartScreen(self.screen_size))
            #Game.__Game.set_level(GameSelectScreen(self.screen_size))
            Game.__Game.set_level(TestScreen(self.screen_size))

            self.__input_system = InputSystem()
            
            self.is_running = True

        def start(self):
            self.__input_system.start()
            self.is_started = True
        
        def run(self):
            if self.is_started:
                return
            self.start()

            while self.is_running:
                if not Game.__Game.level.is_started:
                    Game.__Game.level.start()
                self.process_events()
                self.update(self.delta)
                self.render()
                self.delta = self.clock.tick(Game.__Game._FPS)
                self.time_since_started = pygame.time.get_ticks()
            self.cleanup()

        def process_events(self):
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    self.is_running = False
                elif evt.type == pygame.VIDEORESIZE:
                    self.screen_size = evt.size
                else:
                    self.__input_system.process_events(evt)

        def update(self, delta):
            if self.screen_size != Game.__Game.screen.get_size():
                Game.__Game.screen = pygame.display.set_mode(self.screen_size,
                                                      pygame.RESIZABLE)
                Game.__Game.level.resize(self.screen_size)
            Game.__Game.level.update(delta)

        def render(self):
            Game.__Game.level.render()
            pygame.display.flip()

        def cleanup(self):
            pygame.quit()
        
        #Screen management
        @staticmethod
        def set_level(new_screen):
            if isinstance(new_screen, Screen):
                #must get cause static method
                temp = pygame.display.get_surface().get_size()
                if new_screen.get_size() != temp:
                    new_screen.resize(temp)
                Game.__Game.level = new_screen
                if not Game.__Game.level.is_started:
                    Game.__Game.level.start()
            else:
                raise TypeError(str(type(new_screen))+\
                                "is not a valid Screen type")
        
        @staticmethod
        def get_screen():
            return Game.__Game.screen
            
    instance = None            

    #Singleton Manager methods:
    def __init__(self):
        if not Game.instance:
            Game.instance = Game.__Game()

    def __getattr__(self, name):
        return getattr(self.instance, name)
