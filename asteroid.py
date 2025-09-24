import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, screen):
        pygame.draw.circle(screen, self.__color, self.position, self.radius)
        # pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt