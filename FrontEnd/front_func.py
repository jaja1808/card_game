import pygame as pg

#IMPORTANT VARIABLES 

# Images path
image_path = "C:/Users/rusha/Documents/Sem_7/Computer_science/Project/code/images/"

# Size of the game window
GAME_WIDTH = 800
GAME_HEIGHT = 600

# Colors
GREY = (155, 155, 155)
BACKGROUND = (0, 80, 20)

# Frames
FRAME_RATE = 60

# GAME SIZE DISPLAY
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))


# Function to draw the centre arrow
def draw_arrow(pos_x, pos_y):
    arrow = pg.image.load(image_path + 'Arrow.png')
    arrow_rect = arrow.get_rect(center=(GAME_WIDTH / 2, GAME_HEIGHT / 2))
    scaled_arrow = pg.transform.scale(arrow, (arrow.get_width() // pos_x, arrow.get_height() // pos_y))
    scaled_rect = scaled_arrow.get_rect(center=arrow_rect.center)
    return scaled_arrow, scaled_rect


# Function to display back of the card
def display_card(pos_x, pos_y, card_image):
    back_card = pg.image.load(image_path + card_image)
    back_card_rect = back_card.get_rect(center=(GAME_WIDTH / pos_x, GAME_HEIGHT / pos_y))
    scaled_back_card = pg.transform.scale(back_card, (back_card.get_width() // 6, back_card.get_height() // 6))
    scaled_back_card_rect = scaled_back_card.get_rect(center=back_card_rect.center)
    return scaled_back_card, scaled_back_card_rect


# Function to create div-like elements
def draw_div(pos_x, pos_y, width, height, color):
    div_rect = pg.Rect(pos_x, pos_y, width, height)
    pg.draw.rect(game, color, div_rect)


# Function to display pop-up with buttons and card image
def display_popup(card_image):

    popup_width = 150
    popup_height = 200
    popup_rect = pg.Rect((GAME_WIDTH - popup_width) // 2, (GAME_HEIGHT - popup_height) // 2, popup_width, popup_height)

    # Draw background
    pg.draw.rect(game, BACKGROUND, popup_rect)

    # Display card image
    card, card_rect = display_card(2, 2, card_image)
    game.blit(card, (popup_rect.centerx - card_rect.width // 2, popup_rect.centery - card_rect.height // 2))

    # Display buttons
    button_width = 50
    button_height = 25
    yes_button_rect = pg.Rect(popup_rect.centerx - button_width - 10, popup_rect.bottom - button_height - 10, button_width, button_height)
    no_button_rect = pg.Rect(popup_rect.centerx + 10, popup_rect.bottom - button_height - 10, button_width, button_height)

    pg.draw.rect(game, (255, 0, 0), yes_button_rect)
    pg.draw.rect(game, (0, 255, 0), no_button_rect)

    font = pg.font.Font(None, 36)
    text_yes = font.render("Yes", True, (255, 255, 255))
    text_no = font.render("No", True, (255, 255, 255))

    game.blit(text_yes, (yes_button_rect.centerx - text_yes.get_width() // 2, yes_button_rect.centery - text_yes.get_height() // 2))
    game.blit(text_no, (no_button_rect.centerx - text_no.get_width() // 2, no_button_rect.centery - text_no.get_height() // 2))

    pg.display.flip()

    # Wait for player input
    waiting_for_input = True
    while waiting_for_input:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                if yes_button_rect.collidepoint(mouse_pos):
                    waiting_for_input = False
                elif no_button_rect.collidepoint(mouse_pos):
                    waiting_for_input = False

        pg.time.Clock().tick(FRAME_RATE)

# Function to display a hand of cards
def display_hand(x, y, hand):

    for card in hand:
        # Take each card from the hand array
        card_d, card_rect = display_card(x, y, card)
        game.blit(card_d, card_rect)
        # Change the coordinates
        x += 0.1 