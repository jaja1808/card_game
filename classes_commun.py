import numpy as np
import random as rd


# definition de la classe carte
class Game:
    def __init__(self,player1,player2,player3,player4):
        pass
    #def game_creation(self):
        

class Card:

    # Constructor
    def __init__(self, card_name, colour, image):
        self._card_name = card_name
        self._colour = colour
        self._image = image
        # j'ajoute une test

    # Name Getter  
    def get_card_name(self):
        return self._card_name
    
    # Colour Getter 
    def get_colour(self):
        return self._colour
    
    # Image Getter
    def get_image(self):
        return self._image
    
    # Name setter
    def set_card_name(self, card_name):
        self._card_name = card_name
    
    # Colour setter
    def set_colour(self, colour):
        self._colour = colour

    # Image setter
    def set_image(self, image):
        self._image = image


# définition de la classe carte  attouf
class Asset_card(Card):
    def __init__(self, card_name, colour, score):
        super().__init__(card_name, colour)
        self._score=score

    def get_score(self):
        return self._score
    
    def set_score(self, score):
        self._score=score


# définition de la classe  non attouf(normal)
class Normal_card(Card):
    def __init__(self, card_name, colour, score):
        super().__init__(card_name, colour)
        self._score=score

    def get_score(self):
        return self._score
    
    def set_score(self,score):
        self._score=score


