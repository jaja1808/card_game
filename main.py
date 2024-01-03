import pygame as pg
from classes_commun import *
from pathlib import Path
from FrontEnd.front_func import *
# from classes_backend import *

# image path
image_path = Path.cwd() / 'images'

# creation d'une variable etape qui definit nos conditions
#etape = 0

"""
partie de pré-congiguration frontend
------------------------------------------------------------
"""
# Initializing pygame
pg.init()

# Creating game window 
game = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pg.display.set_caption("Belote Game")

# Variable for game 
run = True

"""
------------------------------------------------------------------------------------
-----------------------------  Boucle Principale   ---------------------------------
------------------------------------------------------------------------------------

"""
# Keep the game going 
while run:
    
    # Set background color
    game.fill(BACKGROUND)

    etape = 100

    while etape!=0:
        
        if etape==100:
            # etape 100 debut de la partie
            # creation d'une instance game()
            new_Game=Game()
            # creation de toute les cartes
            new_Game.Create_Cards()

            """
            je suis dans l'attente du front- end
            attente d'une variable 200
            par click bouton new game
            etape front =200
            """

            # The page of clicking new game button to launch the game
            etape = first_page(image_path)
            print(etape)
            """
            c'est dans cette etape que l'on initialise le jeu
            """

            # afficher les cartes crées
            # evolution 
            # etape=int(input(" rentrer la valeur 200 pour faire evoluer le programme ") )

        elif etape==200:
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
            # name of the user 
            name , etape = user_input(image_path)
            print(name, etape)
            
            #creation Joueur 1
            new_Game.Create_PLayer(1, name, True, [], [])
            #creation Joueur 2
            new_Game.Create_PLayer(2,"Prince",False,[],[])
            #creation Joueur 3
            new_Game.Create_PLayer(3,"Brian",False,[],[])
            #creation Joueur 4
            new_Game.Create_PLayer(4,"Alain",False,[],[])

            #creation d'un tapis vide
            new_Game.creation_tapis()
        
            # evolution 
            # etape=int(input(" rentrer la valeur 300 pour faire evoluer le programme    ") )
            game.fill(BACKGROUND)
        

        elif etape==300:
            
            #names = [new_Game.player4.name_player, new_Game.player2.name_player, new_Game.player3.name_player]
            #back_cards(image_path, names)
            

            # etape  qui consiste à distribuer a chaque joueur 5 cartes 
            new_Game.Distribute(1)  #joueur 1(papi)
            new_Game.Distribute(2)  #(prince)
            new_Game.Distribute(3)  #(Brian)
            new_Game.Distribute(4)  #(Alain)

            #ajouter la derniere carte au tapis pour choix attout
            # ajouter une carte sur le tapis

            new_Game.choix_attout()

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

        # mise a jour de la valeur choix de la part du frontend
        # new_Game.choix=xxxxxxxxxxxx

            #le joueur a choisit de valider le choix
        if new_Game.choix==1:
            
            #mise a jour des valeurs de score des toutes les cartes
               


            # mise a jour de choix
            new_Game.choix=0

                #evolution du grafcet vers l'etape avant la redistribution
                etape=450
        
            #le joueur a choisit pass
            if new_Game.choix==2:
                # mise a jour de choix
                new_Game.choix=0
                
                #evolution du grafcet vers l'etape avant la redistribution
                etape=401
            


        elif etape ==401:
            """
            etape choix atout Joeur 1
            """

            # mise a joueur jeton
            new_Game.jeton=1
            
        # mise a jour de la valeur choix de la part du frontend
        # new_Game.choix=xxxxxxxxxxxx


             #le joueur a choisit de valider le choix
            if new_Game.choix==1:
            
            # mise a jour de choix
                new_Game.choix=0

            #evolution du grafcet vers l'etape avant la redistribution
                etape=451
    
            #le joueur a choisit pass
            if new_Game.choix==2:
            # mise a jour de choix
                new_Game.choix=0
            
                #evolution du grafcet vers l'etape avant la redistribution
                etape=402



            """
            attente de l'affichage de choix atout 
            attente
    
            choix=0 
            choix=1 oui 
            choix=2 pass
            
                
            ici j'envoie l'etat du jeton 
            et le choix de chacun des joueurs

            
            jeton 
            0   joueur principal 
            1   joeur a gauche
            2   joeur en face
            3   joueur à droite 

            """
            pass


        elif etape ==500:
            """
            redistribution des cartes

            ici j'envoit toute les 3 autres cartes aux joueurs 

            j'envoie de jeton du premier qui vas joueur
            """

            pass




        
        elif etape ==550:
            """
        debut du jeu
            si joueur principale

        j'envoie une liste (tapis) [de carte] dans ce cas vide
            attente  de objet

            envoie 
            score partenaire
            score adversaire

        si c'est joueur qui doit jouer je suis dans cette
            """

            pass


        elif etape ==551:
            """
        debut du jeu si c'est joueur 1 qui debute


        j'envoie une liste (tapis) [de carte]
            
        
        j'envoie jeton 
        
            envoie 
            score partenaire
            score adversaire


        si c'est joueur qui doit jouer je suis dans cette
            """

            pass
            
        elif etape ==552:
            """
        debut du jeu si c'est joueur 2 qui debute


        j'envoie une liste (tapis) [de carte]

        j'envoie jeton 
            
        
        
            envoie 
            score partenaire
            score adversaire

        si c'est joueur qui doit jouer je suis dans cette
            """

            pass



        elif etape ==553:
            """
        debut du jeu si c'est joueur 3 qui debute


        j'envoie une liste (tapis) [de carte]

        j'envoie jeton 
        
        

        
        
            envoie 
            score partenaire
            score adversaire


        si c'est joueur qui doit jouer je suis dans cette
            """

            pass




        elif etape ==600:

            """
        debut du jeu si c'est joueur 3 qui debute


        j'envoie une liste (tapis) [de carte]

        j'envoie jeton 
        
        

        
        
            envoie 
            score partenaire
            score adversaire


        si c'est joueur qui doit jouer je suis dans cette
            """

            pass




        elif etape ==900:
            
            """
            last tour
            dernier tour de jeu

            apres
        
        

        
        
            envoie 
            score partenaire
            score adversaire


        si c'est joueur qui doit jouer je suis dans cette
            """

            pass



        elif etape ==1000:
            """
            
            plus de carte sur le tapis jeu finis
        

            score final partenaire
            score final advaire
        
            game finish 
            """

            pass

    # if __name__ == "__main__":




    """
    ------------------------------------------------------------------------------------
    -----------------------------  FIN Boucle Principale   -----------------------------
    ------------------------------------------------------------------------------------
    """    
 
    # Update the Display
    pg.display.flip()

    # Event Listen to Quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

# Quitting the game
pg.quit()