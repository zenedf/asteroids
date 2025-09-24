import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # random r,g,b

    def draw(self, screen):
        # remove the 'width' to fill the circle
        pygame.draw.circle(screen, self.__color, self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt