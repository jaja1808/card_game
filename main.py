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
        new_Game.Create_PLayer(1,"Papi",True,[],[])
        #creation Joueur 2
        new_Game.Create_PLayer(2,"Prince",False,[],[])
        #creation Joueur 3
        new_Game.Create_PLayer(3,"Brian",False,[],[])
        #creation Joueur 4
        new_Game.Create_PLayer(4,"Alain",False,[],[])



        # evolution 
        ETAPE=300

    elif ETAPE==300:
        # etape  qui consiste à distribuer a chaque joueur 5 cartes 
        new_Game.Distribute(1) # joueur 1(papi)
        new_Game.Distribute(2)  #(prince)
        new_Game.Distribute(3)      #(Brian)
        new_Game.Distribute(4)  #(Alain)


    #    for i in new_Game.Players():
    #     print(i.main())

        print (new_Game.Players())

        # mise a jour Etape
        ETAPE=400  



        





"""
------------------------------------------------------------------------------------
-----------------------------  FIN Boucle Principale   -----------------------------
------------------------------------------------------------------------------------
"""    