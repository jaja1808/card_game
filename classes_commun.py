import numpy as np
import random as rd


# definition de la classe carte
class carte:
    def __init__(self,nom_carte,couleur):
        self.__nom_carte=nom_carte
        self.__couleur=couleur

        # j'ajoute une test

# 
    def get_card_name(self):
        return self._card_name
    
    def get_colour(self):
        return self._colour
   
    def set_card_name(self,card_name):
        self._card_name=card_name
    
    def set_colour(self,colour):
        self._colour=colour


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



# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 















