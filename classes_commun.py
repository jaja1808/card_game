import numpy as np
import random as rd


colours = ("spades","hearts","diamonds","clubs")
card_names = ("7","8","9","10","ace","jack","king","queen")

#---------------------------------------------------------------------------------------------------------------------------------------

def valeur_non_atout(nom_carte):

    if nom_carte== "7":
        return 0
   
    if nom_carte== "8":
        return 0
    
    if nom_carte== "9":
        return 0

    if nom_carte== "10":
        return 10
    
    if nom_carte== "ace":
        return 11

    if nom_carte== "jack":
        return 2
    
    if nom_carte== "king":
        return 4
    if nom_carte== "queen":
        return 3
   
def valeur_atout(nom_carte):

    if nom_carte== "7":
        return 0
   
    if nom_carte== "8":
        return 0
    
    if nom_carte== "9":
        return 14

    if nom_carte== "10":
        return 10
    
    if nom_carte== "ace":
        return 11

    if nom_carte== "jack":
        return 20
    
    if nom_carte== "king":
        return 4
    if nom_carte== "queen":
        return 3
      
    

def calcul_score_tapis(tapis):
    score=0
    for card in tapis:
        score =score + card.score

    return score    




#---------------------------------------------------------------------------------------------------------------------------------------

# definition de la classe carte
class Game:
    def __init__(self):
        # Creation de l'instance Game

        #les joueurs(joueur)
        self._player1=None
        self._player2=None
        self._player3=None
        self._player4=None

        #liste de cartes (32)
        self._cards=None
        self._tapis=None

        # choix = card
        self._choix=None
        self._choix_attout_color=None
        # jeton du joueur
        #joueur1 =270
        #joueur2 =180
        #joueur3 =90
        #joueur4 =0
        
        self._jeton=None


    #getter de l'attribut
    def get_cards(self):
        return self._cards
    
    #setter de l'attribut
    def set_cards(self,cards):
        self._cards =  cards

    cards=property(get_cards,set_cards)


    #getter de l'attribut
    def getter_player1(self):
        return self._player1

    #setter de l'attribut
    def setter_player1(self,player):
        self._player1 =  player

    #property sur l'attribut
    player1=property(getter_player1,setter_player1)    

    
    #getter de l'attribut
    def getter_player2(self):
        return self._player2

    #setter de l'attribut
    def setter_player2(self,player):
        self._player2 =  player

    #property sur l'attribut
    player2=property(getter_player2,setter_player2)


    #getter de l'attribut
    def getter_player3(self):
        return self._player3

    #setter de l'attribut
    def setter_player3(self,player):
        self._player3 =  player

    #property sur l'attribut
    player3=property(getter_player3,setter_player3)

    #getter de l'attribut
    def getter_player4(self):
        return self._player4

    #setter de l'attribut
    def setter_player4(self,player):
        self._player4 =  player

    #property sur l'attribut
    player4=property(getter_player4,setter_player4)

    #getter de l'attribut
    def getter_tapis(self):
        return self._tapis

    #setter de l'attribut
    def setter_tapis(self,tapis):
        self._tapis =  tapis

    #property sur l'attribut
    tapis=property(getter_tapis,setter_tapis)


    #getter de l'attribut
    def getter_choix(self):
        return self._choix

    #setter de l'attribut
    def setter_choix(self,choix):
        self._choix =  choix

    #property sur l'attribut
    choix=property(getter_choix,setter_choix)

    #getter de l'attribut
    def getter_jeton(self):
        return self._jeton

    #setter de l'attribut
    def setter_jeton(self,jeton):
        self._jeton =  jeton

    #property  sur l'attribut
    jeton=property(getter_jeton,setter_jeton)

    def getter_choix_attout_color(self):
        return self._choix_attout_color
    
    def setter_choix_attout_color(self,choix_attout_color):
         self._choix_attout_color=choix_attout_color
    
    #property  sur l'attribut
    choix_attout_color=property(getter_choix_attout_color,setter_choix_attout_color)

    # creation de toutes les cartes graces a la liste de 
    def Create_Cards(self):
        self.cards=[]
        for colour in colours:
            for  name in card_names:
                #creation dd'une carte
                card =Card()
                card.colour=colour
                card.name=name
                card.score=0
                card.image=str(name+'_of_'+colour+'.png')
                
                card.is_ok()
                #ajouter la cards a la liste de cartes
                #add_card_cards(Card)  erreeur car ne trouve la fonction
                self.cards.append(card)

        #melanger les cartes à la creation
        rd.shuffle(self.cards)
       


        
