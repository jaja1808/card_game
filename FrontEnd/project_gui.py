import pygame as pg
import numpy as np
from front_func import *


# Array for simulating events
Clicks = np.arange(0, 10)
hand = ['7_of_diamonds.png', '7_of_spades.png', '7_of_hearts.png', '7_of_clubs.png']

angle = 0

# Initializing pygame
pg.init()

# Creating game window 
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pg.display.set_caption("Belote Game")
timer = pg.time.Clock()

# Variable for game 
run = True
# variable for the first display pop up
dfc = True

# Keep the game going 
while run:

    # Set background color
    game.fill(BACKGROUND)

    # Listening for Events
    for click in Clicks:

        # Always start with the back ground        
        game.fill(BACKGROUND)

        # Calculate the rotation angle for the arrow
        angle += 45  # 45 to make 4 sides

        # Draw and Rotate the arrow
        scaled_arrow, scaled_rect = draw_arrow(12, 10)
        rotated_arrow = pg.transform.rotozoom(scaled_arrow, angle, 1)
        rotated_rect = rotated_arrow.get_rect(center=scaled_rect.center)

        # Display the back card at position of all players
        back_card_1, back_card_rect_1 = display_card(2, 8, 'back_card.png')
        back_card_2, back_card_rect_2 = display_card(8, 2, 'back_card.png')
        back_card_4, back_card_rect_4 = display_card(1.15, 2, 'back_card.png')

        # Display the hand at the bottom
        display_hand(1, 1.15, hand)

        # Display the arrow and starting cards
        game.blit(rotated_arrow, rotated_rect)
        game.blit(back_card_1, back_card_rect_1)
        game.blit(back_card_2, back_card_rect_2)
        game.blit(back_card_4, back_card_rect_4)

        if dfc and click ==3:
          # Display pop-up on the first click
          display_popup('10_of_diamonds.png')
          dfc = False
        else:
            pass    

        # Timer for slowing the rotation
        timer.tick(10)  # 2.5 for the rate of rotation

    # Update the Display
    pg.display.flip()

    # Time rate
    timer.tick(FRAME_RATE)

    # Event Listen to Quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

# Quitting the game
pg.quit()
