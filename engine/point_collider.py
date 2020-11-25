from engine.collider import Collider

class PointCollider(Collider):
    def __init__(self, debug = False):
        super().__init__("PointCollider", debug)

    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)

    def render(self):
        super().render()
        if self._is_debug:
            import pygame.draw
            from engine.game_env import Game
            pygame.draw.circle(Game.instance.get_screen(), (0, 255, 0), self.point, 1, 1)

    def collidepoint(self, other):
        super().collidepoint(other)
        return self.center[0] == other.center[0] and self.center[1] == other.center[1]

    def colliderect(self, other):
        super().colliderect(other)
        return other.rect.collidepoint(self.center)

    def collideline(self, other):
        super().collideline(other)
        return False

    def collidecircle(self, other):
        super().collidecircle(other)
        return other.collidepoint(self)