# fonction de creation d'un joueur de la classe 
# important de le faire ainsi car il y as plusieurs attributs pour 1 Joueur 
# par defaut:# par defaut:
#joueur nom =Papi 
#Type =True (humain)
# main = [] (liste vide ) 
# Groupe = [] (liste vide ) 
    def Create_PLayer(self,player_number,name_player="Papi",type_player=True,hand=[],group=[]):
        
        player=Player()

        # on definit le nom du joueur
        player.name_player=name_player

        # on definit la main du joueur
        player.hand=hand
        
        # on definit la le type de joueur
        player.type_player=type_player

        # on definit le groupe du joueur
        player.group=group      

        player.is_ok()

        if player_number==1:
            self.player1=player

        if player_number==2:
            self.player2=player

    
        if player_number==3:
            self.player3=player

        if player_number==4:
            self.player4=player        


    # fonction pour ajouter une carte a la main du joueur
    def add_card_cards(self,Card):
        self.cards.append(Card)

    # fonction pour retirer une carte a la main du joueur
    def remove_card_cards(self):
        self.cards.pop()


    #code pour verifier la creation des cartes  
    def print_Cards(self):
        for card in self.cards:
            print(card.colour)

    # fonction pour melanger les cartes (battre les carte)
    def shuffle_Cards(self):
        self.cards=rd.shuffle(self.cards)
    
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
            card=self.cards[i]
            player.add_card_Hand(card)
            self.cards.pop(i)

    
    #creation de tapis vide
    def creation_tapis(self):
        self.tapis = []
        

    # ajout de carte dans tapis
    def add_card_tapis(self,card):
        self.tapis.append(card)

    #retirer des cartes dans le tapis
    def remove_card_tapis(self):
        self.tapis.pop()

        
    def choix_attout(self):
    #dans cette fontion je rajoute une carte au tapis afin de choisir la carte de attout
        

        # ajout du dernier element des cartes dans la variable atout
        self.choix= self.cards[-1]
        
        #ajout de la variable dans tapis
        self.add_card_tapis(self.choix)

        #mise à jour des cartes
        self.cards.pop()

     
    def choix_atout_IA_first_row(self ,number_player,choix):
        if not (1 <= number_player <= 4):
            raise ValueError("Number of player must be between 1 and 4")

        # creer une list au hazard
        shuffled_suits=[]  
        # shuffled_suits = list(colours)
        colour=choix.colour
        shuffled_suits.append(colour)
        shuffled_suits.append("pass")
        np.random.shuffle(shuffled_suits)

        # Choose the atout based on the shuffled list
        return shuffled_suits[0]
        
        

    def choix_atout_IA_second_row(self ,number_player,choix):
        
        if not (1 <= number_player <= 4):
            raise ValueError("Number of player must be between 1 and 4")

     # creer une list au hazard
    
        shuffled_suits = list(colours)
        #retirer la couleur du choix dans le nouveau choix
        shuffled_suits.pop(shuffled_suits.index(choix.colour))
        shuffled_suits.append("pass")
        np.random.shuffle(shuffled_suits)

        # Choose the atout based on the shuffled list
        return shuffled_suits[0]
    

    def redistribute_card_player_atout(self,player):
        #dans cette fonction je donne 3 cartes au joueur qui as choisit l'attout
        
        #la premiere c'est la carte qui est sur le tapis que je tranfert a la main du joueur
        player.add_card_Hand(self.tapis[0])
        self.remove_card_tapis()
        #ajouter 2 carte de Cards a la main du joueur ,
        #je prend les deux dernière
        for _ in range(2):
            if self.cards:
                player.add_card_Hand(self.cards.pop())
            else:
                # Handle the case where there are not enough cards in the deck.
                print("Not enough cards in the deck.")  

    def redistribute_card_player(self,player):
        # Dans cette fonction, je donne 3 cartes au joueur.
        # Ajouter 3 cartes à la main du joueur.
        for _ in range(3):
            if self.cards:
                player.add_card_Hand(self.cards.pop())
            else:
                # Handle the case where there are not enough cards in the deck.
                print("Not enough cards in the deck.")  
            

        





    def mise_a_jour_score_cards_player(self,player,colour_atout):
        for card in player.hand:
            card.score = valeur_atout(card.name) if card.colour == colour_atout else valeur_non_atout(card.name)


    def play(self,player,card):

            #on ajoute la carte au tapis
           
            self.add_card_tapis(card)
            # on retire la carte de la main du joueur
            if card in player.hand:
                player.remove_card_Hand(card)
            else:
                print(f"La carte {card} n'est pas dans la main du joueur.")    
                
              



    def determine_gagnant_pli(self):
        # Vérifie si le tapis contient 4 cartes (indiquant un pli complet)
        if len(self.tapis) == 4:
            couleur_attout = self.choix_attout_color  # La couleur principale est la couleur de la première carte jouée
            # Vérifie si la couleur principale est une couleur d'atout
            
            # Détermine le gagnant en fonction de la carte de plus grand score
            carte_gagnante = self.tapis[0]
            for carte in self.tapis[1:]:
                if (carte.colour == couleur_attout ):
                    if(carte_gagnante.colour== couleur_attout):
                    # dans cette condition on une carte atout et une carte gagnante atout aussi 
                        if (carte.score > carte_gagnante.score ):
                            carte_gagnante = carte

                    # dans cette condition on une carte atout dans le jeu mais la carte gagnante est pas atout
                    else:
                       carte_gagnante  =  carte

                #    dans ce cas on une carte qui n'est pas atout    
                else:
                    # je verifie si il sont de la meme couleur
                    if( carte.colour== carte_gagnante.colour):
                        if (carte.score > carte_gagnante.score ):
                            carte_gagnante = carte


            # Détermine le joueur gagnant en fonction de la carte gagnante
            if carte_gagnante == self.tapis[0]:
                return self.player1
            elif carte_gagnante == self.tapis[1]:
                return self.player2
            elif carte_gagnante == self.tapis[2]:
                return self.player3
            elif carte_gagnante == self.tapis[3]:
                return self.player4
            else:
                # Gère une égalité ou une situation inattendue
                return None
        else:
            # Gère le cas où le pli n'est pas complet
            return None


        

        

        

