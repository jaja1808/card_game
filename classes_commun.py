import numpy as np
import random as rd


colours = ("spades","hearts","diamonds","clubs")
card_names = ("7","8","9","10","ace","jack","king","queen")



# definition de la classe carte
class Game:
    def __init__(self):
        # Creation de l'instance Game
        self._player1=Player()
        self._player2=Player()
        self._player3=Player()
        self._player4=Player()
        self._Cards=[]


    def Players(self):
        tab=[]
        tab.append(self._player1)
        tab.append(self._player2)
        tab.append(self._player3)
        tab.append(self._player4)

        return tab
        
# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
# par defaut:# par defaut:
#joueur nom =Papi 
#Type =True (humain)
# main = [] (liste vide ) 
# Groupe = [] (liste vide ) 
    def Create_PLayer(self,player_number,name_player="Papi",type_player=True,hand=[],group=[]):
        if player_number == 1:
            player = self._player1
        elif player_number == 2:
            player = self._player2
        elif player_number == 3:
            player = self._player3
        elif player_number == 4:
            player = self._player4
        else:
            raise ValueError("la valeur doit etre comprise entre 1 et 4")

        # on definit le nom du joueur
        player.set_name_Player(name_player)

        # on definit la main du joueur
        player.set_hand(hand)
        
        # on definit la le type de joueur
        player.set_type_player(type_player)

        # on definit le groupe du joueur
        player.set_group(group)      

    # creation de toutes les cartes graces a la liste de 
    def Create_Cards(self):
        for colour in colours:
            for  name in card_names:
                card =Card(name,colour)
                self._Cards.append(card)

    #code pour verifier la creation des cartes  
    def print_Cards(self):
        for Card in self._Cards:
            print(Card.get_colour())

    # fonction pour melanger les cartes (battre les carte)
    def shuffle_Cards(self):
        self._Cards=rd.shuffle(self._Cards)
    
    # fonction pour distribuer 
    def Distribute(self,player,number_cards=5):
        if player == 1:
            player = self._player1
        elif player == 2:
            player = self._player2
        elif player == 3:
            player = self._player3
        elif player == 4:
            player = self._player4
        else:
            raise ValueError("la valeur doit etre comprise entre 1 et 4")

            """
        for i in range(number_cards):
            card=self._Cards[i]
            player.add_card_Hand(card)
            self._Cards.pop(i)
            """







        

class Card:

    # Constructor
    def __init__(self, card_name, colour, image=""):
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


class Player:
    def __init__(self,name_player="",type_player=False,hand=[],group=False):
        # nom du joueur
        # type= Chaine de caractere
        self._name_Player=name_player

        # la main du joueur
        # type= liste
        self._hand=hand

        # le type  du joueur(bool())
        # type= bool (true humain , False IA)
        self._type_player=type_player
        
        self._group=group

    def get_name_Player(self):
        return self._name_Player
    
    def get_player(self):
        return self._player
    
    def get_type_player(self):
        return self._type_player
    
    def get_group(self):
        return self._group
    

    def set_name_Player(self,name_Player):
       self._name_Player=name_Player
    
    def set_hand(self,hand):
        self._hand=hand

    def set_type_player(self,type_player):
        self._type_player=type_player   
    
    def set_group(self,group):
       self._group=group

    # fonction pour ajouter une carte a la main du joueur
    def add_card_Hand(self,Card):
        self._hand=self.self._hand.append(Card)

















