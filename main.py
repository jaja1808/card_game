# new line
from classes_commun import *

# from classes_backend import *


# creation d'une variable Etape qui definit nos conditions
ETAPE=0

ETAPE=100

"""
partie de pré-congiguration frontend
------------------------------------------------------------
pg.init()
game widraw


"""



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
        
        


        """
        c'est dans cette etape que l'on initialise le jeu
        ici on initialise aussi le pygame

        pg.init()
        """
        # afficher les cartes crées
        


        # evolution 
        # ETAPE=int(input(" rentrer la valeur 200 pour faire evoluer le programme    ") )
        """
        je suis dans l'attente du front- end
        etape front =200
        """
        ETAPE=200
      

    elif ETAPE==200:
        # etape 200 creation des 4 joueurs 



        """
        front-end
        attente de nom de joueur sous forme de string
        joueur principal

        user_name (string)

        attente d'un return d'une fonction


        dans une boucle if 
        name=fontion()
        new_Game.Create_PLayer(1,name,True,[],[])

        etape front_end=300

        """

        #creation Joueur 1
        new_Game.Create_PLayer(1,"Papi",True,[],[])
        #creation Joueur 2
        new_Game.Create_PLayer(2,"Prince",False,[],[])
        #creation Joueur 3
        new_Game.Create_PLayer(3,"Brian",False,[],[])
        #creation Joueur 4
        new_Game.Create_PLayer(4,"Alain",False,[],[])


        
        # evolution 
        # ETAPE=int(input(" rentrer la valeur 300 pour faire evoluer le programme    ") )
        ETAPE=300
        

    elif ETAPE==300:
        # etape  qui consiste à distribuer a chaque joueur 5 cartes 
        new_Game.Distribute(1)  #joueur 1(papi)
        new_Game.Distribute(2)  #(prince)
        new_Game.Distribute(3)  #(Brian)
        new_Game.Distribute(4)  #(Alain)


        new_Game.display_players_hands()




        
        # evolution 
        ETAPE=int(input(" rentrer la valeur 400 pour faire evoluer le programme    ") )


        """
        renvoeyer la main du joueur 
        renvoyer la carte de choix d'atout 
        choix atout= last_cards


        etape front etape 300


        attente front_etape 400
        """

    elif ETAPE ==400:
        """
        etape choix atout
        """

        """
        attente de l'affichage de choix atout 
        attente 
        choix=0 
        choix=1 oui 
        choix=2 pass

        """

        pass
        break     



    elif ETAPE ==400:
        """
        etape choix atout
        """

        """
        attente de l'affichage de choix atout 
        attente 
        choix=0 
        choix=1 oui 
        choix=2 pass
        
        """

        pass
        break     
   


        





"""
------------------------------------------------------------------------------------
-----------------------------  FIN Boucle Principale   -----------------------------
------------------------------------------------------------------------------------
"""    