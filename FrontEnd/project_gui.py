import pygame as pg
import numpy as np
import os

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Frames
FRAME_RATE = 60

# Colors
GREY = (155, 155, 155)
BACKGROUND = (0, 80, 20)

# Array for a simulation the events
Clicks = np.arange(0,10)

# Arrow for the game indication
image_path = "C:/Users/rusha/Documents/Sem_7/Computer_science/Project/code/images/"
arrow = pg.image.load(image_path + 'Arrow.png')
arrow_rect = arrow.get_rect(center = (GAME_WIDTH / 2 , GAME_HEIGHT / 2))

# Initializing pygame
pg.init()

# Creating game window 
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pg.display.set_caption("Belote Game")
timer = pg.time.Clock()
run = True

# Keep the game going 
while run:

    # Set background color
    game.fill(BACKGROUND)

 # Listening for Events
    for click in Clicks:
        # Calculate the rotation angle for the arrow
        # You can define the rotation logic based on how you want the clicks to affect it
        angle = click * 90  # Example: each click rotates the arrow 36 degrees

        # Rotate the arrow
        # The `rotozoom` method creates a new surface with the rotated arrow
        rotated_arrow = pg.transform.rotozoom(arrow, angle, 1)
        rotated_rect = rotated_arrow.get_rect(center=arrow_rect.center)

        # Display the arrow
        game.blit(rotated_arrow, rotated_rect.topleft)
    # Update the Display
    pg.display.flip()
    
    # Time rate
    timer.tick(FRAME_RATE)

    # Event Listen to Quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

# Quiting the game
pg.quit()            
