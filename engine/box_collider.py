from pygame import Rect
from engine.collider import Collider

class BoxCollider(Collider):
    def __init__(self, debug = False, size_ = (0, 0)):
        super().__init__("BoxCollider", debug)
        self.center = None
        self.rotation = None
        self.size = size_
        self.rect = Rect((0, 0), self.size)

    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)
        self.rect.center = self.center

    def render(self):
        super().render()
        if self._is_debug and self.size and self.center:
            import pygame.draw
            from engine.game_env import Game
            pygame.draw.rect(Game.instance.get_screen(), (0, 255, 0), self.rect, 1)

    def collidepoint(self, other):
        super().collidepoint(other)
        return self.rect.collidepoint(other.center)

    def colliderect(self, other):
        super().colliderect(other)
        return self.rect.colliderect(other.rect)

    def get_clip_area(self, other):
        return self.rect.clip(other.rect)    

    def collideline(self, other):
        super().collideline(other)
        #REDO!!! This only works in pygame 2.0
        return False

    def collidecircle(self, other):
        super().collidecircle(other)
        #BUGGY!!! VERIFY
        test_x = other.center[0]
        test_y = other.center[1]

        if other.center[0] < self.rect.left:
            test_x = self.rect.left
        elif other.center[0] > self.rect.right:
            test_x = self.rect.right

        if other.center[1] < self.rect.top:
            test_y = self.rect.top
        elif other.center[1] > self.rect.bottom:
            test_y = self.rect.bottom

        dist_x = other.center[0] - test_x
        dist_y = other.center[1] - test_y

        dist = ((dist_x*dist_x)+(dist_y*dist_y))**0.5

        return dist <= other.radius
