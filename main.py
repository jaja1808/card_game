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
            
            names = [new_Game.player4.name_player, new_Game.player2.name_player, new_Game.player3.name_player]
            back_cards(image_path, names)
            

            # etape  qui consiste à distribuer a chaque joueur 5 cartes 
            new_Game.Distribute(1)  #joueur 1(papi)
            new_Game.Distribute(2)  #(prince)
            new_Game.Distribute(3)  #(Brian)
            new_Game.Distribute(4)  #(Alain)

            #ajouter la derniere carte au tapis pour choix attout
            # ajouter une carte sur le tapis
            new_Game.choix_attout()
            
            # Getting the hand of the user
            hand = new_Game.player1.hand
            # Retrieving the card of atout
            choix_atout = new_Game.choix.image
            # Retreaving the colour of atout
            atout_colour = new_Game.choix.colour
            # Arranging the list of atouts
            atouts = arrange_atout(atout_colour, colours)

            """        
            renvoeyer la main du joueur 
            renvoyer la carte de choix d'atout 
            etape front etape 300
            tu prend new_Game.choix
            attente front_etape 400
            """
            #Displaying the hand
            display_hand(hand, image_path)
            
            # Displaying the atout
            new_Game.choix_attout_color = display_popup(choix_atout, image_path, atouts)

            print(new_Game.choix_attout_color)

            etape = 400
    

        elif etape ==400:
            """
            tape choix atout
            """
  
        # mise a jour de la valeur choix de la part du frontend
        # new_Game.choix_attout_color=xxxxxxxxxxxx
        
            #new_Game.choix_attout_color="pass"

            #le joueur a choisit passer le choix
            if new_Game.choix_attout_color=="pass":
                etape=401

            else :
                etape=450
                # mise a jour de _choix_attout
                '''attout presente est prise'''
        
        elif etape == 401:
            """
            etape choix atout Joeur 1
            """
            print("etape 401")

            # mise a joueur jeton (valeur en angle )
            new_Game.jeton=270
            # Hide part of the card 
            pg.draw.rect(game, BACKGROUND, (359, 265, 83, 60))
            # Draw Jeton
            draw_arrow(new_Game.jeton, image_path)

            # Display the choix attout
            # new_Game.choix_attout_color = draw_atout(atouts, image_path)
            print(new_Game.choix_attout_color)
            etape= 402

            
        elif etape ==402:
            """
            etape choix atout Joueur 2
            """
            new_Game.jeton=180
            # Draw Jeton
            draw_arrow(new_Game.jeton, image_path)

            new_Game.choix_attout_color=new_Game.choix_atout_IA_first_row(2,new_Game.choix)

            if new_Game.choix_attout_color=='pass':
                etape=403
            # mise a jour de _choix_attout
            else :
                etape=450

        elif etape ==403:
            """
            etape choix atout Joueur 3
            """
            new_Game.jeton=90
            # Draw Jeton
            draw_arrow(new_Game.jeton, image_path)
            
            new_Game.choix_attout_color=new_Game.choix_atout_IA_first_row(3,new_Game.choix)

            if new_Game.choix_attout_color=='pass':
                etape=404
            # mise a jour de _choix_attout
            else :
                etape=450      

        elif etape ==404:
            """
            etape choix atout Joueur 4
            """
            new_Game.jeton=0
            # Draw Jeton
            draw_arrow(new_Game.jeton, image_path)
            
            new_Game.choix_attout_color=new_Game.choix_atout_IA_first_row(4,new_Game.choix)
           

            if new_Game.choix_attout_color=='pass':
                etape=405
            # mise a jour de _choix_attout
            else :
                etape=450

        
        elif etape ==405:
            """
            etape choix atout Joueur 1 
            apres que tout monde aie pass
            """
            new_Game.jeton=270

            # attente frontend choix 
            # new_Game.choix_attout_color=xxxxxxxxxxxxx
            
            
            

            if new_Game.choix_attout_color=='pass':
                etape=406
            # mise a jour de _choix_attout
            else :
                etape=450

        elif etape ==406:
            """
            etape choix atout Joueur 2 
            apres que tout monde aie pass
            """
            new_Game.jeton=180
            new_Game.choix_attout_color=new_Game.choix_atout_IA_second_row(2,new_Game.choix)

            if new_Game.choix_attout_color=='pass':
                etape=407
            # mise a jour de _choix_attout
            else :
                etape=450

        elif etape ==407:
            """
            etape choix atout Joueur 3 
            apres que tout monde aie pass
            """
            new_Game.jeton=90


            new_Game.choix_attout_color=new_Game.choix_atout_IA_second_row(3,new_Game.choix)

            if new_Game.choix_attout_color=='pass':
                etape=408
            # mise a jour de _choix_attout
            else :
                etape=450


        elif etape ==408:
            """
            etape choix atout Joueur 4 
            apres que tout monde aie pass
            """
            new_Game.jeton=0

            new_Game.choix_attout_color=new_Game.choix_atout_IA_second_row(4,new_Game.choix)

            if new_Game.choix_attout_color=='pass':
                etape=1000
            # mise a jour de _choix_attout
            else :
                etape=450


                
            """
            attente de l'affichage de choix atout 
            attente
    
            choix=0 
            choix=1 oui 
            choix=2 pass
            
                
            ici j'envoie l'etat du jeton 
            et le choix de chacun des joueurs

            
            jeton 
            #joueur1 =270
            #joueur2 =180
            #joueur3 =90
            #joueur4 =0

            """
            pass


        elif etape ==450:
            """
            redistribution des cartes

            ici j'envoit toute les 3 autres cartes aux joueurs 

            j'envoie de jeton du premier qui vas joueur
            """

            if new_Game.jeton==270:
                # joueur1 qui as fait le choix
                new_Game.redistribute_card_player_atout(player=new_Game.player1)
                new_Game.redistribute_card_player(player=new_Game.player2)
                new_Game.redistribute_card_player(player=new_Game.player3)
                new_Game.redistribute_card_player(player=new_Game.player4)
                etape=500

            if new_Game.jeton==180:   
                # joueur2 qui as fait le choix
                new_Game.redistribute_card_player_atout(player=new_Game.player2)
                new_Game.redistribute_card_player(player=new_Game.player1)
                new_Game.redistribute_card_player(player=new_Game.player3)
                new_Game.redistribute_card_player(player=new_Game.player4)
                etape=500


            if new_Game.jeton==90:   
                # 3 qui as fait le choix
                new_Game.redistribute_card_player_atout(player=new_Game.player3)
                new_Game.redistribute_card_player(player=new_Game.player1)
                new_Game.redistribute_card_player(player=new_Game.player2)
                new_Game.redistribute_card_player(player=new_Game.player4)
                etape=500


            if new_Game.jeton==0:   
                # 4 qui as fait le choix
                new_Game.redistribute_card_player_atout(player=new_Game.player4)
                new_Game.redistribute_card_player(player=new_Game.player1)
                new_Game.redistribute_card_player(player=new_Game.player2)
                new_Game.redistribute_card_player(player=new_Game.player3)

                etape=500
                        



        elif etape ==500:
            """


            mise a jour des scores des differente cartes
            
            """
            new_Game.mise_a_jour_score_cards_player(new_Game.player1,new_Game.choix_attout_color)
            new_Game.mise_a_jour_score_cards_player(new_Game.player2,new_Game.choix_attout_color)
            new_Game.mise_a_jour_score_cards_player(new_Game.player3,new_Game.choix_attout_color)
            new_Game.mise_a_jour_score_cards_player(new_Game.player4,new_Game.choix_attout_color)
            
            # evolution etape
            etape=549


        elif etape ==549:
            
            
            #premiee tour de jeu c'est le joeur 1 qui debute
            new_Game.jeton=270
            # evolution etape
            etape =550



        
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


            # controle du jeton 
            if new_Game.jeton== 270:
                # joueur 1
                # evolution etape
                etape =551


            if new_Game.jeton== 180:
                # joueur 2
                # evolution etape
                etape =552

            if new_Game.jeton== 90:
                # joueur 3
                # evolution etape
                etape =553


            if new_Game.jeton== 0:
                # joueur 4
                # evolution etape
                etape =554        

            # mise a jour de jeton car premier tour de cycle
            

            




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

            #dans l'attente du frontend carte à jouer 
            # new_Game.player1.play(xxxxxxxxxxxxxxxx)

            #
            # new_Game.player1.play(card))






            
            
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

        elif etape ==554:
            """
        debut du jeu si c'est joueur 4 qui debute


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