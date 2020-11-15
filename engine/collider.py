"""
    Note: Not intended for direct use
    Calculations in derived classes based on Jeff Thompson's website
    www.jeffreythompson.org
"""
from engine.behaviour import Behaviour

class Collider(Behaviour):
    def __init__(self, name = "Collider", debug = False):
        super().__init__(name)
        self.center = None
        self.rotation = None
        self.size = None #expected box or diameter
        self._is_debug = debug
        
    def start(self):
        self.center = self.game_object.transform.position
        super().start()

    def update(self, delta):
        super().update(delta)
        t = self.game_object.transform
        self.center = (int(t.position[0]), int(t.position[1]))
        self.rotation = t.rotation

    def render(self):
        super().render()

    def collidepoint(self, other):
        if not isinstance(other, Collider):
            raise TypeError("Not a collider")

    def colliderect(self, other):
        if not isinstance(other, Collider):
            raise TypeError("Not a collider")

    def collideline(self, other):
        if not isinstance(other, Collider):
            raise TypeError("Not a collider")

    def collidecircle(self, other):
        if not isinstance(other, Collider):
            raise TypeError("Not a collider")
