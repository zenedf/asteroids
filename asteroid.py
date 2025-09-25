import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # random r,g,b
        self.__color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        ) 

    def draw(self, screen):
        # remove the 'width' to fill the circle
        pygame.draw.circle(screen, self.__color, self.position, self.radius, 2)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return # this was a small asteroid, do not split
        random_angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2
        return [new_asteroid1, new_asteroid2]
        
    def update(self, dt):
        self.position += self.velocity * dt