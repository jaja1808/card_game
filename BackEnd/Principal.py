import classes_backend
from classes_commun import *

from classes_backend import *


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



    elif ETAPE==200:
        # etape 200 creation des 4 joueurs 

        #creation Joueur 1
        new_Game.CreatePLayer1("Papi",I_A)
        #creation Joueur 2
        new_Game.CreatePLayer("Papi",I_A)






"""
------------------------------------------------------------------------------------
-----------------------------  FIN Boucle Principale   -----------------------------
------------------------------------------------------------------------------------
"""    