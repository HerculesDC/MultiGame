from pygame import Rect
from engine.behaviour import Behaviour

class ButtonBehaviour(Behaviour):
    def __init__(self, func, *args_):
        super().__init__("ButtonBehaviour")
        self.center = ()
        self.function = func
        self.args = args_
        self.col = None #Collider
        self.is_hover = False
        self.was_pressed = False
        self.is_pressed = False
        self.is_released = False
        
    def start(self):
        super().start()
        self.center = self.game_object.transform.position
        if self.game_object.has_behaviour("BoxCollider"):
            self.col = self.game_object.get_behaviour("BoxCollider")
        elif self.game_object.has_behaviour("CircleCollider"):
            self.col = self.game_object.get_behavioru("CircleCollider")
        if self.col == None:
            print(self.game_object.name + ", id " + \
                  str(self.game_object.get_id) +\
                  "has no valid Collider attached!")

    def update(self, delta):
        super().update(delta)
        self.center = self.game_object.transform.position
        from engine.input_system import InputSystem
        from engine.point_collider import PointCollider
        temp = PointCollider()
        temp.center = InputSystem.instance.get_mouse_pos()
        self.is_hover = self.col.collidepoint(temp)
        self.is_pressed = self.is_hover and InputSystem.instance.get_mouse_buttons()[0]
        self.is_released = self.was_pressed and not self.is_pressed
        self.was_pressed = self.is_pressed        

    def render(self):
        super().render()

    def on_clicked(self):
        self.function(*self.args)

    def set_function(self, func , *args_):
        self.function = func
        self.args = args

    def set_args(self, *args_):
        self.args = args
