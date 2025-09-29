import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def is_colliding(self, circle:'CircleShape'):
        r1 = self.radius
        r2 = circle.radius
        distance = self.position.distance_to(circle.position)
        return distance <= r1 + r2
    
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def get_position(self):
        return self.position