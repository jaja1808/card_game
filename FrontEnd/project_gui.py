import pygame as pg
import numpy as np
import time
from front_func import *
#from BackEnd.classes_backend import *
#from BackEnd.Principal import *
#from classes_commun import *

# Array for simulating events
Clicks = np.arange(0, 10)
#hand = ['7_of_diamonds.png', '7_of_spades.png', '7_of_hearts.png', '7_of_clubs.png','8_of_clubs.png','8_of_diamonds.png','8_of_hearts.png','8_of_spades.png']
hand = []
# Score array
score_array = np.arange(6)
# Inital angle of the arrow
angle = 0
step = 0

''' We start here fron the main program'''
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

    ''' new game button 
        return (integer) etape front == 200 '''


    ''' the input for the name and the declaration of the player 
        return name (string) and etape (integer) == 300 '''
    
    # Set background color
    game.fill(BACKGROUND)
    
    # Listening for Events
    for click in Clicks:

        # Always start with the back ground        
            game.fill(BACKGROUND)    

            ''' etape == 300, receive hand[], atout and choix atout(carte tapis) 
                from backend and sends Acknowledgement (int == 400 )'''

            # Calculate the rotation angle for the arrow
            angle += 90  # 90 to make 4 sides

            # Display the back card at position of all players
            back_card_1, back_card_rect_1 = display_card(400, 75, 'back_card.png')
            back_card_2, back_card_rect_2 = display_card(75, 300, 'back_card.png')
            back_card_4, back_card_rect_4 = display_card(725, 300, 'back_card.png')

            # Display the arrow and starting cards
            game.blit(back_card_1, back_card_rect_1)
            game.blit(back_card_2, back_card_rect_2)
            game.blit(back_card_4, back_card_rect_4)

            if dfc and click == 0:
              # Display the hand at the bottom
              display_hand(hand[:5]) 
              # Display pop-up on the third click
              display_popup('10_of_diamonds.png')
              dfc = False

              ''' if (pass) sends choix = 2 else choix = 1 , and receives geton for displaying (pass or not) if chosen recieve (atout)[display atout top corner]'''
            else:   
                if len(hand) != 0:
                    draw_arrow(10, 12, angle)
                    display_score(40,50)
                    display_hand(hand)

                else:
                    newGame_page()
                    #user_input()
                    #final_score(score_array)
                    time.sleep(1)
                    run = False

            # Timer for slowing the rotation
            #timer.tick(5)  # 2.5 for the rate of rotation

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
