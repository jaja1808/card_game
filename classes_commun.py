import numpy as np
import random as rd


# definition de la classe carte
class Game:
    def __init__(self):
        # Creation de l'instance Game
        self._player1=None
        self._player2=None
        self._player3=None
        self._player4=None


# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
    def CreatePLayer1(self,name_player,type_player,hand,groupe):
        self._player1=Player(name_player,type_player,hand,groupe)

# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
    def CreatePLayer2(self,name_player,type_player,hand,groupe):
        self._player2=Player(name_player,type_player,hand,groupe)
      
# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
    def CreatePLayer3(self,name_player,type_player,hand,groupe):
        self._player3=Player(name_player,type_player,hand,groupe)  


# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
    def CreatePLayer4(self,name_player,type_player,hand,groupe):
        self._player4=Player(name_player,type_player,hand,groupe)  
    



class Card:
    colour = ("spades","hearts","diamonds","clubs")
    card_name = ("7","8","9","10","ace","jack","king","queen")
    
    def __init__(self,card_name,colour):
        self._card_name=card_name
        self._colour=colour

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


class Player:
    def __init__(self,name_player,type_player,hand,groupe):
        self._name_Player=name_player
        self._player=hand
        self._groupe=groupe

    def get_name_Player(self):
        return self._name_Player
    
    def get_player(self):
        return self._player
    
    def get_groupe(self):
        return self._groupe
    

    def set_name_Player(self,name_Player):
       self._name_Player=name_Player
    
    def set_player(self,player):
        self._player=player
    
    def set_group(self,group):
       self._groupe=group

















