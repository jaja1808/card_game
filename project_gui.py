import pygame

# Initializing pygame
pygame.init()

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Creating game window 
game = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

run = True
# Keep the game going 
while run:

    # Background color
    game.fill((0, 106, 78))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()            
# card objects 

# button objects

# score

# Menu

# Pointer

# Player objects

# Play options
