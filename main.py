###
# check for player inputs
# update the game world
# draw the game to the screen
###

import pygame
from player import Player
from constants import *
# from circleshape import CircleShape


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Delta time
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while (True):
        screen.fill("black")  # Clear screen with black
        player.draw(screen)
        pygame.display.flip()   # Refresh the screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
