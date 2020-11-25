"""
    HAS A LOT OF TODOS IN THE COLLISION DETECTION PART!!!
    Check all "return False" ones
"""
from engine.collider import Collider

class LineCollider(Collider):
    def __init__(self, debug = False):
        super().__init__("LineCollider", debug):
            self.p1 = []
            self.p2 = []
            self.line = []

    def start(self):
        super().start()
        self.line = self.p1 + self.p2

    def update(self, delta):
        super().update(delta)
        #Think of ways to improve this

    def render(self):
        super().render()
        if self._is_debug and self.p1 and self.p2:
            import pygame.draw
            from engine.game_env import Game
            pygame.draw.line(Game.instance.get_screen(), (0, 255, 0), self.p1, self.p2, 1)

    def collidepoint(self, other):
        super().collidepoint(other)
        line_length = ((self.p1[0] - self.p2[0])**2) + ((self.p1[1] - self.p2[1])**2))
        d1 = (((self.p1[0] - other.center[0])**2)+((self.p1[1]-other.center[1])**2))
        d2 = (((self.p2[0] - other.center[0])**2)+((self.p2[1]-other.center[1])**2))
        return d1 + d2 == line_length

    def colliderect(self, other):
        super().colliderect(other)
        return other.rect.collideline(self.line)

    def collideline(self, other):
        super().collideline(other)
        return False

    def collidecircle(self, other):
        super().collidecircle(other)
        return False
