from pygame import Color
from engine.screen import Screen
from engine.game_object import GameObject
from engine.input_system import InputSystem

class TestScreen(Screen):
    def __init__(self, size = (0, 0)):
        super().__init__(size, Color(100, 150, 255))
        
        self.add_game_object(GameObject("test"))
        self._game_objects["test"].transform.set_position((self._size[0]>>1, self._size[1]>>1))
        from engine.box_collider import BoxCollider
        
        from engine.box_renderer import BoxRenderer
        from engine.button_behaviour import ButtonBehaviour
        self._game_objects["test"].add_behaviour(BoxCollider(True,(100, 100)))
        self._game_objects["test"].add_behaviour(BoxRenderer((100, 100)))
        self._game_objects["test"].add_behaviour(ButtonBehaviour(None, None))
        from src.behaviours.button_manager import ButtonManager
        self._game_objects["test"].add_behaviour(ButtonManager())
        from engine.circle_collider import CircleCollider
        self.add_game_object(GameObject("mouse"))
        self._game_objects["mouse"].add_behaviour(CircleCollider(True, 75))

    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)
        self._game_objects["mouse"].transform.position = \
                                        InputSystem.instance.get_mouse_pos()
        self.process_collisions()
        
    def render(self):
        super().render()

    def process_collisions(self):
        temp = self._game_objects["test"].get_behaviour("BoxCollider").\
               collidecircle(self._game_objects["mouse"].get_behaviour("CircleCollider"))
           
        if temp:
            self._screen_colour = Color(0, 0, 0)
        else:
            self._screen_colour = Color(100, 150, 255)
