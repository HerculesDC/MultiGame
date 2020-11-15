"""
    OBS.: This class is used for graphical effects only. Does not take
          physics simulations accurately
"""
import random #relies on Game seeding the random
from pygame.locals import *
from pygame import Color, Rect, Surface, Vector2
from engine.behaviour import Behaviour

class Meteors(Behaviour):
    def __init__(self, size = (0, 0)):
        super().__init__("Meteors")
        #config
        self._bounce_area = size
        self._num_meteors = 10

        #containers
        self._meteors_pos = []
        self._meteors_speeds = []
        
        #meteor attributes
        self._meteor_colour = Color(250, 175, 25)
        self._meteor_radius = 10
        self._max_speed = 0.0075
        self._num_coords = self._num_meteors << 1
        self._rect = Rect(0, 0, 2*self._meteor_radius, 2*self._meteor_radius)
        self._surf = Surface((2*self._meteor_radius, 2*self._meteor_radius), SRCALPHA)
        
    def start(self):
        for i in range(0, self._num_coords):
            temp = i%2 == 0
            self._meteors_pos.append(\
                random.randrange(1, self._bounce_area[0]-self._meteor_radius)*(temp)+
                random.randrange(1, self._bounce_area[1]-self._meteor_radius)*(not temp))
            sp = 0
            while -0.001 < sp < 0.001:
                sp = random.uniform(-self._max_speed, self._max_speed)
            self._meteors_speeds.append(sp)
        import pygame.draw
        pygame.draw.circle(self._surf, self._meteor_colour, self._rect.center,
                           self._meteor_radius)
        super().start()
        
    def update(self, delta):
        temp_width = self._bounce_area[0] - (2*self._meteor_radius)
        temp_height = self._bounce_area[1] - (2*self._meteor_radius)
        for i in range(0, self._num_coords):
            temp = i%2==0
            self._meteors_pos[i] = int(self._meteors_pos[i]+
                                       self._meteors_speeds[i]*self._bounce_area[not temp])
            self._meteors_speeds[i] *= Meteors.bounce(self._meteors_pos[i],
                                                   self._meteors_speeds[i],
                                                   (temp_width*(temp)+
                                                    temp_height*(not temp)))
        super().update(delta)

    def render(self):
        super().render()
        from engine.game_env import Game
        for i in range(0, self._num_coords, 2):
            #incomplete resize logic. May cause errors in small windows. Check
            Game.instance.get_screen().blit(self._surf,
                                           (int(self._meteors_pos[i]),
                                            int(self._meteors_pos[i+1])))

    def get_bounce_area(self):
        return self._bounce_area
    
    def set_bounce_area(self, area):
        if isinstance(area, (tuple, list, Vector2)):
            reposition = []
            for i in range(self._num_coords):
                temp = i%2==0
                new_coord = float(self._meteors_pos[i]/
                                        (self._bounce_area[0]*temp +
                                         self._bounce_area[1]*(not temp)))
                if new_coord < 0.01:
                    new_coord = 0.01
                elif new_coord > 1:
                    new_coord = 0.99
                reposition.append(new_coord)
            if len(area) >= 2:
                self._bounce_area = (int(area[0]), int(area[1]))
                for i in range(self._num_coords):
                    self._meteors_pos[i] = int(self._meteors_pos[i]*reposition[i])
            else:
                raise ValueError("Not enough data to resize")
        else:
            raise TypeError("Incorrect area type")
        
    
    @staticmethod
    def bounce(pos, speed, max_):
        return 1 - 2*(pos + speed < 0 or pos + speed > max_)
