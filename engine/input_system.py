import pygame.key
import pygame.mouse
from pygame.locals import *

class InputSystem():
    instance = None
    class __InputSystem():
        def __init__(self):
            self.keys = None
            self.buttons = None
            self.mouse_prev = None
            self.mouse_pos = None
            self.mouse_rel = None
            self.started = False
            
        def start(self):
            import pygame.display
            self.started = pygame.display.get_init()
            if not self.started:
                raise AssertionError("Display not initialized")
            self.keys = pygame.key.get_pressed()
            self.buttons = pygame.mouse.get_pressed()
            self.mouse_prev = self.mouse_pos = pygame.mouse.get_pos()
            self.mouse_rel = pygame.mouse.get_rel()

        def process_events(self, evt):
            if evt.type == KEYUP or evt.type == KEYDOWN:
                self.keys = pygame.key.get_pressed()
            if evt.type == MOUSEBUTTONUP or evt.type == MOUSEBUTTONDOWN:
                self.buttons = pygame.mouse.get_pressed()
                self.mouse_prev = self.mouse_pos
                self.mouse_pos = pygame.mouse.get_pos()
                self.mouse_rel = pygame.mouse.get_rel()
            if evt.type == MOUSEMOTION:
                self.mouse_prev = self.mouse_pos
                self.mouse_pos = pygame.mouse.get_pos()
                self.mouse_rel = pygame.mouse.get_rel()

        def get_keys(self):
            return self.keys

        def get_key(self, key):
            return self.keys[key]

        def get_mouse_buttons(self):
            return self.mouse_buttons()

        def get_mouse_pos(self):
            return self.mouse_pos

        def get_mouse_prev(self):
            return self.mouse_prev

        def get_mouse_rel(self):
            return self.mouse_rel
                
    def __init__(self):
        if not InputSystem.instance:
            InputSystem.instance = InputSystem.__InputSystem()

    def __getattr__(self, name):
        return getattr(self.instance, name)
