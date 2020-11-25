from engine.collider import Collider

class CircleCollider(Collider):
    def __init__(self, debug = False, radius_ = 0):
        super().__init__("CircleCollider", debug)
        self.center = None
        self.rotation = None
        self.radius = radius_

    def start(self):
        super().start()

    def update(self, delta):
        super().update(delta)

    def render(self):
        super().render()
        if self._is_debug and self.radius and self.center:
            import pygame.draw
            from engine.game_env import Game
            pygame.draw.circle(Game.instance.get_screen(), (0, 255, 0), self.center, self.radius, 1)

    def collidepoint(self, other):
        super().collidepoint(other)
        dist = ((other.center[0] - self.center[0])**2 + \
                (other.center[1] - self.center[1])**2)**0.5
        return dist <= self.radius

    def colliderect(self, other):
        super().colliderect(other)

        test_x = self.center[0]
        test_y = self.center[1]

        if self.center[0] < other.rect.left:
            test_x = other.rect.left
        elif self.center[0] > other.rect.right:
            test_x = other.rect.right

        if self.center[1] < other.rect.top:
            test_y = other.rect.top
        elif self.center[1] > other.rect.bottom:
            test_y = other.rect.bottom

        dist_x = self.center[0] - test_x
        dist_y = self.center[1] - test_y

        dist = ((dist_x*dist_x)+(dist_y*dist_y))**0.5

        return dist <= self.radius

    def collideline(self, other):
        super().collideline(other)
        

    def collidecircle(self, other):
        super().collidepoint(other)
        dist = ((other.center[0] - self.center[0])**2 + \
                (other.center[1] - self.center[1])**2)**0.5
        if dist <= (self.radius + other.radius):
            return True
        return False
