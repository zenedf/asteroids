"""

check for player inputs
update the game world
draw the game to the screen

"""

import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from circleshape import CircleShape
from shot import Shot
from coordinates import display_coords


def test_coords(screen, font, player, asteroids):
            # Display coordinates for different objects
            display_coords(screen, font, player, "yellow")
            display_coords(screen, font, pygame.mouse, "white", -25)
            
            # Display coordinates for asteroids
            asteroid_list = list(asteroids)
            for i, asteroid in enumerate(asteroid_list):
                display_coords(screen, font, asteroid, "white")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)  # font for mouse coordinates
    dt = 0 # delta time
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)
    
    asteroid_field = AsteroidField() # disable this line to stop asteroids from spawning
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while (True):
        ms = clock.tick(60) # milliseconds = Cap the frame rate at 60 FPS
        dt = ms / 1000      # delta_time = Convert milliseconds to seconds
        updateable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.is_colliding(bullet):
                    bullet.kill()
                    asteroid.split()
        screen.fill("black")  # Clear screen with black
        for sprite in drawable:
            sprite.draw(screen)

        # Display coordinates for debugging
        test_coords(screen, font, player, asteroids)

        # Refresh the screen
        pygame.display.flip()
        # If player clicks the window close button, exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    
if __name__ == "__main__":
    main()