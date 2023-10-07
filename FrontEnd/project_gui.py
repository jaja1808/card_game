import pygame as pg
import os

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Frames
FRAME_RATE = 60

# Colors
GREY = (155, 155, 155)
BACKGROUND = (0, 80, 20)

# card objects 

# button objects

# score

# Menu

# Pointer

# Player objects

# Play options


# Initializing pygame
pg.init()

# Creating game window 
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pg.display.set_caption("Belote Game")
timer = pg.time.Clock()
run = True

# Keep the game going 
while run:

    # Event Listen to Quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Set background color
    game.fill(BACKGROUND)        
    
    # Update the Display
    pg.display.flip()

    # Time rate
    timer.tick(FRAME_RATE)

# Quiting the game
pg.quit()            
