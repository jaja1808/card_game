import pygame as pg

#IMPORTANT VARIABLES 

# Images path
image_path = "C:/Users/rusha/Documents/Sem_7/Computer_science/Project/code/images/"

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Inital angle of the arrow
angle = 0

# Atout array
atout = ['spade.png','heart.png','diamond.png','club.png']
# Colors
GREY = (155, 155, 155)
BACKGROUND = (0, 80, 20)
BEIGE = (245, 245, 220)

# Frames
FRAME_RATE = 60

# GAME SIZE DISPLAY
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


# Function to draw the centre arrow
def draw_arrow(pos_x, pos_y, angle):
    arrow = pg.image.load(image_path + 'Arrow.png')
    arrow_rect = arrow.get_rect(center=(GAME_WIDTH / 2, GAME_HEIGHT / 2))
    scaled_arrow = pg.transform.scale(arrow, (arrow.get_width() // pos_x, arrow.get_height() // pos_y))
    scaled_rect = scaled_arrow.get_rect(center=arrow_rect.center)
    
    # Draw and Rotate the arrow
    rotated_arrow = pg.transform.rotozoom(scaled_arrow, angle, 1)
    rotated_rect = rotated_arrow.get_rect(center=scaled_rect.center)
    # Display arrow
    game.blit(rotated_arrow, rotated_rect)


# Function to display back of the card
def display_card(pos_x, pos_y, card_image):
    back_card = pg.image.load(image_path + card_image)
    back_card_rect = back_card.get_rect(center=(pos_x, pos_y))
    scaled_back_card = pg.transform.scale(back_card, (back_card.get_width() // 6, back_card.get_height() // 6))
    scaled_back_card_rect = scaled_back_card.get_rect(center=back_card_rect.center)
    return scaled_back_card, scaled_back_card_rect


# Function to create div-like elements
def draw_div(pos_x, pos_y, width, height, color):
    div_rect = pg.Rect(pos_x, pos_y, width, height)
    div = pg.draw.rect(game, color, div_rect)
    return div

#  Function to draw buttons in the pop-up div
def draw_atout(popup_rect, button_width, button_height):
    # loading the images of atout to be used in the game
    spade_image = pg.image.load(image_path+ atout[0]) 
    space_resized = pg.transform.scale(spade_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image
    heart_image = pg.image.load(image_path+ atout[1])
    heart_resized = pg.transform.scale(heart_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image 
    diamond_image = pg.image.load(image_path+ atout[2]) 
    diamond_resized = pg.transform.scale(diamond_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image
    club_image = pg.image.load(image_path+ atout[3]) 
    club_resized = pg.transform.scale(club_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image

    # Creating the rectanges of the buttons 
    spade_button_rect = pg.Rect(popup_rect.centerx - button_width + 10, popup_rect.bottom - button_height - 40, space_resized.get_width(), space_resized.get_height())
    heart_button_rect = pg.Rect(popup_rect.centerx + 15, popup_rect.bottom - button_height - 40, space_resized.get_width(), space_resized.get_height())
    club_button_rect = pg.Rect(popup_rect.centerx + 15, popup_rect.bottom - button_height - 10, space_resized.get_width(), space_resized.get_height())
    diamond_button_rect = pg.Rect(popup_rect.centerx - button_width + 10, popup_rect.bottom - button_height - 10, space_resized.get_width(), space_resized.get_height())

    # Display the buttons
    game.blit(space_resized, (spade_button_rect.centerx - space_resized.get_width() //2, spade_button_rect.centery - space_resized.get_height() //2))
    game.blit(heart_resized, (heart_button_rect.centerx - space_resized.get_width() //2, heart_button_rect.centery - space_resized.get_height() //2))
    game.blit(diamond_resized, (diamond_button_rect.centerx - space_resized.get_width() //2, diamond_button_rect.centery - space_resized.get_height() //2))
    game.blit(club_resized, (club_button_rect.centerx - space_resized.get_width() //2, club_button_rect.centery - space_resized.get_height() //2))

    pg.display.flip()

    # Wait for player input
    input = True
    while input:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN: # Listen for the mouse click
                mouse_pos = pg.mouse.get_pos()
                if spade_button_rect.collidepoint(mouse_pos):
                    input = False
                    return atout[0]
                elif heart_button_rect.collidepoint(mouse_pos):
                    input = False
                    return atout[1]
                elif club_button_rect.collidepoint(mouse_pos):
                    input = False
                    return atout[3]
                elif diamond_button_rect.collidepoint(mouse_pos):
                    input = False  #print(f'your atout is: {atout[2]}') # testing 
                    return atout[2]



# Function to display pop-up with buttons and card image
def display_popup(card_image):
    # size of the pop-up
    popup_width = 150
    popup_height = 200
    popup_rect = pg.Rect((GAME_WIDTH - popup_width) // 2, (GAME_HEIGHT - popup_height) // 2, popup_width, popup_height)

    # Draw background
    pg.draw.rect(game, BACKGROUND, popup_rect) # change background to grey to see it

    # Display card image
    card, card_rect = display_card(2, 2, card_image)
    game.blit(card, (popup_rect.centerx - card_rect.width // 2, popup_rect.centery - card_rect.height/1.25))

    # Display buttons
    button_width = 50
    button_height = 25

    # loading the images of atout to be used in the game
    atout_image = pg.image.load(image_path+ atout[0]) #loading the atout images
    atout_resized = pg.transform.scale(atout_image,(atout_image.get_width() // 2, atout_image.get_height() // 2)) # reducing the size of atout image
    
    # Creating the rectanges of the buttons  ()
    yes_button_rect = pg.Rect(popup_rect.centerx - button_width + 10, popup_rect.bottom - button_height - 40, atout_resized.get_width(), atout_resized.get_height())
    no_button_rect = pg.Rect(popup_rect.centerx, popup_rect.bottom - button_height - 40, button_width - 5, button_height)

    pg.draw.rect(game, BACKGROUND, no_button_rect) # change background to grey to see it
    pg.draw.rect(game, BACKGROUND, yes_button_rect) # change background to grey to see it
    
    # Creating the font for first choice
    font = pg.font.SysFont('Arial',25) # Arial font
    text_no = font.render("Pass", True, (0, 0, 0))

    # Diplaying the buttons   
    game.blit(atout_resized, (yes_button_rect.centerx - atout_resized.get_width() //2, yes_button_rect.centery - atout_resized.get_height() //2))
    game.blit(text_no, (no_button_rect.centerx - text_no.get_width() // 2, no_button_rect.centery - text_no.get_height() // 2))

    pg.display.flip()

    # Wait for player input
    waiting_for_input = True
    while waiting_for_input:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN: # Listen for the mouse click
                mouse_pos = pg.mouse.get_pos()
                if yes_button_rect.collidepoint(mouse_pos):
                    waiting_for_input = False
                    print(f'Atout is:{atout[0]}')
                    return atout[0]
                elif no_button_rect.collidepoint(mouse_pos):
                    pg.draw.rect(game, BACKGROUND, no_button_rect)
                    atout_ch = draw_atout(popup_rect, button_width, button_height)
                    print(f'Atout is:{atout_ch}')
                    waiting_for_input = False


# Function to display a hand of cards
def display_hand(hand):
    
    total_card_width = sum(pg.image.load(image_path + card).get_width()/12 for card in hand) # 12 from 6 of display card and 2 for half image
    spacing = 10  # Adjust this value to control the spacing between cards

    x = ( GAME_WIDTH - (total_card_width + (spacing * len(hand))+ 42)) / 2  # Starting x-coordinate for centering 

    mouse_x, mouse_y = pg.mouse.get_pos()

    for card in hand:
        card_image, card_rect = display_card(x, GAME_HEIGHT - 135, card)

        # Check if the mouse is over the scaled card
        scaled_rect = pg.Rect(x, GAME_HEIGHT - 135, card_rect.width/2, card_rect.height)

        if scaled_rect.collidepoint(mouse_x, mouse_y):
            card_image = pg.transform.scale(card_image, (int(card_rect.width * 1.1), int(card_rect.height * 1.1)))

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN :  #and angle == 270: # to be added later
                    print(f'Clicked on: {card}')
                    hand.remove(card)
                    #display played cards
                    display_tapis(card, '10_of_diamonds.png', '10_of_clubs.png', '10_of_hearts.png')

        game.blit(card_image, (x, GAME_HEIGHT - 135))
        x += card_rect.width / 2 + spacing  # Adjust spacing between cards

    pg.display.flip()


# Function to display cards on the tapis
def display_tapis(card_1, card_2, card_3, card_4):
        
        # Display the cards at position of all players
        card_1, card_rect_1 = display_card(440, 220, card_1)
        card_2, card_rect_2 = display_card(360, 220, card_2)
        card_3, card_rect_3 = display_card(360, 340, card_3)
        card_4, card_rect_4 = display_card(440, 340, card_4)
        
        # Display the cards on the tapis
        game.blit(card_1, card_rect_1)
        game.blit(card_2, card_rect_2)
        game.blit(card_3, card_rect_3)
        game.blit(card_4, card_rect_4)


# Function to Display the score board
def display_score(us, them):

    # Positions
    position_x  = 10
    position_y = 10

    # Draw the div for score 
    score = draw_div(position_x, position_y, 50, 60, BACKGROUND)
    
    # Creating the font for Score
    font = pg.font.SysFont('Arial',14) # Arial font

    score_us = font.render('US: '+str(us), True, BEIGE)
    score_them = font.render('THEM: '+str(them), True, BEIGE)

    # Display on game
    game.blit(score_us, (score.centerx - 24, score.centery - 30))
    game.blit(score_them, (score.centerx - 25, score.centery - 10))

# Final score Window
def final_score():

    score = pg.Rect(100, 100, 600, 400)
    # Draw the final score
    game.fill(BACKGROUND)
    pg.draw.rect(game, BEIGE, score)

    # The rest will go here
    
    
    pg.display.flip()