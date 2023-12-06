import numpy as np
import random
"""
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
# jusbfibqiybbriunfddd


"""


class Player:
    def __init__(self):
        self._name_Player = None
        self._hand =  None
        self._type_player = None
        self._group = None

    def get_name_Player(self):
        return self._name_Player

    def set_name_Player(self, name_Player):
        self._name_Player = name_Player

    name_Player = property(get_name_Player, set_name_Player)

    def get_hand(self):
        return self._hand

    def set_hand(self, hand):
        self._hand = hand if hand is not None else []

    @property
    def hand(self):
        return self.get_hand()
    
    @hand.setter
    def hand(self, value):
        self.set_hand(value)

    def get_type_player(self):
        return self._type_player

    def set_type_player(self, type_player):
        self._type_player = type_player

    type_player = property(get_type_player, set_type_player)

    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group

    group = property(get_group, set_group)

    def add_card_hand(self, card):
        self.hand.append(card)

    def remove_card_hand(self, card):
        self.hand.remove(card)
