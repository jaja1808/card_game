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
angle = 0

# Image folder path
image_path = "C:/Users/rusha/Documents/Sem_7/Computer_science/Project/code/images/"

# Function to draw the centre arrow
def draw_arrow(pos_x,pos_y):
    # Arrow for the game indication
    arrow = pg.image.load(image_path + 'Arrow.png')
    arrow_rect = arrow.get_rect(center = (GAME_WIDTH / 2 , GAME_HEIGHT / 2))
    # Scale the arrow to 12.5% size 
    scaled_arrow = pg.transform.scale(arrow, (arrow.get_width()//pos_x, arrow.get_height()//pos_y))
    scaled_rect = scaled_arrow.get_rect(center=arrow_rect.center)
    return scaled_arrow, scaled_rect

# Function to display back of the card
def display_card(pos_x, pos_y, card_name):
    # Load the bach face of the cards
    back_card = pg.image.load(image_path + card_name)
    back_card_rect = back_card.get_rect(center = (GAME_WIDTH /pos_x, GAME_HEIGHT /pos_y))
    # Scale the Back card to 12.5% size 
    scaled_back_card = pg.transform.scale(back_card, (back_card.get_width()//8, back_card.get_height()//8))
    scaled_back_card_rect = scaled_back_card.get_rect(center=back_card_rect.center)
    return scaled_back_card, scaled_back_card_rect

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
        angle += 45 # 45 to make 4 sides
        
        # Draw and Rotate the arrow
        scaled_arrow, scaled_rect = draw_arrow(12,10)
        rotated_arrow = pg.transform.rotozoom(scaled_arrow, angle, 1)
        rotated_rect = rotated_arrow.get_rect(center=scaled_rect.center)

        # Display the back card at position of all players
        back_card_1, back_card_rect_1 = display_card(2, 8, 'back_card.jpg')
        back_card_2, back_card_rect_2 = display_card(8, 2, 'back_card.jpg')
        back_card_3, back_card_rect_3 = display_card(2, 1.15, 'ace_of_clubs.png')
        back_card_4, back_card_rect_4 = display_card(1.15, 2, 'back_card.jpg')
       
        # Display the arrow and starting cards
        game.fill(BACKGROUND)
        game.blit(rotated_arrow, rotated_rect.topleft)
        game.blit(back_card_1, back_card_rect_1)
        game.blit(back_card_2, back_card_rect_2)
        game.blit(back_card_3, back_card_rect_3)
        game.blit(back_card_4, back_card_rect_4)

        # Timer for slowing the rotaion
        timer.tick(10) # 2.5 for the rate of rotation
 
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
