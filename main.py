# new line
from classes_commun import *

# from classes_backend import *


# creation d'une variable Etape qui definit nos conditions
ETAPE=0

ETAPE=100

"""
------------------------------------------------------------------------------------
-----------------------------  Boucle Principale   ---------------------------------
------------------------------------------------------------------------------------
"""
while ETAPE!=0:
    
    if ETAPE==100:
        # etape 100 debut de la partie
        # creation d'une instance game()
        new_Game=Game()

        # creation de toute les cartes
        new_Game.Create_Cards()
        
        # evolution 
        ETAPE=200

    elif ETAPE==200:
        # etape 200 creation des 4 joueurs 

        #creation Joueur 1
        new_Game.CreatePLayer(1,"Papi",True,[],[])
        #creation Joueur 2
        new_Game.CreatePLayer(2,"Prince",False,[],[])
        #creation Joueur 3
        new_Game.CreatePLayer(3,"Brian",False,[],[])
        #creation Joueur 4
        new_Game.CreatePLayer(4,"Alain",False,[],[])



        # evolution 
        ETAPE=300

    elif ETAPE==300:
        # etape  qui consiste à distribuer a chaque joueur 5 cartes 

        for player in range(4):
            new_Game.distribute(player)
        





"""
------------------------------------------------------------------------------------
-----------------------------  FIN Boucle Principale   -----------------------------
------------------------------------------------------------------------------------
"""    