#---------------------------------------------------------------------------------------------------------------------------------------
        
class Card:
    
    def __init__(self):
        self._name  =None
        self._colour=None
        self._score =None
        self._image =None

    #getter de l'attribut 
    def get_name(self):
        return self._name
    
    #setter de l'attribut
    def set_name(self,card_name):
        self._name=card_name

    #property sur l'attribut name
    name=property(get_name,set_name)

    #setter de l'attribut 
    def set_colour(self,colour):
        self._colour=colour

    #getter de l'attribut 
    def get_colour(self):
        return self._colour 

    #property sur l'image 
    colour=property(get_colour,set_colour)   

    #setter de l'attribut 
    def set_score(self,score):
        self._score=score

    #getter de l'attribut 
    def get_score(self):
        return self._score 

    #property sur l'image 
    score=property(get_score,set_score)   

    #setter de l'attribut 
    def set_image(self,image):
        self._image=image

    #getter de l'attribut 
    def get_image(self):
        return self._image 

    #property sur l'image 
    image=property(get_image,set_image) 

    # method de test pour voir si 
    def is_ok(self):
        none_attributes = [key for key, value in self.__dict__.items() if value is None]
    
        if none_attributes:
            raise CardError(f"Card instance has None values for attributes: {none_attributes}")  


#---------------------------------------------------------------------------------------------------------------------------------------

class Player:
    def __init__(self):
        # nom du joueur
        # type= Chaine de caractere
        self._name_player=None 

        # la main du joueur
        # type= liste
        self._hand=None

        # le type  du joueur(bool())
        # type= bool (true humain , False IA)
        self._type_player=None
        
        self._group=None

    def get_name_player(self):
        return self._name_player
    
    def set_name_player(self,name_Player):
       self._name_player=name_Player
       
    name_player = property(get_name_player,set_name_player)
    #    a =P¨layer()
        # a.name_player=prince
        # X=a.name_player
        

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

    # fonction pour retirer une carte a la main du joueur
    def remove_card_Hand(self,Card):
        self.hand.remove(Card)


    # method de test pour voir si 
    def is_ok(self):
        none_attributes = [key for key, value in self.__dict__.items() if value is None]
    
        if none_attributes:
            raise PlayerError(f"Player instance has None values for attributes: {none_attributes}")
        

    def random_card_hand(self):
        if self.hand:
            # Utilisation de random.choice pour choisir une carte aléatoire dans la main
            random_card = rd.choice(self.hand)
            
            return random_card
        else:
            print("The player's hand is empty.")
            return None    
        


    


class PlayerError(Exception):
    pass


class CardError(Exception):
    pass
    












