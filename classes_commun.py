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

            
        for i in range(number_cards):
            card=self._Cards[i]
            player.add_card_Hand(card)
            self._Cards.pop(i)
        

    def display_players_hands(self):
            players = self.Players()
            for i, player in enumerate(players, start=1):
                print(f"\nPlayer {i}'s Hand:")
                hand = player.get_hand()

                if not hand:
                    print("Empty hand.")
                else:
                    for card in hand:
                        print(f"{card.get_name()} of {card.get_colour()}")

        






        

class Card:
    
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
    def __init__(self):
        # nom du joueur
        # type= Chaine de caractere
        self.name_Player=None 

        # la main du joueur
        # type= liste
        self._hand=None

        # le type  du joueur(bool())
        # type= bool (true humain , False IA)
        self._type_player=None
        
        self._group=None

    def get_name_Player(self):
        return self._name_Player
    
    def set_name_Player(self,name_Player):
       self._name_Player=name_Player
       
    #    a =P¨layer()
        # a.name_player=prince
        # X=a.name_player
        
    name_Player = property(get_name_Player,set_name_Player)

    
    def get_hand(self):
        return self._hand
    
    def set_hand(self,hand):
        self._hand=hand if hand is not None else []
    # definir une property
    hand=property(get_hand,set_hand)

    
    def get_type_player(self):
        return self._type_player
    
    def set_type_player(self,type_player):
        self._type_player=type_player 

    type_player=property(get_type_player,set_type_player)   

    def get_group(self):
        return self._group
    
    def set_group(self,group):
       self._group=group

    group=property(get_group,set_group)
    

    # fonction pour ajouter une carte a la main du joueur
    def add_card_Hand(self,Card):
        self.hand.append(Card)

    def remove_card_Hand(self,Card):
        self.hand.pop(Card)

















