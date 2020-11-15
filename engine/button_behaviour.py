from pygame import Rect
from engine.behaviour import Behaviour

class ButtonBehaviour(Button):
    def __init__(self, func, *args_):
        super().__init__("ButtonBehaviour")
        self.center = ()
        self.function = func
        self.args = args_
        
    def start(self):
        super().start()
        self.center = self.game_object.transform.position

    def update(self):
        super().update()
        self.center = self.game_object.transform.position

    def render(self):
        super().render()

    def on_clicked(self):
        self.function(*self.args)

    def set_function(self, func , *args_):
        self.function = func
        self.args = args

    def set_args(self, *args_):
        self.args = args
