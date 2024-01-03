import pygame as pg

#IMPORTANT VARIABLES (STRUCTURE)

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

timer = pg.time.Clock()

# Atout array
#atout = ['spade.png','heart.png','diamond.png','club.png']
# Score array
#score_array = np.arange(6)

# Colors
GREY = (155, 155, 155)
BACKGROUND = (0, 80, 20)
BEIGE = (245, 245, 220)

# Frames
#FRAME_RATE = 60

# GAME SIZE DISPLAY
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


######################################################################################################################################

# Function to draw the centre arrow
def draw_arrow(angle, image_path):
    ''' 
        This function is for drawing Arrow pointing on the player to play in that instant
        the scale of reducing the size of Arrow picture in the game 10 and 12
        angle: the angle of rotation of the arrow
        image_path: the path to the images used in this game
    '''
    # Importing the image and reducing the size of the arrow
    arrow = pg.image.load(str(image_path / 'Arrow.png'))
    arrow_rect = arrow.get_rect(center=(GAME_WIDTH / 2, GAME_HEIGHT / 2))

    # Size reduction
    scaled_arrow = pg.transform.scale(arrow, (arrow.get_width() //10 , arrow.get_height() // 12))
    scaled_rect = scaled_arrow.get_rect(center=arrow_rect.center)
    
    # Draw and Rotate the arrow
    rotated_arrow = pg.transform.rotozoom(scaled_arrow, angle, 1)
    rotated_rect = rotated_arrow.get_rect(center=scaled_rect.center)

    # Display arrow
    game.blit(rotated_arrow, rotated_rect)

######################################################################################################################################

# Function to display back of the card in the size acceptable
def display_card(pos_x, pos_y, card_image, image_path):
    '''
        Pos_x: the position on the horizontal where you want to display the card 
        pos_y: the position on the vertical where you want to display the card
        card_image: image of the card
        image_path: the path to the images used in this game
    '''
    # Loading the image
    back_card = pg.image.load(str(image_path / card_image))
    back_card_rect = back_card.get_rect(center=(pos_x, pos_y))

    # Reducing the size of the image
    scaled_back_card = pg.transform.scale(back_card, (back_card.get_width() // 6, back_card.get_height() // 6))
    scaled_back_card_rect = scaled_back_card.get_rect(center=back_card_rect.center)

    return scaled_back_card, scaled_back_card_rect

######################################################################################################################################

# Function
def display_image(pos_x, pos_y, image, image_path):
    '''
        Pos_x: the position on the horizontal where you want to display the image
        pos_y: the position on the vertical where you want to display the image
        image: image to be displayed
        image_path: the path to the images used in this game
    '''
    # Loading the image
    im = pg.image.load(str(image_path / image))
    im_rect = im.get_rect(topleft = (pos_x, pos_y))

    return im, im_rect

######################################################################################################################################

# Function to draw the grid
def draw_grid(screen , color, width, height, grid_width, grid_height):
    '''
        screen: the surface of interest
        color : background color 
        width: width of the grid
        height: height of the grid
        grid_width: width of one grid rectangle
        grid_height: height of one grid rectangle 
    '''
    # Drawing the grid 
    for x in range(0, width, grid_width):
        pg.draw.line(screen, color, (x, 0), (x, height))
    for y in range(0, height, grid_height):
        pg.draw.line(screen, color, (0, y), (width, y))
    
######################################################################################################################################

# Function to create div-like elements
def draw_div(pos_x, pos_y, width, height, color):
    div_rect = pg.Rect(pos_x, pos_y, width, height)
    div = pg.draw.rect(game, color, div_rect)
    return div

######################################################################################################################################

# Function to Display the 3 cards of other players
def back_cards(image_path, names):
    '''
        this function is for displaying the back of the cards of other players 
    '''
    # Display the back card at position of all players
    
    # Font for the button words
    font = pg.font.SysFont('Arial', 14)

    back_card_1, back_card_rect_1 = display_card(400, 75, 'back_card.png',image_path)
    back_card_2, back_card_rect_2 = display_card(75, 300, 'back_card.png', image_path)
    back_card_4, back_card_rect_4 = display_card(725, 300, 'back_card.png', image_path)

    # Render text surfaces for player names
    name_surfaces = [font.render(name, True, BEIGE) for name in names]

    running = True
    while running:
        
        # Blit the cards and player names
        game.blit(back_card_1, back_card_rect_1)
        game.blit(back_card_2, back_card_rect_2)
        game.blit(back_card_4, back_card_rect_4)

        # Display player names above the cards
        for i, name_surface in enumerate(name_surfaces):
            card_rect = [back_card_rect_1, back_card_rect_2, back_card_rect_4][i]

            # Calculate the position to display the name above the card
            text_x = card_rect.centerx - name_surface.get_width() // 2
            text_y = card_rect.top - name_surface.get_height() - 2  # Place it above the card with a small margin

            game.blit(name_surface, (text_x, text_y))
        
        pg.display.flip()

        for event in pg.event.get():
           if event.type == pg.QUIT:
                running = False

######################################################################################################################################
# Function to create div-like elements
def first_page(image_path):
    '''
        this will create the first page to start the new game with a click of the button
        the next step will be called 
    '''
    # fille the background with dark green
    game.fill(BACKGROUND)
    etape = 200
    # Displaying the image of Belote for the first page
    first_image, first_image_rect = display_image(144, 0, 'Home.png', image_path)
    # Font for the button words
    font = pg.font.SysFont('Arial', 30)
    # Text on the button
    button_text = "New Game"
    color = (80, 80, 80)
    # Declare the button rectangle
    button_rect = pg.Rect(first_image_rect.bottomleft[0], first_image_rect.bottomleft[1]+ 10, first_image_rect.width, 50)
    pg.draw.rect(game, GREY, button_rect)
    # Creating the button surface
    button_surface = pg.Surface((button_rect.width, button_rect.height), pg.SRCALPHA)
    
    # Loop to handle events
    running = True
    while running:
        # get the position of the mouse
        mouse_pos = pg.mouse.get_pos()

        # checking the position of the mouse if it touches the button rectangle
        if button_rect.collidepoint(mouse_pos):
            color = (0, 0, 0)

        button_txt = font.render(button_text, True, color)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return etape
    
        # Calculate coordinates to center the text within the button
        text_x = (button_rect.width - button_txt.get_width()) // 2
        text_y = (button_rect.height - button_txt.get_height()) // 2
        
        button_surface.blit(button_txt, (text_x, text_y))  # Blit text onto button_surface at center

        game.blit(first_image,first_image_rect)
        game.blit(button_surface, button_rect)
    
        pg.display.flip()

######################################################################################################################################
    
# Function to give the user input page and get their name as well
def user_input(image_path):
    '''
        This function will take the name of the user and give it back to the system
        then call the next step
    ''' 
    # Fill the surface and declaring the variables
    game.fill(BACKGROUND)
    font = pg.font.SysFont('Arial', 28)
    etape = 300
    motor = True
    input_active = True  

    # important rectangles to be used along 
    home = pg.Rect(0, 0, GAME_WIDTH, GAME_HEIGHT)
    input_box = pg.Rect(GAME_WIDTH // 2 - 150, GAME_HEIGHT // 2 - 25, 280, 50)
    button = pg.Rect(input_box.right + 10, input_box.y, 80, 50)

    # Surfaces
    home_surface = pg.Surface((home.width, home.height), pg.SRCALPHA)
    input_surface = pg.Surface((input_box.width, input_box.height), pg.SRCALPHA)

    # Displaying the Image
    home_im, home_rect = display_image(0, 0, 'tapis_belote.png', image_path)
    home_surface.blit(home_im, home_rect)
    # Text to display initially
    initial_text = "Enter your name"
    user_text = ''
    # Text surface
    text_surface = font.render(user_text, True, (128, 128, 128))
    button_txt = font.render("OK", True, (0, 0, 255))
    
    while motor:

        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                motor = False

            if event.type == pg.MOUSEBUTTONDOWN:
                
                if input_box.collidepoint(event.pos):
                    input_active = True
                
                elif button.collidepoint(event.pos) and user_text != '':
                    input_active = False
                    motor = False
                    game.fill(BACKGROUND)
                    pg.display.flip()
                    return user_text, etape
                else:
                    input_active = False
                    text_surface = font.render(initial_text, True, (128, 128, 128))

            if event.type == pg.KEYDOWN:
                if input_active:
                    
                    if event.key == pg.K_BACKSPACE:
                        user_text = user_text[:-1]

                    elif event.key == pg.K_RETURN:
                        input_active = False
                        motor = False
                        return user_text, etape
                    
                    else:
                        user_text += event.unicode
                
        pg.draw.rect(home_surface, BEIGE, input_box)
        pg.draw.rect(home_surface, GREY, button)
        home_surface.blit(button_txt, (button.centerx - button_txt.get_width() // 2, button.centery - button_txt.get_height() // 2))

        if user_text == '':
            text_surface = font.render(initial_text, True, (128, 128, 128))
        elif text_surface.get_width() > input_box.width - 10:
            user_text = ''  # Clear the user text
        else:
            text_surface = font.render(user_text, True, (0, 0, 0))
        
        home_surface.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        home_surface.blit(input_surface, (input_box.x, input_box.y))
        game.blit(home_surface, (home.x, home.y))

        pg.display.flip()

######################################################################################################################################

#  Function to draw buttons in the pop-up div
def draw_atout(popup_rect, button_width, button_height, atout, image_path):
    '''
        This function is to display the atout and  displaying the options to the user who will then respond and make a choice
        popup_rect: canvas rectangle to be drawn on
        button width and height: the width and height of the buttons as the user chooses
        atout: color of the cards proporsed 
    '''
    # loading the images of atout to be used in the game
    spade_image = pg.image.load(str(image_path / atout[0])) 
    space_resized = pg.transform.scale(spade_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image
    heart_image = pg.image.load(str(image_path / atout[1]))
    heart_resized = pg.transform.scale(heart_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image 
    diamond_image = pg.image.load(str(image_path / atout[2])) 
    diamond_resized = pg.transform.scale(diamond_image,(spade_image.get_width() // 2, spade_image.get_height() // 2)) # reducing the size of atout image
    club_image = pg.image.load(str(image_path / atout[3])) 
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
                    input = False 
                    return atout[2]

######################################################################################################################################

# Function to display pop-up with buttons and card image
def display_popup(card_image, image_path, atout):
    '''
        This function is for displaying the whole atout and proposed card step where the user will make a choice for the progrss of the game
        card_image: the card proposed by the back end as atout
        atout: the list of card color of the game
    '''
    # size of the pop-up
    popup_width = 150
    popup_height = 200
    popup_rect = pg.Rect((GAME_WIDTH - popup_width) // 2, (GAME_HEIGHT - popup_height) // 2, popup_width, popup_height)

    # Draw background
    pg.draw.rect(game, BACKGROUND, popup_rect) # change background to grey to see it

    # Display card image
    card, card_rect = display_card(2, 2, card_image, image_path)
    game.blit(card, (popup_rect.centerx - card_rect.width // 2, popup_rect.centery - card_rect.height/1.25))

    # Display buttons
    button_width = 50
    button_height = 25

    # loading the images of atout to be used in the game
    atout_image = pg.image.load(str(image_path / atout[0])) #loading the atout images
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
                    return 2
                elif no_button_rect.collidepoint(mouse_pos):
                    pg.draw.rect(game, BACKGROUND, no_button_rect)
                    atout_ch = draw_atout(popup_rect, button_width, button_height)
                    print(f'Atout is:{atout_ch}')
                    waiting_for_input = False
                    return atout_ch

######################################################################################################################################

# Function to display a hand of cards
def display_hand(hand, image_path):
    ''' 
        This function will display the hand of the player and will handle the size and display as the game progress
        hand: the hand of the player from front end
    '''
    
    total_card_width = sum(pg.image.load(str(image_path / card)).get_width()/12 for card in hand) # 12 from 6 of display card and 2 for half image
    spacing = 10  # Adjust this value to control the spacing between cards

    x = ( GAME_WIDTH - (total_card_width + (spacing * len(hand))+ 42)) / 2  # Starting x-coordinate for centering 

    mouse_x, mouse_y = pg.mouse.get_pos()

    for card in hand:
        card_image, card_rect = display_card(x, GAME_HEIGHT - 135, card, image_path)

        # Check if the mouse is over the scaled card
        scaled_rect = pg.Rect(x, GAME_HEIGHT - 135, card_rect.width/2, card_rect.height)

        if scaled_rect.collidepoint(mouse_x, mouse_y):
            card_image = pg.transform.scale(card_image, (int(card_rect.width * 1.1), int(card_rect.height * 1.1)))

            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN: # and angle == 270: # to be added later
                    print(f'Clicked on: {card}')
                    hand.remove(card)
                    #display played cards
                    display_tapis(card, '10_of_diamonds.png', '10_of_clubs.png', '10_of_hearts.png')

        game.blit(card_image, (x, GAME_HEIGHT - 135))
        x += card_rect.width / 2 + spacing  # Adjust spacing between cards

    pg.display.flip()

######################################################################################################################################

# Function to display cards on the tapis
def display_tapis(tapis, image_path): 
        '''
            This function will display the cards played by the 4 players
            tapis: array cards of the round played 
        '''
        # Display the cards at position of all players
        card_1, card_rect_1 = display_card(440, 220, tapis[0], image_path)
        card_2, card_rect_2 = display_card(360, 220, tapis[1], image_path)
        card_3, card_rect_3 = display_card(360, 340, tapis[2], image_path)
        card_4, card_rect_4 = display_card(440, 340, tapis[3], image_path)
        
        # Display the cards on the tapis
        game.blit(card_1, card_rect_1)
        game.blit(card_2, card_rect_2)
        game.blit(card_3, card_rect_3)
        game.blit(card_4, card_rect_4)

######################################################################################################################################

# Function to Display the score board
def display_score(us, them):
    '''
        This function will display the score as the game progresses
        us: score of the user and his partner
        them: the score of the opposing team
    '''
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

######################################################################################################################################

# Final score Window
def final_score(score_array, image_path): # to be completed
    '''
        This function will display the final page with the total scores and the verdict of the game
        score array: belote score '''

    score = pg.Rect(10, 10, 530, 270)
    table = pg.Rect(500, 350, 280, 200)

    # Draw the final score and making it the base surface
    game.fill(BACKGROUND)
    score_surface = pg.Surface((score.width, score.height), pg.SRCALPHA)
    table_surface = pg.Surface((table.width, table.height), pg.SRCALPHA)

    # Displaying the Image
    bacG, bacG_rect = display_image(10, 10, 'back_gound_score.png', image_path)
    score_surface.blit(bacG, bacG_rect)
    
    if score_array[1] > score_array[2]:
        color = (0, 255, 0)
        sentence = 'WIN'
    else:
        color = (255, 0, 0)
        sentence = 'LOOSE'

    pg.draw.rect(game, color, score)
    pg.draw.rect(game, BEIGE, table)

    # Creating the font for Score
    font = pg.font.SysFont('Arial',34) # Arial font
    word = font.render(sentence, True, color) # the win message
    tot_score_us = font.render('US: '+str(score_array[1]), True, (0, 0, 0))
    tot_score_them = font.render('THEM: '+str(score_array[2]), True, (0, 0, 0))

    # Creating the grid in Table
    draw_grid(table_surface, (0, 0, 0), table.width, table.height, 140, 50)

    game.blit(word, (score.centerx - 50, score.centery + 200))
    game.blit(score_surface, (score.x, score.y))
    game.blit(table_surface, (table.x, table.y))

    pg.display.flip()

#########################################################################################################################
