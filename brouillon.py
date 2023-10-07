


import numpy as np
import random as rd







# Définition des valeurs et des couleurs des cartes
valeurs = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

# Création d'un jeu de cartes
jeu_de_cartes = [{'valeur': valeur, 'couleur': couleur} for valeur in valeurs for couleur in couleurs]

# Fonction pour mélanger les cartes
def melanger_cartes(jeu):
    random.shuffle(jeu)




def distribuer_cartes_debut(jeu, nb_joueurs):
    main_joueurs = [[] for _ in range(nb_joueurs)]
    for _ in range((len(jeu)-12) // nb_joueurs):
        for i in range(nb_joueurs):
            carte = jeu.pop()
            main_joueurs[i].append(carte)
    return main_joueurs


def distribuer_cartes_fin(jeu, nb_joueurs):
    main_joueurs = [[] for _ in range(nb_joueurs)]
    for _ in range((len(jeu)-12) // nb_joueurs):
        for i in range(nb_joueurs):
            carte = jeu.pop()
            main_joueurs[i].append(carte)
    return main_joueurs


# Mélanger les cartes
melanger_cartes(jeu_de_cartes)

# Distribuer les cartes à quatre joueurs
main_joueurs = distribuer_cartes_debut(jeu_de_cartes,4)
main_joueurs =distribuer_cartes_fin(jeu_de_cartes,4)

#Afficher la main de chaque joueur
for i, main in enumerate(main_joueurs):
    print(f"Joueur {i + 1}: {main}")
    print ("________")
    print ("________")

print(main_joueurs[0])
# ...clc

"""
# Fonction pour calculer les points de chaque équipe à la fin de la manche
def calculer_points_manche(plis, contrat):
    points = {'Équipe1': 0, 'Équipe2': 0}

    # Calcul des points des plis remportés
    for pli in plis:
        couleur_atout = contrat['couleur_atout']
        pli_trie = sorted(pli, key=lambda x: (x['couleur'] == couleur_atout, valeurs.index(x['valeur'])), reverse=True)
        points_gagnants = pli_trie[0:2]
        equipe_gagnante = contrat['preneur'] if points_gagnants[0] in pli else contrat['défense']
        points[equipe_gagnante] += sum(valeurs_points[carte['valeur']] for carte in points_gagnants)

    # Ajoute des points annonces de contrat
    points[contrat['preneur']] += contrat['points_contrat']

    return points

    
"""

# 1 test annonce de contrat
contrat = {'preneur': 'Équipe1', 'défense': 'Équipe2', 'points_contrat': 162, 'couleur_atout': 'Coeur'}

# Les plis remportés (chaque pli est une liste de cartes)
plis = [[{'valeur': '7', 'couleur': 'Coeur'}, {'valeur': 'A', 'couleur': 'Coeur'}, ...], ...]

# Calcul des points à la fin de la manche
#points_manche = calculer_points_manche(plis, contrat)
#print(points_manche)


