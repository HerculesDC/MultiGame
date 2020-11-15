class Behaviour():
    def __init__(self, name_ = ""):
        self.name = name_
        self.game_object = None
       
        self.is_active = True
        self.is_started = False

    def start(self):
        self.is_started = True

    def update(self, delta):
        pass

    def render(self):
        pass
