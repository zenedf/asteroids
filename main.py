###
# check for player inputs
# update the game world
# draw the game to the screen
###

import pygame
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while (True):
        screen.fill((0, 0, 0))  # Clear screen with black
        pygame.display.flip()   # Refresh the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
